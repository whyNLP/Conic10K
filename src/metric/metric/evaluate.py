import re, warnings, itertools
from typing import List, Tuple
from collections import OrderedDict
from tqdm import tqdm

from sympy.parsing.sympy_parser import (parse_expr,\
     standard_transformations, convert_equals_signs,\
     lambda_notation, repeated_decimals, auto_number,\
     factorial_notation)
from sympy import Symbol, Function, Dummy
from sympy.simplify.simplify import simplify
from sympy.core import Add, Mul, Pow, Number, Tuple
from sympy.core.relational import Relational
from sympy.core.numbers import NumberSymbol
from sympy.core.basic import Basic

from tokenize import (NAME, OP)
from keyword import iskeyword


# ===== Helper objects for sympy =====

class TypeSymbol(Symbol):
    """
    A decorator for Symbol to allow additional information. We have to define
    a new class since Symbol uses `__slots__` to save memory.
    """

    __slots__ = ('name', 'type')

    def __new__(cls, name, **assumptions):
        """Override the __new__ function to enforce symbols with different
        types map to difference objects. The type string is written to the
        assumption of a symbol.
        """
        type_: str = assumptions.pop('type', 'Object')
        assumptions['is_type_%s' % type_] = True

        return super().__new__(cls, name, **assumptions)
    
    def __init__(self, *args, **kwargs):
        self.type: str = kwargs.pop('type', 'Object')
        # XXX: it is strange that super() is object instead of Symbol
        # super().__init__(*args, **kwargs)

# Override keywords in sympy
_default_local_dict = {
    'N': Symbol('N'),
    'O': Symbol('O'),
    'S': Symbol('S'),
    'Eq': Function('Eq'),
    'Intersection': Function('Intersection'),
    'DotProduct': Function('DotProduct'),
    'degree': Symbol('degree'),
    'Range': Function('Range'),
    'beta': Symbol('beta'),
    'Max': Function('Max'),
    'Min': Function('Min'),
    'And': Function('And')
}

# Functions that are insensitive to argument order
_order_insensitive_functions = [
    'Eq', 'set', 'Distance', 'DotProduct', 'InterReciprocal', 'Intersection', 'LineOf', 'LineSegmentOf', 'NumIntersection', 'TangentPoint', 'TriangleOf', 'Add', 'Mul', 'IsIntersect', 'IsParallel', 'IsPerpendicular', 'IsSeparated', 'IsTangent', 'IsOutTangent', 'IsInTangent', 'FootPoint'
]

# Rewrite the parse algorithm to allow equations as function arguments
def auto_symbol(tokens, local_dict, global_dict):
    """Inserts calls to ``Symbol``/``Function`` for undefined variables."""
    result = []
    prevTok = (None, None)

    tokens.append((None, None))  # so zip traverses all tokens
    for tok, nextTok in zip(tokens, tokens[1:]):
        tokNum, tokVal = tok
        nextTokNum, nextTokVal = nextTok
        if tokNum == NAME:
            name = tokVal

            if (name in ['True', 'False', 'None']
                or (iskeyword(name) and name != 'lambda')
                # Don't convert attribute access
                or (prevTok[0] == OP and prevTok[1] == '.')
                # Do convert keyword arguments
                or (prevTok[0] == OP and prevTok[1] in ('(', ',')
                    and nextTokNum == OP and nextTokVal == '=') and False):
                result.append((NAME, name))
                continue
            elif name in local_dict:
                if isinstance(local_dict[name], Symbol) and nextTokVal == '(':
                    result.extend([(NAME, 'Function'),
                                   (OP, '('),
                                   (NAME, repr(str(local_dict[name]))),
                                   (OP, ')')])
                else:
                    result.append((NAME, name))
                continue
            elif name in global_dict:
                obj = global_dict[name]
                if isinstance(obj, (Basic, type)) or callable(obj):
                    result.append((NAME, name))
                    continue

            result.extend([
                (NAME, 'Symbol' if nextTokVal != '(' else 'Function'),
                (OP, '('),
                (NAME, repr(str(name))),
                (OP, ')'),
            ])
        else:
            result.append((tokNum, tokVal))

        prevTok = (tokNum, tokVal)

    return result

def auto_interval(tokens, local_dict, global_dict):
    """
    Deal with the intervals (a, b), [a, b], [a, b), (a, b] in sentences.
     - (a, b) -> tuple(a, b)
     - (a, b] -> Interval_left_open_right_close(a, b)
     - [a, b) -> Interval_left_close_right_open(a, b)
     - [a, b] -> Interval_left_close_right_close(a, b)
     - {a, b} -> set(a, b)
    Call before `auto_symbol`.
    """
    MAPPING = {
        # ('(', ')'): 'tuple', # it seems that we need to treat parentheses more carefully
                               # TODO: parse tuples to sympy objects. is it necessary?
        ('(', ']'): 'Interval_left_open_right_close',
        ('[', ')'): 'Interval_left_close_right_open',
        ('[', ']'): 'Interval_left_close_right_close',
        ('{', '}'): 'set', # it is different from python set. just parsed as a function name.
    }
    # TODO: here we do not consider the number of the arguments. should we make more constraints?

    result = []
    stack = []

    for tokNum, tokVal in tokens:
        if tokNum == OP:
            name = tokVal

            if name in '([{':
                stack.append((name, len(result)))
            elif name in ')]}':
                l_name, l_idx = stack.pop()
                func_name = MAPPING.get((l_name, name), None)

                if func_name:
                    result[l_idx] = (OP, '(')
                    result.insert(l_idx, (NAME, func_name))
                    tokVal = ')'
        
        result.append((tokNum, tokVal))

    return result


custom_transformations = (auto_interval, auto_symbol, repeated_decimals, auto_number, 
        factorial_notation, convert_equals_signs)

## ===== Parse sentences =====

def parse_al(s, local_dict = None):
    """
    Parse an Assertional Logic expression string into a valid
    sympy expression. It also does partial simplification.
    In addition you can use alternative spellings of these operators:
      'x ==> y'   parses as   (x >> y)    # Implication
      'x <== y'   parses as   (x << y)    # Reverse implication
    >>> s = '(1+x=2)=True'
    >>> parse_al(s)
    Eq(x + 1, 2)
    """
    if local_dict is None: local_dict = dict()
    ## Replace the alternative spellings of operators with canonical spellings
    s = s.replace('==>', '>>').replace('<==', '<<')
    s = s.replace('^', '**')
    ## TODO: Remove '=True' to temporarily solve some problem.
    ##       Need further modify the set parsing method and utils to fully solve
    ##       this problem.
    s = re.sub(r'=\s*True', '', s)
    ## Replace keywords
    s = re.sub(r'lambda', 'lbd_', s)
    ## TODO: Replace special variables. This might be a hack?
    s = re.sub(r'(?:([a-zA-Z])(?:_\{(\d+)\}))', r'\1_\2', s)
    ## Detect type definition. Return a list of variables for type definition.
    def_rule = re.compile(r'^\s*(\w+\s*(,\s*\w+\s*)*):\s*(\w+)\s*$')
    if re.match(def_rule, s):
        tp = re.match(def_rule, s).group(3)
        vs = [item.strip() for item in re.match(def_rule, s).group(1).split(',')]
        for v in vs:
            if v in local_dict: warnings.warn("parse_al(): Repeatively declare variable %s. "
                                              "Original variable will be overrided." % v)
            tmp_v = TypeSymbol(v, type=tp)
            local_dict[v] = tmp_v
        return [local_dict[v] for v in vs]
    ## Now eval the string.  (A security hole; do not use with an adversary.)
    return parse_expr(s, transformations=custom_transformations,
            local_dict={**_default_local_dict, **local_dict}, evaluate=False)


## ===== Compare sentences =====

Functions = (Function, Add, Mul, Pow, Tuple, Relational)
def get_name(sympy_object):
    """
    Get the name of the sympy object.
    """
    if hasattr(sympy_object, 'name'):
        return sympy_object.name
    elif sympy_object.is_Add:
        return 'Add'
    elif sympy_object.is_Mul:
        return 'Mul'
    elif sympy_object.is_Pow:
        return 'Pow'
    return type(sympy_object)

def has_function(sympy_object):
    """
    Return True if the object is not only composed of simple objects (has
    functions in expression). If the object is composed of simple objects,
    then we may directly compare two objects through 
    `simplify(obj1 - obj2) == 0`.
    >>> has_function(sympy.parse_expr("x**2 + y**2 / b**2"))
    False
    >>> has_function(sympy.parse_expr("Coordinate(P)"))
    True
    """
    if isinstance(sympy_object, (Symbol, Number, NumberSymbol)):
        return False
    elif isinstance(sympy_object, (Function, Tuple, Relational)):
        return True
    else:
        return any([has_function(arg) for arg in sympy_object.args])

def cmp_sentence(sent1, sent2):
    """
    Recursively compare two sentences. Return True if they are the same, False otherwise.
    """

    def _cmp_sentence(sent1, sent2):
        if isinstance(sent1, Number) or isinstance(sent2, Number):
            return sent1.simplify() == sent2.simplify()
        if isinstance(sent1, NumberSymbol) or isinstance(sent2, NumberSymbol):
            return sent1 == sent2
        
        if not has_function(sent1) and not has_function(sent2) and simplify(sent1 - sent2) == 0:
            return True
        
        if isinstance(sent1, (Symbol, *Functions)) and not isinstance(sent2, (Symbol, *Functions)) or \
            isinstance(sent2, (Symbol, *Functions)) and not isinstance(sent1, (Symbol, *Functions)):
            return False
        
        assert isinstance(sent1, (Symbol, *Functions))
        assert isinstance(sent2, (Symbol, *Functions))
        if isinstance(sent1, Symbol) and isinstance(sent2, Symbol):
            if isinstance(sent1, TypeSymbol) and isinstance(sent2, TypeSymbol):
                return get_name(sent1) == get_name(sent2) and sent1.type == sent2.type
            elif not isinstance(sent1, TypeSymbol) and not isinstance(sent2, TypeSymbol):
                return get_name(sent1) == get_name(sent2)
        elif (isinstance(sent1, Functions) and isinstance(sent2, Functions) and
                get_name(sent1) == get_name(sent2) and len(sent1.args) == len(sent2.args)):
            if get_name(sent1) in _order_insensitive_functions:
                for permuted_arg1 in itertools.permutations(sent1.args):
                    if all([_cmp_sentence(arg1, arg2) for arg1, arg2 in zip(permuted_arg1, sent2.args)]):
                        return True
            else:
                return all([_cmp_sentence(arg1, arg2) for arg1, arg2 in zip(sent1.args, sent2.args)])
    
    try: # a big escaper to handle annoying seq2seq output.
        if sent1.free_symbols == sent2.free_symbols: # a quick check to accelerate
            return _cmp_sentence(sent1, sent2)
    except KeyboardInterrupt: # raise keyboard interrupt
        raise
    except:
        pass

    return False


## ===== Compare annotations =====

def parse_annotation(annotation: str):
    """
    Parse an annotation. It will
     - filter out invalid sentences
     - parse the annotations to sympy objects
     - establish the line number alignment
    :return parse: a 3-element tuple of variables, facts and queries, each element is a list of sympy objects.
    :return filtered_annotation: a list of valid sentences.
    :return alignment: a dict mapping sympy objects to line numbers.
    """

    def register(s: str, filtered: List[str]) -> int:
        """register the sentence and get the line number."""
        lineno = len(filtered)
        filtered.append(s)
        return lineno
    
    vars, facts, queries = [], [], []
    local_dict = OrderedDict() # Ensure the same result to the same input

    alignment = {'vars': {}, 'facts': {}, 'queries': {}} # <sympy_object: lineno>
    filtered: List[str] = [] # filtered annotations, list of str

    pattern = re.compile(r'\[\[\d+\]\]')
    has_escape = lambda s: re.search(pattern, s)

    for sentence in annotation.split('\n'):
        sentence = sentence.strip()
        if not sentence: continue

        try: # escape parse errors
            if ':' in sentence and not has_escape(sentence): # declaration
                vs = parse_al(sentence, local_dict=local_dict)
                lineno = register(sentence, filtered)
                for v in vs:
                    alignment['vars'][v] = lineno
        except Exception:
            pass
    
    for sentence in annotation.split('\n'):
        sentence = sentence.strip()
        if not sentence or has_escape(sentence): continue

        try: # escape parse errors
            if ':' in sentence: # declaration
                pass
            elif '?' in sentence: # query
                obj = parse_al(re.sub(r'=\s*\?', '', sentence), local_dict=local_dict)
                # dummy subsititution to hack annoying end2end predictions
                for v in local_dict.values(): obj.subs(v, Symbol('S'))
                queries.append(obj)
                alignment['queries'][obj] = register(sentence, filtered)
            else: # fact
                obj = parse_al(sentence, local_dict=local_dict)
                # dummy subsititution to hack annoying end2end predictions
                for v in local_dict.values(): obj.subs(v, Symbol('S'))
                facts.append(obj)
                alignment['facts'][obj] = register(sentence, filtered)
        except Exception:
            pass
    
    vars = list(local_dict.values())
    return (vars, facts, queries), filtered, alignment


def cmp_question(
        annotation1: str, 
        annotation2: str, 
        include_dec: bool = True,
        verbose: bool = False, 
        speed_up: bool = True,
        max_workers = 0
    ):
    """
    Compare two annotations for the same question.
    Return the best variable alignments of the question, along with the cleaned annotations.
    An annotation is composed of declarations, facts and queries. Sentences are seperated by newline charaters. E.g.
        C, D: Curve
        Expression(D) = ( (x - 2)*(x - 1) + (y - 4)*(y - 3) = 0 )
        NumIntersection(C, D) = ?
    The annotation should be passed in as a string with several line of sentences.
    :param annotation1: The 1st annotation.
    :param annotation2: The 2nd annotation.
    :param include_dec: Include the declaration sentences in evaluation.
    :param verbose: Show the progress bar.
    :param speed_up: Assume single-character variables with the same name are matched. This would accelerate a lot, but may under estimate the result.
    """
    (vars1, facts1, queries1), filtered1, alignment1 = parse_annotation(annotation1)
    (vars2, facts2, queries2), filtered2, alignment2 = parse_annotation(annotation2)

    def get_align_tuples(obj1, obj2, category='vars'):
        """
        Input two objects (in two annotations), return a tuple of alignment tuples.
        """
        nonlocal alignment1, alignment2
        lineno1 = alignment1[category].get(obj1, -1)
        lineno2 = alignment2[category].get(obj2, -1)
        if lineno1 != -1 and lineno2 != -1:
            return (lineno1, lineno2)
        return None
    
    # remove common vars. we think they are the same (not necessarily), reduce accuracy but may accelerate the comparing process.
    common_vars = [v for v in vars1 if v in vars2 and len(v.name) == 1] if speed_up else []
    vars1, vars2 = [v for v in vars1 if v not in common_vars], [v for v in vars2 if v not in common_vars]
    default_alignments = [get_align_tuples(v, v) for v in common_vars]
    
    max_cnt = 0
    best_alignments = []
    dummy_vars = [Dummy() for _ in range(len(vars1))]

    iterator = get_alignments(vars1, vars2)
    if verbose:
        iterator = list(iterator)
        iterator = tqdm(iterator, total=len(iterator), leave=False, desc="Question")
    
    for aligned_vars1, aligned_vars2 in iterator:
        cur_alignments = []
        
        # substitute the variables according to the alignment, then
        # count the common sentences.
        sub_facts1, sub_facts2 = [], [] # facts
        for sent1 in facts1:
            for tgt, src1 in zip(dummy_vars, aligned_vars1):
                sent1 = sent1.subs(src1, tgt)
            sub_facts1.append(sent1)
        for sent2 in facts2:
            for tgt, src2 in zip(dummy_vars, aligned_vars2):
                sent2 = sent2.subs(src2, tgt)
            sub_facts2.append(sent2)
        sub_idxs2 = [i for i in range(len(facts2))]
        for idx1 in range(len(facts1)):
            for idx2 in sub_idxs2[:]:
                if cmp_sentence(sub_facts1[idx1], sub_facts2[idx2]):
                    cur_alignments.append(get_align_tuples(facts1[idx1], facts2[idx2], 'facts'))
                    sub_idxs2.remove(idx2)
                    break
        
        sub_queries1, sub_queries2 = [], [] # queries
        for sent1 in queries1:
            for tgt, src1 in zip(dummy_vars, aligned_vars1):
                sent1 = sent1.subs(src1, tgt)
            sub_queries1.append(sent1)
        for sent2 in queries2:
            for tgt, src2 in zip(dummy_vars, aligned_vars2):
                sent2 = sent2.subs(src2, tgt)
            sub_queries2.append(sent2)
        sub_idxs2 = [i for i in range(len(queries2))]
        for idx1 in range(len(queries1)):
            for idx2 in sub_idxs2[:]:
                if cmp_sentence(sub_queries1[idx1], sub_queries2[idx2]):
                    cur_alignments.append(get_align_tuples(queries1[idx1], queries2[idx2], 'queries'))
                    sub_idxs2.remove(idx2)
                    break
        
        if include_dec: # variables
            for src1, src2 in zip(aligned_vars1, aligned_vars2):
                if src1.type == src2.type:
                    cur_alignments.append(get_align_tuples(src1, src2))

        cnt = len(cur_alignments)
        if cnt > max_cnt:
            best_alignments = [cur_alignments]
        elif cnt == max_cnt:
            best_alignments.append(cur_alignments)
        max_cnt = max(max_cnt, cnt)

    if include_dec:
        max_cnt += len(common_vars)
        best_alignments = [default_alignments + align for align in best_alignments]

    return max_cnt, best_alignments, (filtered1, filtered2)
    
def get_alignments(vars1, vars2):
    """
    Get the alignments based on the variable type.
    """

    # divide into groups based on type.
    groups = [] # Elements: (type, vars1, vars2)

    types = {str(v.type) for v in vars1 + vars2}
    for tp in types:
        group = [str(tp), [v for v in vars1 if str(v.type) == tp], [v for v in vars2 if str(v.type) == tp]]
        groups.append(group)

    # get permute iter for each type
    permute_iterators = []
    for tp, vs1, vs2 in groups:
        if len(vs1) < len(vs2):
            it = zip(itertools.repeat(vs1), itertools.permutations(vs2, r=len(vs1)))
        else:
            it = zip(itertools.permutations(vs1, r=len(vs2)), itertools.repeat(vs2))
        permute_iterators.append(it)
    
    for aligns in itertools.product(*permute_iterators):
        yield [item for x, y in aligns for item in x], [item for x, y in aligns for item in y]