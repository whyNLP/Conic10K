import pytest

from .evaluate import parse_al, cmp_question
from .metric import Metric
from .utils import diff, filter_annotation

@pytest.fixture()
def data():
    with open('tests/pred.txt', 'r') as f:
        preds = f.read().split('\n')
    with open('tests/gold.txt', 'r') as f:
        golds = f.read().split('\n')

    preds = [pred.replace(';', '\n') for pred in preds]
    golds = [gold.replace(';', '\n') for gold in golds]

    return (preds, golds)


def test_parse_lambda():
    assert str(parse_al('lambda')) == 'lbd_'
    assert str(parse_al('z=lambda+1')) == 'Eq(z, lbd_ + 1)'
    assert str(parse_al('lambda=t')) == 'Eq(lbd_, t)'

def test_parse_intervals():
    assert str(parse_al('Focus(C) = {F_{1}, F_{2}}')) == 'Eq(Focus(C), set(F_1, F_2))'
    assert str(parse_al('Focus(C) = {LeftFoucs(E), Focus(F)}')) == 'Eq(Focus(C), set(LeftFoucs(E), Focus(F)))'
    assert str(parse_al('Range(h) = [1, 2]')) == 'Eq(Range(h), Interval_left_close_right_close(1, 2))'
    assert str(parse_al('Range(h) = (1, a+k*(1+x)]')) == 'Eq(Range(h), Interval_left_open_right_close(1, a + k*(x + 1)))'
    assert str(parse_al('Range(z) = [(z+1)*t, 2+(5*x+1))')) == 'Eq(Range(z), Interval_left_close_right_open(t*(z + 1), 5*x + 1 + 2))'


def test_cmp_question(data):
    preds, golds = data
    a1, a2 = preds[4], golds[4]
    assert cmp_question(a1, a2)[0] == 24


def test_metric_general_tiny(recwarn, data):
    preds, golds = data

    preds = preds[:23]
    golds = golds[:23]
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.avg_f1 - 0.955732645806477) < 1e-4

def test_metric_general_medium(recwarn, data):
    preds, golds = data

    preds = preds[:107]
    golds = golds[:107]
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.avg_f1 - 0.9637181486584114) < 1e-4

@pytest.mark.skip(reason='Time costly test.')
def test_metric_general_large(recwarn, data):
    preds, golds = data
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.avg_f1 - 0.9482032003728795) < 1e-4


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

def test_filter(recwarn):
    """
    We do not remove the same query since it may come from the (problematic) question.
    """
    annotation = "G: Hyperbola\nH: Point\nExpression(G) = (x^2/a^2 + y^2 = 1)\nExpression(G) = (x^2/a^2+y^2=1)\nEccentricity(G) = ?\nEccentricity(G) = ?"
    filtered = filter_annotation(annotation)
    assert filtered in [
        "G: Hyperbola\nH: Point\nExpression(G) = (x^2/a^2+y^2=1)\nEccentricity(G) = ?\nEccentricity(G) = ?",
        "G: Hyperbola\nH: Point\nExpression(G) = (x^2/a^2 + y^2 = 1)\nEccentricity(G) = ?\nEccentricity(G) = ?"
    ]