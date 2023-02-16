from .evaluate import cmp_question
from .metric import Metric

annotation_pairs = [
    (
        "G:Ellipse\nb:Number\na:Number\nO:Origin\nD:Point\nA:Point\nB:Point\nC:Point\nF:Point\na>b\nb>0\nExpression(G)=(y^2/b^2+x^2/a^2=1)\nEccentricity(G)=sqrt(2)/2\nPointOnCurve(Vertex(TriangleOf(A,B,C)),G)\nMidPoint(LineSegmentOf(A,B))=D\nMidPoint(LineSegmentOf(B,C))=E\nMidPoint(LineSegmentOf(A,C))=F\nk1:Number\nk2:Number\nk3:Number\nSlope(OverlappingLine(LineSegmentOf(A,B)))=k1\nSlope(OverlappingLine(LineSegmentOf(B,C)))=k2\nSlope(OverlappingLine(LineSegmentOf(A,C)))=k3\nNegation(k1*k2*k3=0)\nSlope(LineOf(O,D))+Slope(LineOf(O,F))+Slope(LineOf(O,D))=-1\n1/k2+1/k1+1/k3=?",
        "G:Ellipse\nExpression(G)=(y^2/b^2+x^2/a^2=1)\na:Number\nb:Number\na>b\nb>0\nEccentricity(G)=sqrt(2)/2\nA:Point\nB:Point\nC:Point\nPointOnCurve(Vertex(TriangleOf(A,B,C)),G)\nD:Point\nE:Point\nF:Point\nMidPoint(LineSegmentOf(A,B))=D\nMidPoint(LineSegmentOf(B,C))=E\nMidPoint(LineSegmentOf(A,C))=F\nk1:Number\nk2:Number\nk3:Number\nSlope(OverlappingLine(LineSegmentOf(A,B)))=k1\nSlope(OverlappingLine(LineSegmentOf(B,C)))=k2\nSlope(OverlappingLine(LineSegmentOf(A,C)))=k3\nNegation(k1*k2*k3=0)\nO:Origin\nSlope(LineOf(O,D))+Slope(LineOf(O,E))+Slope(LineOf(O,F))=-1\n1/k1+1/k2+1/k3=?"
    )
]

def test_cmp_question():
    a1, a2 = annotation_pairs[0]
    assert cmp_question(a1, a2) == 24

def test_metric_general_tiny(recwarn):
    with open('tests/pred.txt', 'r') as f:
        preds = f.read().split('\n')
    with open('tests/gold.txt', 'r') as f:
        golds = f.read().split('\n')

    preds = [pred.replace(';', '\n') for pred in preds][:23]
    golds = [gold.replace(';', '\n') for gold in golds][:23]
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.f1 - 0.955732645806477) < 1e-3

def test_metric_general_medium(recwarn):
    with open('tests/pred.txt', 'r') as f:
        preds = f.read().split('\n')
    with open('tests/gold.txt', 'r') as f:
        golds = f.read().split('\n')

    preds = [pred.replace(';', '\n') for pred in preds][:107]
    golds = [gold.replace(';', '\n') for gold in golds][:107]
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.f1 - 0.9637181486584114) < 1e-3

def test_metric_general_large(recwarn):
    with open('tests/pred.txt', 'r') as f:
        preds = f.read().split('\n')
    with open('tests/gold.txt', 'r') as f:
        golds = f.read().split('\n')

    preds = [pred.replace(';', '\n') for pred in preds]
    golds = [gold.replace(';', '\n') for gold in golds]
    
    mtc = Metric()
    mtc.cmps(preds, golds)

    assert abs(mtc.f1 - 0.9482032003728795) < 1e-3