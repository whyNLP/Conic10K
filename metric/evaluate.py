import re, warnings, itertools
from tqdm import tqdm

from sympy.parsing.sympy_parser import (parse_expr,\
     standard_transformations, convert_equals_signs,\
     lambda_notation, repeated_decimals, auto_number,\
     factorial_notation)
from sympy import Symbol, Function
from sympy.simplify.simplify import simplify
from sympy.core import Add, Mul, Pow, Number, Tuple
from sympy.core.relational import Relational
from sympy.core.numbers import NumberSymbol
from sympy.core.basic import Basic

from tokenize import (NAME, OP)
from keyword import iskeyword

__all__ = ['parse_annotation', 'cmp_question', 'cnt_sentences']


# ===== Helper objects for sympy =====

class TypeSymbol(Symbol):
    """
    A decorator for Symbol to allow additional information. We have to define
    a new class since Symbol uses `__slots__` to save memory.
    """
    def __init__(self, *args, **kwargs):
        Symbol.__init__(*args, **kwargs)
        if 'type' in kwargs:
            self.type = kwargs['type']

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
    'Eq', 'set', 'Distance', 'DotProduct', 'InterReciprocal', 'Intersection', 'LineOf', 'LineSegmentOf', 'NumIntersection', 'TangencyPoint', 'TriangleOf', 'Add', 'Mul', 'IsIntersect', 'IsParallel', 'IsPerpendicular', 'IsSeparated', 'IsTangent', 'IsOutTangent', 'IsInTangent', 'FootPoint'
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
                or iskeyword(name)
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

standard_transformations = (lambda_notation, auto_symbol, repeated_decimals, auto_number,
    factorial_notation)


## ===== Parse sentences =====

def parse_al(s, local_dict = None):
    """
    Parse an Assertional Logic expression string into a valid
    sympy expression. It also does simplification.

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
    ## Detect type definition. Return None for type definition.
    def_rule = re.compile(r'^\s*(\w+\s*(,\s*\w+\s*)*):\s*(\w+)\s*$')
    if re.match(def_rule, s):
        tp = re.match(def_rule, s).group(3)
        vs = [item.strip() for item in re.match(def_rule, s).group(1).split(',')]
        for v in vs:
            if v in local_dict: warnings.warn("parse_al(): Repeatively declare variable %s. "
                                              "Original variable will be overrided." % v)
            tmp_v = TypeSymbol(v+'_WITH_TYPE_'+tp, type=parse_al(tp))
            local_dict[v] = tmp_v
        return None
    ## Deal with enumerate sets
    s = re.sub(r'\{(.*)\}', r'set(\1)', s)
    ## Now eval the string.  (A security hole; do not use with an adversary.)
    return parse_expr(s, transformations=(
            standard_transformations + (convert_equals_signs,)),
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

    try: # a big escaper to handle annoying seq2seq output.

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
                    if all([cmp_sentence(arg1, arg2) for arg1, arg2 in zip(permuted_arg1, sent2.args)]):
                        return True
            else:
                return all([cmp_sentence(arg1, arg2) for arg1, arg2 in zip(sent1.args, sent2.args)])
    
    except:

        pass

    return False


## ===== Compare annotations =====

def parse_annotation(annotation):
    """
    Parse the annotations to sympy objects, ignoring the invalid sentences. Return a tuple of variables, facts
    and queries.
    """
    facts, queries = [], []
    local_dict = {}

    pattern = re.compile(r'\[\[\d+\]\]')
    has_escape = lambda s: re.search(pattern, s)

    for sentence in annotation.split('\n'):
        sentence = sentence.strip()
        if not sentence: continue

        try: # escape parse errors
            if ':' in sentence and not has_escape(sentence): # declaration
                parse_al(sentence, local_dict=local_dict)
        except Exception:
            pass
    
    for sentence in annotation.split('\n'):
        sentence = sentence.strip()
        if not sentence or has_escape(sentence): continue

        try: # escape parse errors
            if ':' in sentence: # declaration
                pass
            elif '?' in sentence: # query
                sentence = re.sub(r'=\s*\?', '', sentence)
                obj = parse_al(sentence, local_dict=local_dict)
                # dummy subsititution to hack annoying end2end predictions
                for v in local_dict.values(): obj.subs(v, Symbol('S'))
                queries.append(obj)
            else: # fact
                obj = parse_al(sentence, local_dict=local_dict)
                # dummy subsititution to hack annoying end2end predictions
                for v in local_dict.values(): obj.subs(v, Symbol('S'))
                facts.append(obj)
        except Exception:
            pass
    
    vars = list(local_dict.values())
    return vars, facts, queries

def gen_variable():
    """Create a new dummy variable."""
    return Symbol('_DUMMY_' + str(gen_variable.counter.__next__()) + '_')
gen_variable.counter = itertools.count()

def cmp_question(
        annotation1: str, 
        annotation2: str, 
        include_dec: bool = True,
        verbose: bool = False, 
        speedup: bool = True
    ):
    """
    Compare two annotations for the same question.
    Return # of common sentences. By default include the declaration sentences.

    An annotation is composed of declarations, facts and queries. Sentences are seperated by newline charaters. E.g.
        C, D: Curve
        Expression(D) = ( (x - 2)*(x - 1) + (y - 4)*(y - 3) = 0 )
        NumIntersection(C, D) = ?
    The annotation should be passed in as a string with several line of sentences.

    :param annotation1: The 1st annotation.
    :param annotation2: The 2nd annotation.
    :param include_dec: Include the declaration sentences in evaluation.
    :param verbose: Show the progress bar.
    :param speedup: Assume single-character variables with the same name are matched. This would accelerate a lot, but may under estimate the result.
    """
    vars1, facts1, queries1 = parse_annotation(annotation1)
    vars2, facts2, queries2 = parse_annotation(annotation2)
    # remove common vars. we think they are the same (not necessarily), reduce accuracy but may accelerate the comparing process.
    common_vars = [v for v in vars1 if v in vars2 and len(v.name.split('_WITH_TYPE_')[0]) == 1] if speedup else []
    vars1, vars2 = [v for v in vars1 if v not in common_vars], [v for v in vars2 if v not in common_vars]
    
    max_cnt = 0
    dummy_vars = [gen_variable() for _ in range(len(vars1))]

    iterator = get_alignments(vars1, vars2)
    if verbose:
        iterator = list(iterator)
        iterator = tqdm(iterator, total=len(iterator), leave=False, desc="Question")
    
    for aligned_vars1, aligned_vars2 in iterator:
        cnt = 0
        
        # substitute the variables according to the alignment, then
        # count the common sentences.
        sub_fqs1, sub_fqs2 = [], []
        for sent1 in facts1 + queries1:
            for tgt, src1 in zip(dummy_vars, aligned_vars1):
                sent1 = sent1.subs(src1, tgt)
            sub_fqs1.append(sent1)
        for sent2 in facts2 + queries2:
            for tgt, src2 in zip(dummy_vars, aligned_vars2):
                sent2 = sent2.subs(src2, tgt)
            sub_fqs2.append(sent2)
        for sent1 in sub_fqs1:
            for sent2 in sub_fqs2[:]:
                if cmp_sentence(sent1, sent2):
                    cnt += 1
                    sub_fqs2.remove(sent2)
                    break
        
        if include_dec:
            for src1, src2 in zip(aligned_vars1, aligned_vars2):
                if src1.type == src2.type:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)

    if include_dec:
        max_cnt += len(common_vars)

    return max_cnt

def cnt_sentences(annotation, include_dec = True):
    """
    Count the number of sentences in an annotation.
    """
    vars, facts, queries = parse_annotation(annotation)
    cnt = len(facts) + len(queries)
    if include_dec:
        cnt += len(vars)
    return cnt
    
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


# ===== Utils for other use =====
# TODO: move to other files

def filter_annotation(annotation):
    """
    Similar to parse_annotation, but used for filtering out invalid sentences.
    Usually embedded after the model predictions.
    """
    vars, facts, queries = [], [], []
    local_dict = {}

    pattern = re.compile(r'\[\[\d+\]\]')
    has_escape = lambda s: re.search(pattern, s)

    for sentence in annotation.split('\n'):
        sentence = sentence.strip()
        if not sentence: continue

        try: # escape parse errors
            if ':' in sentence and not has_escape(sentence): # declaration
                parse_al(sentence, local_dict=local_dict)
        except Exception:
            pass
    
    for sentence in annotation.split('\n'):
        sentence = sentence.strip()
        if not sentence or has_escape(sentence): continue

        try: # escape parse errors
            if ':' in sentence: # declaration
                def_rule = re.compile(r'^\s*(\w+\s*(,\s*\w+\s*)*):\s*(\w+)\s*$')
                if re.match(def_rule, sentence):
                    vars.append(sentence)
            elif '?' in sentence: # query
                obj = parse_al(re.sub(r'=\s*\?', '', sentence), local_dict=local_dict)
                # dummy subsititution to hack annoying end2end predictions
                for v in local_dict.values(): obj.subs(v, Symbol('S'))
                queries.append(sentence)
            else: # fact
                obj = parse_al(sentence, local_dict=local_dict)
                # dummy subsititution to hack annoying end2end predictions
                for v in local_dict.values(): obj.subs(v, Symbol('S'))
                facts.append(sentence)
        except Exception:
            pass
    
    return '\n'.join(vars + facts + queries)