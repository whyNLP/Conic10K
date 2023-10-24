import json
from argparse import ArgumentParser
from data import get_dataset
from metric.metric import Metric


parser = ArgumentParser()
parser.add_argument('--dataset_path', default='conic10k', type=str)
parser.add_argument('--prediction_file', type=str)
parser.add_argument('--split', default='test', type=str)
parser.add_argument('--report_file', default='', type=str)

if __name__ == '__main__':
    args = parser.parse_args()

    task = args.prediction_file
    split = args.split
    report_file = args.report_file

    refs = [
        d['labels']
        for d in get_dataset(args.dataset_path, 'semantic_parsing')[split]
    ]

    preds = json.load(open(args.prediction_file))

    preds = [
        p.split('" is')[1].strip().replace('</s>', '')
        for p in preds
    ]

    mtc = Metric(max_workers=1)
    mtc.cmps(preds, refs, verbose=True)

    if report_file:
        with open(report_file, 'w') as f:
            f.write(mtc.detail())

    print(f'accuracy: {mtc.accuracy}\nmi-f1: {mtc.f1}\nma-f1: {mtc.avg_f1}')
