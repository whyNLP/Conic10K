import pytest

from .evaluate import cmp_question
from .metric import Metric
from .utils import align_question, diff

@pytest.fixture()
def data():
    with open('tests/pred.txt', 'r') as f:
        preds = f.read().split('\n')
    with open('tests/gold.txt', 'r') as f:
        golds = f.read().split('\n')

    preds = [pred.replace(';', '\n') for pred in preds]
    golds = [gold.replace(';', '\n') for gold in golds]

    return (preds, golds)


def test_cmp_question(data):
    preds, golds = data
    a1, a2 = preds[4], golds[4]
    assert cmp_question(a1, a2) == 24
    assert align_question(a1, a2)[0] == 24


def test_metric_general_tiny(recwarn, data):
    preds, golds = data

    preds = preds[:23]
    golds = golds[:23]
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.avg_f1 - 0.955732645806477) < 1e-3

def test_metric_general_medium(recwarn, data):
    preds, golds = data

    preds = preds[:107]
    golds = golds[:107]
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.avg_f1 - 0.9637181486584114) < 1e-3

@pytest.mark.skip(reason='Time costly test.')
def test_metric_general_large(recwarn, data):
    preds, golds = data
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.avg_f1 - 0.9482032003728795) < 1e-3


def test_difflog(recwarn, data):
    preds, golds = data

    log4 = """< MidPoint(LineSegmentOf(B,C))=E
< Slope(LineOf(O,D))+Slope(LineOf(O,F))+Slope(LineOf(O,D))=-1
---
> E:Point
> MidPoint(LineSegmentOf(B,C))=E
> Slope(LineOf(O,D))+Slope(LineOf(O,E))+Slope(LineOf(O,F))=-1"""

    log94 = "< PointOnCurve(M,yAxis)"

    assert diff(preds[4], golds[4]) == log4
    assert diff(preds[94], golds[94]) == log94