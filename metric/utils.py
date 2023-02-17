import re
from typing import List, Tuple
from sympy import Symbol, Dummy
from tqdm import tqdm

from .evaluate import parse_al, cmp_sentence, get_alignments


## ===== Algorithm for diff ======

def parse_and_align_annotation(annotation: str):
    """
    Similar to parse_annotation, but it will
     - filter out invalid sentences
     - parse the annotations to sympy objects
     + establish the line number alignment

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


def align_question(
        annotation1: str, 
        annotation2: str, 
        include_dec: bool = True,
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
    :param include_dec: Include the declaration sentences in evaluation.
    :param verbose: Show the progress bar.
    :param speedup: Assume single-character variables with the same name are matched. This would accelerate a lot, but may under estimate the result.
    """
    (vars1, facts1, queries1), filtered1, alignment1 = parse_and_align_annotation(annotation1)
    (vars2, facts2, queries2), filtered2, alignment2 = parse_and_align_annotation(annotation2)

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
    common_vars = [v for v in vars1 if v in vars2 and len(v.name) == 1] if speedup else []
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


def align2diff(
        best_alignments: List[List[Tuple[int, int]]], 
        filtered: Tuple[List[str], List[str]]
    ) -> str:
    """
    Generate a diff log for two annotations, based on the return value
    from `align_question`. Return a human-readable diff string.

    Only pick the first element in `best_alignment`.
    """
    assert len(best_alignments) > 0, "Empty alignment in diff!"

    filtered1, filtered2 = filtered
    idx1, idx2 = map(lambda x: list(range(len(x))), filtered)

    alignment = best_alignments[0]
    for align1, align2 in alignment:
        if align1 in idx1: idx1.remove(align1)
        if align2 in idx2: idx2.remove(align2)

    diff_string = ""
    if idx1 and idx2:
        diff_string += '\n'.join(f"< {s}" for s in map(lambda x: filtered1[x], idx1))
        diff_string += '\n---\n'
        diff_string += '\n'.join(f"> {s}" for s in map(lambda x: filtered2[x], idx2))
    elif idx1:
        diff_string += '\n'.join(f"< {s}" for s in map(lambda x: filtered1[x], idx1))
    elif idx2:
        diff_string += '\n'.join(f"> {s}" for s in map(lambda x: filtered2[x], idx2))

    return diff_string


## ===== Easy-to-access functions =====

def filter_annotation(annotation: str) -> str:
    """
    Filter out invalid sentences in an annotation. Usually embedded
    after the model predictions.
    """
    _, filtered, _ = parse_and_align_annotation(annotation)
    return '\n'.join(filtered) if filtered else ''

def diff(
        annotation1: str, 
        annotation2: str, 
        include_dec: bool = True,
        verbose: bool = False, 
        speedup: bool = True
    ) -> str:
    """
    Generate a diff log for two annotations. Return a human-readable diff string.
    """
    _, aligns, filtered = align_question(annotation1, annotation2, include_dec, verbose, speedup)
    diff_log: str = align2diff(aligns, filtered)
    return diff_log