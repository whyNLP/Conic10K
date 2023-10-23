"""
A parallel patch for `cmp_question` in evaluate.py
"""

from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor as Pool

from sympy import Dummy

from .evaluate import parse_annotation, cmp_sentence, get_alignments
from .evaluate import cmp_question as cmp_question_naive

def get_align_tuples(obj1, obj2, alignments, category='vars'):
    """
    Input two objects (in two annotations), return a tuple of alignment tuples.
    """
    alignment1, alignment2 = alignments
    lineno1 = alignment1[category].get(obj1, -1)
    lineno2 = alignment2[category].get(obj2, -1)
    if lineno1 != -1 and lineno2 != -1:
        return (lineno1, lineno2)
    
    raise ValueError(f"'{obj1}: {obj1.type}' or '{obj2}: {obj2.type}' is not found in alignemnts.")


def each(aligned_vars, env_pack, reconstruct: bool = False):
    """
    Each worker evaluates an alignment.
    """

    if reconstruct:
        # redundnat work, but necessary for multiprocessing pickling
        aligned_vars1, aligned_vars2 = aligned_vars
        annotation1, annotation2, include_dec = env_pack
        (vars1, facts1, queries1), _, alignment1 = parse_annotation(annotation1)
        (vars2, facts2, queries2), _, alignment2 = parse_annotation(annotation2)
        dummy_vars = [Dummy() for _ in range(len(vars1))]
        aligned_vars1, aligned_vars2 = [vars1[idx] for idx in aligned_vars1], [vars2[idx] for idx in aligned_vars2]
        aligns = (alignment1, alignment2)
    else:
        aligned_vars1, aligned_vars2 = aligned_vars
        dummy_vars, facts1, queries1, facts2, queries2, aligns, include_dec = env_pack

    alignments = []
    
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
                alignments.append(get_align_tuples(facts1[idx1], facts2[idx2], aligns, 'facts'))
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
                alignments.append(get_align_tuples(queries1[idx1], queries2[idx2], aligns, 'queries'))
                sub_idxs2.remove(idx2)
                break
    
    if include_dec: # variables
        for src1, src2 in zip(aligned_vars1, aligned_vars2):
            assert src1.type == src2.type
            alignments.append(get_align_tuples(src1, src2, aligns, 'vars'))

    return alignments

def cmp_question(
        annotation1: str,
        annotation2: str,
        include_dec: bool = True,
        verbose: bool = False,
        accuracy_only = False,
        max_workers: int = 8,
        speed_up: bool = True
    ):
    """
    Parallel version for comparing two annotations for the same question. Maybe have to conduct redundant work to enable parallelism.
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
    :param max_workers: Maximum number of workers in parallel to accelerate. If None, use cpu_count in the tasks.
    :param speed_up: Assume single-character variables with the same name are matched. This would accelerate a lot, but may under estimate the result.
    """
    # Call the serial implementation to avoid redundant work.


    
    (vars1, facts1, queries1), filtered1, alignment1 = parse_annotation(annotation1)
    (vars2, facts2, queries2), filtered2, alignment2 = parse_annotation(annotation2)
    aligns = (alignment1, alignment2)
    
    if accuracy_only:
        if len(facts1) != len(facts2) or len(queries1) != len(queries2):
            return 0, 0, 0
    
    if max_workers == 1:
        return cmp_question_naive(annotation1=annotation1, annotation2=annotation2, include_dec=include_dec, verbose=verbose, speed_up=speed_up)
    
    # remove common vars. we think they are the same (not necessarily), reduce accuracy but may accelerate the comparing process.
    common_vars = [v for v in vars1 if v in vars2 and len(v.name) == 1] if speed_up else []
    vars1_, vars2_ = [v for v in vars1 if v not in common_vars], [v for v in vars2 if v not in common_vars]
    default_alignments = [get_align_tuples(v, v, aligns) for v in common_vars]
    
    # Deal with multiprocessing
    iterator = get_alignments(vars1_, vars2_)
    iterator = list(iterator)
    possible_alignments = []

    if len(iterator) <= 4: # overhead may cost too much, use single process
        dummy_vars = [Dummy() for _ in range(len(vars1_))]
        env_pack = dummy_vars, facts1, queries1, facts2, queries2, aligns, include_dec
        if verbose:
            iterator = tqdm(iterator, total=len(iterator), leave=False, desc="Question")
        for align in iterator:
            possible_alignments.append(each(align, env_pack, False))
    else:
        pool = Pool(max_workers=max_workers)
        iterator = [([vars1.index(v) for v in align1], [vars2.index(v) for v in align2]) for align1, align2 in iterator] # convert to picklable instances
        env_pack = annotation1, annotation2, include_dec
        futures = [pool.submit(each, align, env_pack, True) for align in iterator]

        if verbose:
            with tqdm(total=len(futures), leave=False, desc="Question") as t:
                for future in futures:
                    future.add_done_callback(lambda x: t.update())
                for future in futures:
                    possible_alignments.append(future.result())
        else:
            for future in futures:
                possible_alignments.append(future.result())
        
    max_cnt = max(map(lambda x: len(x), possible_alignments))
    best_alignments = [align for align in possible_alignments if len(align) == max_cnt]

    if include_dec:
        max_cnt += len(common_vars)
        best_alignments = [default_alignments + align for align in best_alignments]

    return max_cnt, best_alignments, (filtered1, filtered2)
