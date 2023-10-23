import datasets
import evaluate
from metric.metric import Metric

class ExprExactMatch(evaluate.Metric):
    def _info(self):
        return evaluate.MetricInfo(
            description='',
            citation='',
            inputs_description='',
            features=datasets.Features(
                {
                    "predictions": datasets.Value("string", id="sequence"),
                    "references": datasets.Value("string", id="sequence"),
                }
            ),
            reference_urls=[],
        )


    def _compute(self, predictions, references, correct_only=False):
        """
        Compute the exact match between two annotations.
        """

        predictions = [s.replace(';', '\n') for s in predictions]
        references = [s.replace(';', '\n') for s in references]

        mtc = Metric(max_workers=1)
        mtc.cmps(predictions, references, verbose=False)
     
        return {
            "acc": mtc.accuracy,
        }