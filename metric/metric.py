from typing import List, Union
from .evaluate import cmp_question, cnt_sentences, parse_annotation

from tqdm import tqdm

class Record:
    """Helper class for Metric."""
    
    __slots__ = ['pred', 'gold', 'question', 'common', 'num_gold', 'num_pred', 'correct']

    def __init__(
        self,
        pred: str,
        gold: str,
        question: str,
        common: int,
        num_gold: int,
        num_pred: int,
        correct: bool,
    ):
        self.pred = str(pred)
        self.gold = str(gold)
        self.question = str(question)
        self.common = int(common)
        self.num_gold = int(num_gold)
        self.num_pred = int(num_pred)
        self.correct = bool(correct)
    
    def __str__(self) -> str:
        detailed_record = "=== Beginning of Record ===\n\n"

        detailed_record += "Question:\n"
        detailed_record += self.question

        detailed_record += "\n\nGold Annotation:\n"
        detailed_record += self.gold

        detailed_record += "\n\nPredicted Annotation:\n"
        detailed_record += self.pred

        detailed_record += "\n\nComparasion Result:\n"
        detailed_record += f"Common: {self.common}\n"
        detailed_record += f"Gold Sentences: {self.num_gold}\n"
        detailed_record += f"Predicted Sentences: {self.num_pred}\n"
        detailed_record += f"Correct: {self.correct}\n\n"

        detailed_record += "=== End of Record ===\n"
        return detailed_record

class Metric:
    """
    The evaluation metric toolkit for L annotations.
    Use `Metric.cmp` or `Metric.cmps` to compare annotations, and print the `Metric` object to show the report.
    
    >>> mtc = Metric()
    >>> question = "长为2的线段$AB$的两个端点在抛物线$y^{2}=x$上滑动,则线段$AB$中点$N$到$y$轴距离的最小值是?"
    >>> gold = "A, B: Point\\nLength(LineSegmentOf(A, B)) = 2\\nParabola_1: Parabola\\nExpression(Parabola_1) = (y^2=x)\\nPointOnCurve(A, Parabola_1)\\nPointOnCurve(B, Parabola_1)\\nM: Point\\nMidPoint(LineSegmentOf(A, B)) = M\\nMin(Distance(M, yAxis)) = ?\\n"
    >>> pred = "A: Point\\nB: Point\\nC: Parabola\\nN: Point\\nExpression(C) = ( y^2 = x )\\nMidPoint(LineSegmentOf(A, B)) = N\\nMin(Distance(N, yAxis)) = ?"
    >>> mtc.cmp(pred, gold, question, verbose = False)
    >>> round(mtc.f1, 4)
    0.8235
    >>> print(mtc) # show the report  # doctest: +SKIP
    ...
    """
    def __init__(self, include_dec: bool = True):
        """
        The evaluation metric toolkit for L annotations.
        :param include_dec: include the declaration sentences in evaluation.
        """
        self.include_dec: bool = include_dec

        ## Records
        self.records: List[Record] = []

        ## Statistics
        self.t_questions = 0
        self.t_common = 0
        self.t_gold = 0
        self.t_pred = 0
        self.t_correct = 0
        self.precs = []
        self.recalls = []
        self.f1s = []
    
    def cmps(self, preds: List[str], golds: List[str], questions: List[str] = None, verbose: bool = True):
        """
        Compare a batch of annotations.
        The length of the input lists must be the same.

        :param preds: The predicted annotations.
        :param golds: The gold annotations.
        :param questions: (optional) The question texts.
        :param verbose: Show the progress bar.
        """
        if questions is None:
            questions = [None] * len(preds)
        assert len(preds) == len(golds) == len(questions), "The length of the input lists must be the same."
        
        iterator = zip(preds, golds, questions)
        if verbose:
            iterator = tqdm(iterator, desc="Dataset")
        
        for p, g, q in iterator:
            self.cmp(p, g, q, verbose=verbose)

    def cmp(self, pred: str, gold: str, question: str = None, verbose: bool = True):
        """
        Compare two annotations for the same question.

        An annotation is composed of declarations, facts and queries. E.g.
            D: Curve
            Expression(D) = ( (x - 2)*(x - 1) + (y - 4)*(y - 3) = 0 )
            NumIntersection(C, D) = ?
        The annotation should be passed in as a string with several line of sentences.

        :param pred: The predicted annotation.
        :param gold: The gold annotation.
        :param question: (optional) The question text.
        :param verbose: Show the progress bar.
        """
        common = cmp_question(gold, pred, include_dec=self.include_dec, verbose=verbose)
        num_gold = cnt_sentences(gold, include_dec=self.include_dec)
        num_pred = cnt_sentences(pred, include_dec=self.include_dec)
        correct = 1 if common == num_gold == num_pred else 0

        self.records.append(Record(pred, gold, question, common, num_gold, num_pred, correct))

        self.t_common += common
        self.t_gold += num_gold
        self.t_pred += num_pred
        self.t_correct += correct
        self.t_questions += 1

        prec = (common / num_pred) if num_pred else 0
        recall = (common / num_gold) if num_gold else 1
        f1 = ((2 * prec * recall) / (prec + recall)) if (prec + recall) else 0
        self.precs.append(prec)
        self.recalls.append(recall)
        self.f1s.append(f1)
    
    def detail(self):
        """
        Print out a report for current metric.
        """
        # TODO: is 0 precision correct.
        detailed_report = "=== Beginning of Report ===\n\n"

        detailed_report += "Main metric: {:.2%}\n\n".format(self.f1)

        detailed_report += "Overview:\n    "\
        f"Total sample questions: {self.t_questions}\n    "\
        f"Total correct questions: {self.t_correct}\n    "\
        f"Total gold sentences: {self.t_gold}\n    "\
        f"Total pred sentences: {self.t_pred}\n    "\
        f"Total common sentences: {self.t_common}\n\n"

        detailed_report += "Sentece Level (Total):\n    "
        prec = self.t_common / self.t_pred if self.t_pred else 0
        recall = self.t_common / self.t_gold if self.t_gold else 1
        f1 = (2 * prec * recall) / (prec + recall) if (prec + recall) else 0
        detailed_report += "Precision: {:.2%}, Recall: {:.2%}, F1: {:.2%}\n\n".format(prec, recall, f1)

        detailed_report += "Sentece Level (Question Average):\n    "
        avg_prec = sum(self.precs) / len(self.precs) if len(self.precs) else 0
        avg_recall = sum(self.recalls) / len(self.recalls) if len(self.recalls) else 1
        avg_f1 = sum(self.f1s) / len(self.f1s) if len(self.f1s) else 0
        detailed_report += "Precision: {:.2%}, Recall: {:.2%}, F1: {:.2%}\n\n".format(avg_prec, avg_recall, avg_f1)

        detailed_report += "Question Level:\n    "
        acc = self.t_correct / self.t_questions if self.t_questions else 0
        detailed_report += "Accuracy: {:.2%}\n\n".format(acc)

        detailed_report += "=== End of Report ===\n"

        return detailed_report

    def __len__(self):
        return len(self.records)
    
    def __getitem__(self, idx):
        return self.records[idx]

    def __str__(self) -> str:
        return self.detail()
    
    @property
    def f1(self):
        """This is the main metric."""
        return sum(self.f1s) / len(self.f1s) if len(self.f1s) else 0