import re
from typing import List
from sympy import Symbol

from .evaluate import parse_al, gen_variable, get_alignments

def filter_annotation(annotation: str):
    """
    Similar to parse_annotation, but it will
     - filter out invalid sentences
     - parse the annotations to sympy objects
     - establish the line number alignment

    :return parse: a 3-element tuple that is the same as the output of 
        `parse_annotation`.
    :return filtered_annotation: a list of valid sentences.
    :return alignment: a dict mapping sympy objects to line numbers.
    """

    def register(s: str, filtered: List[str]) -> int:
        """register the sentence and get the line number."""
        lineno = len(filtered)
        filtered.append(s)
        return lineno
    
    vars, facts, queries = [], [], []
    local_dict = {}

    alignment = {} # <sympy_object: lineno>
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
                    alignment[v] = lineno
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
                alignment[obj] = register(sentence, filtered)
            else: # fact
                obj = parse_al(sentence, local_dict=local_dict)
                # dummy subsititution to hack annoying end2end predictions
                for v in local_dict.values(): obj.subs(v, Symbol('S'))
                facts.append(obj)
                alignment[obj] = register(sentence, filtered)
        except Exception:
            pass
    
    vars = list(local_dict.values())
    return (vars, facts, queries), filtered, alignment


def align_question(
        annotation1: str, 
        annotation2: str, 
        verbose: bool = False, 
        speedup: bool = True
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
    :param verbose: Show the progress bar.
    :param speedup: Assume single-character variables with the same name are matched. This would accelerate a lot, but may under estimate the result.
    """
    (vars1, facts1, queries1), filtered1, alignment1 = filter_annotation(annotation1)
    (vars2, facts2, queries2), filtered2, alignment2 = filter_annotation(annotation2)
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