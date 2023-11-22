# Train Set v2

这份标注样例来自一个之前构建的数据集。由于标注要求发生了细微的改动，尽管我们尽可能地修改了内容，但仍可能有些内容会与标注手册发生冲突，这些情况请以标注手册为准。这份样例中不包含span区间的标注。

## Question 1
抛物线$y^{2}=4x$的焦点为$F$,点$P(x,y)$为该抛物线上的动点,又点$A(-1,0)$,则$\frac{|PF|}{|PA|}$的取值范围是?

Fact list:
```
C: Parabola
Expression(C) = (y^2 = 4*x)
P: Point
Coordinate(P) = (x, y)
A: Point
Coordinate(A) = (-1, 0)
F: Point
Focus(C) = F
PointOnCurve(P, C) = True
```

Query list:
```
Range(Abs(LineSegmentOf(P, F))/Abs(LineSegmentOf(P, A)))
```

Answer list:
```
[sqrt(2)/2, 1]  
```


## Question 2
$P$是双曲线$\frac{x^{2}}{9}-\frac{y^{2}}{16}=1$的右支上一点,$M$、$N$分别是圆$(x+5)^{2}+y^{2}=4$和$(x-5)^{2}+y^{2}=1$上的点,则$|PM|-|PN|$的最大值等于?

Fact list:
```
C1: Hyperbola
Expression(C1) = (x^2/9 - y^2/16 = 1)
C2: Circle
Expression(C2) = ((x + 5)^2 + y^2 = 4)
C3: Circle
Expression(C3) = ((x - 5)^2 + y^2 = 1)
P: Point
PointOnCurve(P, RightPart(C1)) = True
M: Point
N: Point
PointOnCurve (M, C2) = True
PointOnCurve (N, C3) = True
```

Query list:
```
Max(Abs(LineSegmentOf(P, M)) - Abs(LineSegmentOf(P, N)))
```

Answer list:
```
9
```


## Question 3
已知抛物线$y^{2}=2px(p>0)$的焦点为$F(2,0)$,则$p$=?,过点$A(3,2)$向其准线作垂线,记与抛物线的交点为$E$,则$|EF|$=?.

Fact list:
```
C1:Parabola
p: Number
F,A,E: Point
L1,L2: Line
Expression(C1)=(y^2=2*p*x)
p>0
Focus(C1)=F
Coordinate(F)=(2,0)
Coordinate(A)=(3,2)
Directrix(C1)=L1
PointOnCurve(A,L2)=True
IsPerpendicular(L1,L2)=True 
Intersection(L2,C1)=E
```

Query list:
```
p
Abs(LineSegmentOf(E, F))
```

Answer list:
```
4
5/2
```


## Question 4
直线$x-y+2=0$与曲线$(x-1)(x-2)+(y-3)(y-4)=0$的交点个数是?

Fact list:
```
L1:Line
C1:Curve
Expression(L1)=(x-y+2=0)
Expression(C1)=((x-1)*(x-2)+(y-3)*(y-4)=0)
```

Query list:
```
NumIntersection(L1,C1)
```

Answer list:
```
2
```


## Question 5
长为$2$的线段$AB$的两个端点在抛物线$y^{2}=x$上滑动,则线段$AB$中点$M$到$y$轴距离的最小值是?

Fact list:
```
A, B: Point
Length(LineSegmentOf(A, B)) = 2
Parabola_1: Parabola
Expression(Parabola_1) = (y^2=x)
P, Q: Point
Endpoint(LineSegmentOf(A, B)) = {P, Q}
PointOnCurve(P, Parabola_1) = True
PointOnCurve(Q, Parabola_1) = True
M: Point
MidPoint(LineSegmentOf(A, B)) = M
```

Query list:
```
Min(Distance(M, yAxis))
```

Answer list:
```
3/4
```


## Question 6
双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的左、右焦点分别为$F_{1}$和$F_{2}$,左、右顶点分别为$A_{1}$和$A_{2}$,过焦点$F_{2}$与$x$轴垂直的直线和双曲线的一个交点为$P$,若$\frac{1}{2}|\overrightarrow{PA}|^{2}$是$|\overrightarrow{PA_{2}}|^{2}$和$2|\overrightarrow{A_{1}A_{2}}|^{2}$的等差中项,则该双曲线的离心率为?

Cannot annotate. Reason: 知识点不符


## Question 7
双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的左、右焦点分别为$F_{1}$和$F_{2}$,左、右顶点分别为$A_{1}$和$A_{2}$,过焦点$F_{2}$与$x$轴垂直的直线和双曲线的一个交点为$P$,若$|\overrightarrow{PA_{1}}|$是$|\overrightarrow{F_{1}F_{2}}|$和$|\overrightarrow{A_{1}F_{2}}|$的等比中项,则该双曲线的离心率为?

Cannot annotate. Reason: 知识点不符


## Question 8
设抛物线$y^{2}=8x$上一点$P$到$y$轴的距离是$4$,则点$P$到该抛物线焦点的距离是?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 8*x )
P: Point
PointOnCurve(P, C) = True
Distance(P, yAxis) = 4
```

Query list:
```
Distance(P, Focus(C))
```

Answer list:
```
6
```


## Question 9
在平面直角坐标系中,动点$P(x,y)$到两条坐标轴的距离之和等于它到点$(1,1)$的距离,记点$P$的轨迹为曲线$W$.(I)给出下列三个结论:1曲线$W$关于原点对称;2曲线$W$关于直线$y=x$对称;3曲线$W$与$x$轴非负半轴,$y$轴非负半轴围成的封闭图形的面积小于$\frac{1}{2}$;其中,所有正确结论的序号是?;(II)曲线$W$上的点到原点距离的最小值为?.

Cannot annotate. Reason: 题型不符


## Question 10
已知$F_{1}$、$F_{2}$为双曲线C:$x^{2}-y^{2}=1$的左、右焦点,点P在C上,$\angle F_{1}PF_{2}=60^{\circ}$,则$|PF_{1}|\cdot|PF_{2}|$=?

Fact list:
```
C: Hyperbola
P, F1, F2: Point
Expression(C) = (x^2-y^2=1)
F1 = LeftFocus(C)
F2 = RightFocus(C)
PointOnCurve(P, C) = True
AngleOf(F1,P,F2) = ApplyUnit(60, degree)
```

Query list:
```
Abs(LineSegmentOf(P, F1)) * Abs(LineSegmentOf(P, F2))
```

Answer list:
```
4
```


## Question 11
过点$P(-1,0)$作曲线$C$:$y=e^{x}$的切线,切点为$T_{1}$,设$T_{1}$在$x$轴上的投影是点$H_{1}$,过点$H_{1}$再作曲线$C$的切线,切点为$T_{2}$,设$T_{2}$在$x$轴上的投影是点$H_{2}$,...,依次下去,得到第$n+1$$(n\in N)$个切点$T_{n+1}$.则点$T_{n+1}$的坐标为?

Cannot annotate. Reason: 知识点不符


## Question 12
在平面直角坐标系$xOy$中,设点$P$为圆$C$:$(x-1)^{2}+y^{2}=4$上的任意一点,点$Q(2a,a-3)(a\in R)$,则线段$PQ$长度的最小值为?

Fact list:
```
P: Point
C: Circle
Expression(C) = ((x-1)^2+y^2=4)
PointOnCurve(P, C)
Q: Point
a: Real
Coordinate(Q) = (2*a, a-3)
```

Query list:
```
Min(Length(LineSegmentOf(P, Q)))
```

Answer list:
```
sqrt(5) - 2
```


## Question 13
已知抛物线$y^{2}=-8x$的准线过双曲线$\frac{x^{2}}{m}-\frac{y^{2}}{3}=1$的右焦点,则双曲线的离心率为?

Fact list:
```
Parabola_A : Parabola
Hyperbola_A : Hyperbola
m: Number
PointOnCurve(RightFocus(Hyperbola_A), Directrix(Parabola_A)) = True
Expression(Parabola_A) = (y^2 = -8*x)
Expression(Hyperbola_A) = (x^2/m - y^2/3 = 1)
```

Query list:
```
Eccentricity(Hyperbola_A)
```

Answer list:
```
2
```


## Question 14
若双曲线$x^{2}+ky^{2}=1$的离心率是$2$,则实数$k$的值是?

Fact list:
```
C: Hyperbola
k: Real
Expression(C) = ( k*y^2 + x^2 = 1 )
Eccentricity(C) = 2
```

Query list:
```
k
```

Answer list:
```
-1/3
```


## Question 15
过双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$的左焦点$F$作圆$O$:$x^{2}+y^{2}=a^{2}$的两条切线,记切点为$A$、$B$,双曲线左顶点为$C$,若$\angle ACB=120^{\circ}$,则双曲线的离心率为?

Fact list:
```
E: Hyperbola
a: Number
b: Number
Expression(E) = ( -y^2/b^2 + x^2/a^2 = 1 )
F: Point
LeftFocus(E) = F
O: Circle
Expression(O) = ( x^2 + y^2 = a^2 )
l1: Line
l2: Line
TangentOfPoint(F, O) = {l1, l2}
A, B: Point
TangencyPoint(l1, O) = A
TangencyPoint(l2, O) = B
C: Point
LeftVertex(E) = C
AngleOf(A, C, B) = ApplyUnit(120, degree)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
2
```


## Question 16
圆$O_{1}$和圆$O_{2}$的极坐标方程分别为$\rho=4\cos\theta,\rho=-4\sin\theta$,则经过两圆圆心的直线的直角坐标方程为?

Cannot annotate. Reason: 知识点不符


## Question 17
直线$l$与双曲线C:$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$交于$A,B$两点,$M$是线段$AB$的中点,若$l$与$OM$($O$是原点)的斜率的乘积等于$1$,则此双曲线的离心率为?

Fact list:
```
l: Line
C: Hyperbola
a, b: Number
A, B: Point
M:Point
O:Origin
Expression(C)=(x^2/a^2-y^2/b^2=1)
a>0
b>0
{A,B}=Intersection(l,C)
M=MidPoint(LineSegmentOf(A,B))
Slope(l)*Slope(LineSegmentOf(O,M))=1
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(2)
```


## Question 18
在平面直角坐标系$Oxy$中,若双曲线$\frac{x^{2}}{m}-\frac{y^{2}}{m^{2}+4}=1$的焦距为8,则$m$=?

Fact list:
```
C_1 : Hyperbola
m : Number
Expression(C_1) = (x^2/m - y^2/((m^2)+4) = 1)
FocalLength(C_1) = 8
```

Query list:
```
m
```

Answer list:
```
3
```


## Question 19
焦点在$y$轴上,渐近线方程为$y=\pm2x$的双曲线的离心率为?

Fact list:
```
C: Hyperbola
PointOnCurve(Focus(C), yAxis) = True
Expression(Asymptote(C)) = (y=pm*2*x)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(5)/2
```


## Question 20
设点$P$是双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$与圆$x^{2}+y^{2}=a^{2}+b^{2}$在第一象限的交点,其中$F_{1}$、$F_{2}$分别是双曲线的左、右焦点,若$\tan\angle PF_{2}F_{1}=3$,则双曲线的离心率为?

Fact list:
```
C: Hyperbola
a: Number
b: Number
a>0
b>0
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
D: Circle
Expression(D) = ( x^2 + y^2 = a^2 + b^2 )
P: Point
Quadrant(P) = 1
P = OneOf(Intersection(C, D))
F1, F2: Point
LeftFocus(C) = F1
RightFocus(C) = F2
Tan(AngleOf(P, F2, F1)) = 3
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(10)/2
```


## Question 21
(1)(坐标系与参数方程选做题)已知在极坐标系下,点$A(1,\frac{\pi}{3}),B(3,\frac{2\pi}{3}),O$是极点,则$\Delta AOB$的面积等于?

Cannot annotate. Reason: 知识点不符


## Question 22
已知过抛物线$y^{2}=2px(p>0)$的焦点$F$且斜率为$\sqrt{3}$的直线与抛物线交于$A,B$两点,且$|AF|>|BF|$,则$\frac{|AF|}{|BF|}$=?

Fact list:
```
C1:Parabola
p:Number
L:Line
F,A,B:Point
Expression(C1) = (y^2=2*p*x)
p>0
Focus(C1)=F
Slope(L)=sqrt(3)
PointOnCurve(F,L)=True 
Intersection(L,C1)={A,B}
Abs(LineSegmentOf(A,F))>Abs(LineSegmentOf(B,F))
```

Query list:
```
Abs(LineSegmentOf(A,F))/Abs(LineSegmentOf(B,F))
```

Answer list:
```
3
```


## Question 23
双曲线$\frac{x^{2}}{9}-\frac{y^{2}}{16}=1$的一个焦点到一条渐近线的距离为?

Fact list:
```
Hyperbola_1: Hyperbola
F: Point
Asymptote_1: Line
Expression(Hyperbola_1) = (x^2/9-y^2/16=1)
```

Query list:
```
Distance(OneOf(Focus(Hyperbola_1)), OneOf(Asymptote(Hyperbola_1))))
```

Answer list:
```
4
```


## Question 24
若双曲线的渐近线方程为$y=\pm3x$,它的一个焦点是$(\sqrt{10},0)$,则双曲线的标准方程是?

Fact list:
```
C_1 : Hyperbola
Expression(Asymptote(C_1)) = (y = pm*3*x)
F : Point
Coordinate(OneOf(Focus(C_1))) = (sqrt(10),0)
```

Query list:
```
Expression(C_1)
```

Answer list:
```
(x^2-y^2/9 = 1)
```


## Question 25
我们把形如$y=\frac{b}{|x|-a}(a>0,b>0)$的函数称为“莫言函数”,并把其与$y$轴的交点关于原点的对称点称为“莫言点”,以“莫言点”为圆心凡是与“莫言函数”图象有公共点的圆,皆称之为“莫言圆”.当$a=1,b=1$时,在所有的“莫言圆”中,面积的最小值?

Cannot annotate. Reason: 新定义问题


## Question 26
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的一条渐近线的斜率为$\sqrt{2}$,且右焦点与抛物线$y^{2}=4\sqrt{3}x$的焦点重合,则该双曲线的方程为?

Fact list:
```
C: Hyperbola
b, a: Number
a>0
b>0
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
Slope(OneOf(Asymptote(C))) = sqrt(2)
D: Parabola
Expression(D) = ( y^2 = 4*(sqrt(3)*x) )
RightFocus(C) = Focus(D)
```

Query list:
```
Expression(C)
```

Answer list:
```
x^2-y^2/2=1
```


## Question 27
已知点$A(-3,0)$和圆$O$:$x^{2}+y^{2}=9$,$AB$是圆$O$的直径,$M$和$N$是$AB$的三等分点,$P$(异于$A,B$)是圆$O$上的动点,$PD\bot AB$于$D$,$\overrightarrow{PE}=\lambda\overrightarrow{ED}(\lambda>0)$,直线$PA$与$BE$交于$C$,则当$\lambda$=?时,$|CM|+|CN|$为定值.

Cannot annotate. Reason: 算子缺失


## Question 28
已知点$P(2,-3)$是双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$上一点,双曲线两个焦点间的距离等于4,则该双曲线方程是?

Fact list:
```
P: Point
Hyperbola_1: Hyperbola 
F1, F2: Point 
a, b:Number
Coordinate(P) = (2,-3)
Expression(Hyperbola_1) = (x^2/a^2-y^2/b^2=1)
a>0
b>0
PointOnCurve(P, Hyperbola_1)
{F1, F2} = Focus(Hyperbola_1)
Distance(F1, F2) = 4
```

Query list:
```
Expression(Hyperbola_1)
```

Answer list:
```
x^2-y^2/3=1
```


## Question 29
方程$\frac{x^{2}}{a}+\frac{y^{2}}{b}=1(a,b\in\{1,2,3,4,...,2013\})$的曲线中,所有圆面积的和等于?离心率最小的椭圆方程为?

Cannot annotate. Reason: 其他


## Question 30
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的左右焦点为$F_{1},F_{2}$,$P$为双曲线右支上的任意一点,若$\frac{|PF_1|^2}{|PF_2|}$的最小值为$8a$,则双曲线的离心率的取值范围是?

Fact list:
```
Hyperbola_A: Hyperbola
Expression(Hyperbola_A) = (x^2/a^2 - y^2/b^2=1)
a,b:Number
a>0
b>0
F1,F2: Point
F1 = LeftFocus(Hyperbola_A)
F2 = RightFocus(Hyperbola_A)
P: Point
PointOnCurve(P, RightPart(Hyperbola_A))
Min(Abs(LineSegmentOf(P, F1))^2 / Abs(LineSegmentOf(P, F2))) = 8*a
```

Query list:
```
Range(Eccentricity(Hyperbola_A))
```

Answer list:
```
(1,3]
```


## Question 31
已知椭圆$\frac{x^{2}}{3m}+\frac{y^{2}}{5n}=1$和双曲线$\frac{x^{2}}{2m}-\frac{y^{2}}{3n}=1$有公共的焦点,那么双曲线的渐近线方程是?

Fact list:
```
C: Hyperbola
n: Number
m: Number
D: Ellipse
Expression(C) = ( -1/(3*n)*y^2 + x^2/((2*m)) = 1 )
Expression(D) = ( y^2/((5*n)) + x^2/((3*m)) = 1 )
Focus(D) = Focus(C)
```

Query list:
```
Expression(Asymptote(C))
```

Answer list:
```
(y=pm*sqrt(3)/4*x)
```


## Question 32
抛物线$x^{2}=8y$的准线与$y$轴交于点$A$,点$B$在抛物线对称轴上,过$A$可作直线交抛物线于点$M$、$N$,使得$\overrightarrow{BM}\cdot\overrightarrow{MN}=-\frac{1}{2}\overrightarrow{MN}^{2}$,则$|OB|$的取值范围是?

Fact list:
```
C: Parabola
Expression(C) = (x^2 = 8*y)
A: Point
Intersection(Directrix(C), yAxis) = A
B: Point
PointOnCurve(B, SymmetryAxis(C)) = True
l: Line
PointOnCurve(A, l) = True
M, N: Point
Intersection(l, C) = {M, N}
DotProduct(VectorOf(B, M), VectorOf(M, N)) = -1/2 * VectorOf(M, N)^2
O: Origin
```

Query list:
```
Range(Abs(LineSegmentOf(O, B)))
```

Answer list:
```
(6, +oo)
```


## Question 33
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0, b>0)$的焦点到渐近线的距离为$a$，则双曲线离心率为?

Fact list:
```
C:Hyperbola
a, b:Number
Expression(C)=(x^2/a^2-y^2/b^2=1)
a>0
b>0
Distance(Focus(C),Asymptote(C))=a
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(2)
```


## Question 34
过抛物线$y^{2}=4x$的焦点作一条倾斜角为$\alpha$,长度不超过$8$的弦,弦所在的直线与圆$x^{2}+y^{2}=\frac{3}{4}$有公共点,则$\alpha$的取值范围是?

Fact list:
```
Parabola_1: Parabola 
alpha: Number
Chord_1: LineSegment 
Circle_1: Circle
Expression(Parabola_1) = (y^2=4*x)
PointOnCurve(Focus(Parabola_1), Chord_1) = True 
Inclination(Chord_1) = alpha
Length(Chord_1) <= 8
Expression(Circle_1) = (x^2+y^2=3/4)
IsIntersect(OverlappingLine(Chord_1),Circle_1) = True
```

Query list:
```
Range(alpha)
```

Answer list:
```
[pi/4,pi/3]+[2*pi/3,3*pi/4]
```


## Question 35
椭圆$\frac{x^{2}}{4a^{2}}+\frac{y^{2}}{3a^{2}}=1(a>0)$的左焦点为F,直线$x=m$与椭圆相交于点$A$、$B$,当$\triangle FAB$的周长最大时,$\triangle FAB$的面积是?

Cannot annotate. Reason: 其他


## Question 36
已知抛物线$y^{2}=4x$的焦点$F$恰好是双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$$(a>0,b>0)$的右顶点,且渐近线方程为$y=\pm\sqrt{3}x$,则双曲线方程为?

Fact list:
```
Parabola_A : Parabola
Expression(Parabola_A) = (y^2 = 4*x)
Hyperbola_A : Hyperbola
Expression(Hyperbola_A) = (x^2/a^2 - y^2/b^2 =1)
a,b : Number
a>0
b>0
F:Point
F = Focus(Parabola_A)
F= RightVertex(Hyperbola_A)
Expression(Asymptote(Hyperbola_A)) = (y=pm*sqrt(3) * x)
```

Query list:
```
Expression(Hyperbola_A)
```

Answer list:
```
(x^2 - y^2/3 = 1)
```


## Question 37
以双曲线:$\frac{x^{2}}{8}-y^{2}=1$的右焦点为圆心,并与其渐近线相切的圆的标准方程是?

Fact list:
```
C: Hyperbola
Expression(C) = (x^2/8 - y^2 = 1)
D: Circle
Center(D) = RightFocus(C)
IsTangent(D, Asymptote(C)) = True
```

Query list:
```
Expression(D)
```

Answer list:
```
(x-3)^2 + y^2 = 1
```


## Question 38
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$,若过右焦点F且倾斜角为$30^\circ$的直线与双曲线的右支有两个交点,则此双曲线离心率的取值范围是?

Fact list:
```
C: Hyperbola
a, b: Number
Expression(C) = (x^2/a^2-y^2/b^2=1)
a>0
b>0
F: Point
RightFocus(C) = F
l: Line
PointOnCurve(F, l) = True
Inclination(l) = ApplyUnit(30, degree)
NumIntersection(l, RightPart(C)) = 2
```

Query list:
```
Range(Eccentricity(C))
```

Answer list:
```
(1, 2/3*sqrt(3))
```


## Question 39
已知椭圆方程$\frac{x^{2}}{9}+\frac{y^{2}}{5}=1$,点$F_{1}(2,0)$、$A(1,1)$,$P$为椭圆上任意一点,则$|PA|+|PF_{1}|$的取值范围是?

Fact list:
```
C:Ellipse
F1,A,P:Point
Expression(C)=(x^2/9+y^2/5=1)
Coordinate(F1)=(2,0)
Coordinate(A)=(1,1)
PointOnCurve(P,C)
```

Query list:
```
Range(Abs(LineSegmentOf(P,A))+Abs(LineSegmentOf(P,F1)))
```

Answer list:
```
[6-sqrt(10),6+sqrt(10)]
```


## Question 40
已知对称中心为原点的双曲线$x^{2}-y^{2}=\frac{1}{2}$与椭圆有公共的焦点,且它们的离心率互为倒数,则该椭圆的标准方程为?

Fact list:
```
O: Origin
C1: Ellipse
Center(C1) = O
Expression(C1) = (x^2 - y^2 = 1/2)
C2: Parabola
Center(C2) = O
Focus(C1) = Focus(C2)
InterReciprocal(Eccentricity(C1), Eccentricity(C2)) = True
```

Query list:
```
Expression(C2)
```

Answer list:
```
x^2/2+y^2=1
```


## Question 41
已知$B$为双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的左准线与$x$轴的交点,点$A(0,b)$,若满足$\overrightarrow{AP}=2\overrightarrow{AB}$的点$P$在双曲线上,则该双曲线的离心率为?

Fact list:
```
B: Point
Hyperbola_A : Hyperbola
Expression(Hyperbola_A) = (x^2/a^2 - y^2/b^2 = 1)
a,b : Number
a > 0
b > 0
Intersection(LeftDirectrix(Hyperbola_A), xAxis) = B
A: Point
P: Point
Coordinate(A) = (0,b)
VectorOf(A, P) = 2 * VectorOf(A, B)
PointOnCurve(P, Hyperbola_A) = True
```

Query list:
```
Eccentricity(Hyperbola_A)
```

Answer list:
```
sqrt(2)
```


## Question 42
已知曲线$C_{1}$:$\rho=2\sqrt{2}$和曲线$C_{2}$:$\rho\cos(\theta+\frac{\pi}{4})=\sqrt{2}$,则$C_{1}$上到$C_{2}$的距离等于$\sqrt{2}$的点的个数为?

Cannot annotate. Reason: 知识点不符


## Question 43
已知抛物线$y=x^{2}$上有一条长为$2$的动弦$AB$,则$AB$中点$M$到$x$轴的最短距离为?

Fact list:
```
C: Parabola
Expression(C) = (y = x^2)
A, B: Point
IsChordOf(LineSegmentOf(A, B), C) = True
Length(LineSegmentOf(A, B)) = 2
M: Point
MidPoint(LineSegmentOf(A, B)) = M
```

Query list:
```
Min(Distance(M, xAxis))
```

Answer list:
```
3/4
```


## Question 44
若抛物线$y^{2}=x$上一点$P$到准线的距离等于它到顶点的距离,则点$P$的坐标为?

Fact list:
```
C: Parabola
Expression(C) = (y^2 = x)
P: Point
PointOnCurve(P, C) = True
Distance(P, Directrix(C)) = Distance(P, Vertex(C))
```

Query list:
```
Coordinate(P)
```

Answer list:
```
{(1/8, sqrt(2)/4), (1/8, -sqrt(2)/4)}
```


## Question 45
圆$(x-a)^{2}+y^{2}=1$与双曲线$x^{2}-y^{2}=1$的渐近线相切,则$a$的值是?

Fact list:
```
C1:Circle
C2:Hyperbola
a:Number
Expression(C1)=((x-a)^2+y^2=1)
Expression(C2)=(x^2-y^2=1)
IsTangent(C1, Asymptote(C2))
```

Query list:
```
a
```

Answer list:
```
pm*sqrt(2)
```


## Question 46
已知抛物线$y^{2}=4x$的焦点为$F$,过抛物线在第一象限部分上一点P的切线为$l$,过$P$点作平行于$x$轴的直线$m$,过焦点$F$作平行于$l$的直线交$m$于$M$,若$|PM|=4$,则点$P$的坐标为?

Fact list:
```
m: Line
C: Parabola
D: Line
P: Point
M: Point
F: Point
l: Line
Expression(C) = ( y^2 = 4*x )
Focus(C) = F
Quadrant(P) = 1
TangentOfPoint(P, C) = l
PointOnCurve(P, C) = True
PointOnCurve(P, m) = True
IsParallel(xAxis, m) = True
PointOnCurve(F, D) = True
IsParallel(l, D) = True
Intersection(D, m) = M
Abs(LineSegmentOf(P, M)) = 4
```

Query list:
```
Coordinate(P) = ?
```

Answer list:
```
(3, 2*sqrt(3))
```


## Question 47
已知双曲线过点$(4,\frac{4\sqrt{7}}{3})$,渐近线方程为$y=\pm\frac{4}{3}x$,圆$C$经过双曲线的一个顶点和一个焦点且圆心在双曲线上,则圆心到该双曲线的中心的距离是?

Fact list:
```
Hyperbola_1: Hyperbola
Point_1: Point
C: Circle
Center_1: Point
Coordinate(Point_1) = (4,4*sqrt(7)/3)
PointOnCurve(Point_1, Hyperbola_1) = True
Expression(Asymptote(Hyperbola_1)) = (y=pm*4/3*x)
PointOnCurve(OneOf(Focus(Hyperbola_1)), C) = True
PointOnCurve(OneOf(Vertex(Hyperbola_1)), C) = True
PointOnCurve(Center(C), Hyperbola_1)
```

Query list:
```
Distance(Center(C), Center(Hyperbola_1))
```

Answer list:
```
16/3
```


## Question 48
抛物线$y=ax^{2}$的准线方程是$y=-1$,$a$的值为?

Fact list:
```
Parabola_A: Parabola
a:Number
Expression(Parabola_A) = (y=a*x^2)
Expression(Directrix(Parabola_A)) = (y=-1)
```

Query list:
```
a
```

Answer list:
```
1/4
```


## Question 49
过椭圆$C:\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$长轴的一个顶点作圆$x^{2}+y^{2}=b^{2}$的两条切线,切点分别为$A,B$,若$\angle AOB=90^{\circ}$($O$是坐标原点),则椭圆$C$的离心率为?

Fact list:
```
C: Ellipse
a, b: Number
Expression(C) = (x^2/a^2 + y^2/b^2 = 1)
a>b
b>0
P:Point
In(P, Endpoint(MajorAxis(C)))
L1, L2: Line
C2: Circle
Expression(C2)=(x^2 + y^2=b^2)
{L1, L2} = TangentOfPoint(P, C2)
A, B: Point
TangencyPoint(L1, C2) = A
TangencyPoint(L2, C2) = B
O: Origin
AngleOf(A, O, B) = ApplyUnit(90, degree)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(2) / 2
```


## Question 50
若双曲线$x^{2}-\frac{y^{2}}{15}=1$的离心率为$e$,则$e$=?

Fact list:
```
e: Number
C: Hyperbola
Expression(C) = (x^2 - y^2/15 = 1)
e = Eccentricity(C)
```

Query list:
```
e
```

Answer list:
```
4
```


## Question 51
若直线$y=x+k$与曲线$x=\sqrt{1-y^{2}}$恰有一个公共点,则$k$的取值范围是?

Fact list:
```
L:Line
C:Curve
k:Number
Expression(L)=(y=x+k)
Expression(C)=(x=sqrt(1-y^2))
NumIntersection(L,C)=1
```

Query list:
```
Range(k)
```

Answer list:
```
(-1,1)+{-sqrt(2)}
```


## Question 52
椭圆$\frac{x^{2}}{25}+\frac{y^{2}}{16}=1$的左右焦点为$F_{1},F_{2}$,弦$AB$过点$F_{1}$,若$\triangle ABF_{2}$的内切圆周长为$\pi$,点$A,B$坐标分别为$(x_{1},y_{1}),(x_{2},y_{2})$,则$|y_{1}-y_{2}|$=?

Fact list:
```
C: Ellipse
Expression(C) = (x^2/25 + y^2/16 = 1)
F1, F2: Point
LeftFocus(C) = F1
RightFocus(C) = F2
A, B: Point
IsChordOf(LineSegmentOf(A, B), C) = True
PointOnCurve(F1, LineSegmentOf(A, B)) = True
Perimeter(InscribedCircle(TriangleOf(A, B, F2))) = pi
x1, x2, y1, y2: Number
Coordinate(A) = (x1, y1)
Coordinate(B) = (x2, y2)
```

Query list:
```
Abs(y1-y2)
```

Answer list:
```
5/3
```


## Question 53
设双曲线$C:\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>b>0)$的右焦点为$F$,左右顶点分别为$A_{1},A_{2}$,过$F$且与双曲线$C$的一条渐近线平行的直线$l$与另一条渐近线相交于$P$,若$P$恰好在以$A_{1}A_{2}$为直径的圆上,则双曲线的离心率为?

Fact list:
```
C: Hyperbola
a, b: Number
Expression(C) = (x^2/a^2 - y^2/b^2 = 1)
a>b
b>0
F: Point
RightFocus(C) = F
A1, A2: Point
LeftVertex(C) = A1
RightVertex(C) = A2
l: Line
PointOnCurve(F, l) = True
l1, l2: Line
Asymptote(C) = {l1, l2}
IsParallel(l, l1) = True
P: Point
Intersection(l, l2) = P
M: Circle
IsDiameter(LineSegmentOf(A1, A2), M) = True
PointOnCurve(P, M) = True
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(2)
```


## Question 54
已知直线$l$经过椭圆$\frac{y^{2}}{2}+x^{2}=1$的焦点并且与椭圆相交于$P,Q$两点,线段$PQ$的垂直平分线与$x$轴相交于点$M$,则$\Delta MPQ$面积的最大值为?

Fact list:
```
C: Ellipse
l: Line
M, P, Q: Point
Expression(C) = (y^2/2+x^2=1)
PointOnCurve(Focus(C), l)
Intersection(l, C) = {P, Q}
M = Intersection(PerpendicularBisector(LineSegmentOf(P, Q)), xAxis)
```

Query list:
```
Max(Area(TriangleOf(M, P, Q)))
```

Answer list:
```
3*sqrt(6)/8
```


## Question 55
若关于$x$的方程$x^{3}+ax^{2}+bx+c=0$的三个根可分别作为一个椭圆、双曲线、抛物线的离心率,则$\frac{b}{a}$的取值范围为?

Cannot annotate. Reason: 知识点不符


## Question 56
已知椭圆$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$的右焦点为$F$,$P$点在椭圆上,以$P$点为圆心的圆与$y$轴相切,且同时与$x$轴相切于椭圆的右焦点$F$,则椭圆$\frac{y^{2}}{a^{2}}+\frac{x^{2}}{b^{2}}=1$的离心率为?

Fact list:
```
C1, C2:Ellipse
a, b: Number
a>b
b>0
Expression(C1) = (x^2/a^2 + y^2/b^2=1)
F,P:Point
C3:Circle
F=RightFocus(C1)
PointOnCurve(P, C1)
Center(C3) = P
IsTangent(C3, yAxis) 
TangencyPoint(C3, xAxis) = F
Expression(C2) = (y^2/a^2+x^2/b^2 = 1)
```

Query list:
```
Eccentricity(C2)
```

Answer list:
```
(sqrt(5)-1)/2
```


## Question 57
如图,已知椭圆$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$的左、右准线分别为$l_{1},l_{2}$,且分别交$x$轴于$C,D$两点,从$l_{1}$上一点$A$发出一条光线经过椭圆的左焦点$F$被$x$轴反射后与$l_{2}$交于点$B$,若$AF\bot BF$,且$\angle ABD=75^{\circ}$,则椭圆的离心率=?

Cannot annotate. Reason: 知识点不符


## Question 58
在$\triangle ABC$中,角$A$、$B$、$C$的对边分别$a$、$b$、$c$,若$a^{2}+b^{2}=\frac{1}{2}c^{2}$.则直线$ax-by+c=0$被圆$x^{2}+y^{2}=9$所截得的弦长为?

Cannot annotate. Reason: 其他


## Question 59
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的一条渐近线与直线$x+2y-1=0$垂直,则曲线的离心率等于?

Fact list:
```
Hyperbola_1: Hyperbola
a, b: Number
Line_1: Line

Expression(Hyperbola_1) = (x^2/a^2-y^2/b^2=1)
a>0
b>0
Expression(Line_1) = (x+2*y-1=0)
IsPerpendicular(Line_1, OneOf(Asymptote(Hyperbola_1)))
```

Query list:
```
Eccentricity(Hyperbola_1)
```

Answer list:
```
sqrt(5)
```


## Question 60
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$的一条渐近线方程为$y=2x$,则其离心率为?

Fact list:
```
Hyperbola_A : Hyperbola
a,b : Number
Expression(Hyperbola_A) = (x^2/a^2 - y^2/b^2 = 1)
Expression(OneOf(Asymptote(Hyperbola_A))) = (y=2*x)
```

Query list:
```
Eccentricity(Hyperbola_A)
```

Answer list:
```
sqrt(5)
```


## Question 61
抛物线$y=x^{2}$在点?处的切线平行于直线$y=4x-5$。

Fact list:
```
C: Parabola
Expression(C) = ( y = x^2 )
D: Line
Expression(D) = ( y = 4*x - 5 )
P: Point
IsParallel(TangentOnPoint(P, C), D)
```

Query list:
```
Coordinate(P)
```

Answer list:
```
(2,4)
```


## Question 62
若双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的一条渐近线方程为$y=-\frac{x}{3}$,则此双曲线的离心率是?

Fact list:
```
C: Hyperbola
a, b: Number
a>0
b>0
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
Expression(OneOf(Asymptote(C))) = (y = -x/3)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(10) / 3
```


## Question 63
设$A$、$B$为在双曲线$x^{2}-\frac{y^{2}}{2}=1$上两点,O为坐标原点.若$\overrightarrow{OA}\cdot\overrightarrow{OB}=0$,则$\triangle AOB$面积的最小值为?

Fact list:
```
A, B: Point
O: Origin
C: Hyperbola
Expression(C) = ( x^2 - y^2/2 = 1 )
PointOnCurve(A, C)
PointOnCurve(B, C)
DotProduct(VectorOf(O, A), VectorOf(O,B))=0
```

Query list:
```
Min(Area(TriangleOf(A, O, B)))
```

Answer list:
```
2
```


## Question 64
已知抛物线$y^{2}=8x$的准线$l$与双曲线$C:\frac{x^{2}}{a^{2}}-y^{2}=1$相切,则双曲线$C$的离心率$e$=?

Fact list:
```
Parabola_1: Parabola
l: Line
C: Hyperbola
e, a: Number

Expression(Parabola_1) = (y^2=8*x)
Directrix(Parabola_1) = l 
Expression(C) = (x^2/a^2-y^2=1)
IsTangent(l, C) = True
Eccentricity(C) = e
```

Query list:
```
e
```

Answer list:
```
sqrt(5)/2
```


## Question 65
已知抛物线$y^{2}=8x$,焦点为$F$,准线为$l$,$P$为抛物线上一点,$PA\bot l$,$A$为垂足,如果直线$AF$的斜率为$-\sqrt{3}$,那么$PF$=?

Fact list:
```
C: Parabola
Expression(C) = (y^2=8*x)
F: Point
F = Focus(C)
P: Point
l: Line
PointOnCurve(P, C)
IsPerpendicular(LineSegmentOf(P, A), l)
A: Point
FootPoint(LineSegmentOf(P, A), l) = A
Slope(LineOf(A, F)) = -sqrt(3)
```

Query list:
```
LineSegmentOf(P, F)
```

Answer list:
```
8
```


## Question 66
若实数$a$、$b$、$c$成等差数列,点$P(–1,0)$在动直线$l$:$ax+by+c=0$上的射影为$M$,点$N(0,3)$,则线段$MN$长度的最小值是?

Cannot annotate. Reason: 知识点不符


## Question 67
若抛物线$y^{2}=2px(p>0)$的焦点与双曲线$\frac{x^{2}}{6}-\frac{y^{2}}{10}=1$的右焦点重合,则实数$p$的值是?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/6 - y^2/10 = 1 )
D: Parabola
p: Real
p>0
Expression(D) = ( y^2 = 2*(p*x) )
Focus(D) = RightFocus(C)
```

Query list:
```
p
```

Answer list:
```
8
```


## Question 68
过抛物线$y^{2}=4x$的焦点,且被圆$x^{2}+y^{2}-4x+2y=0$截得弦最长的直线的方程是?

Cannot annotate. Reason: 算子缺失


## Question 69
已知椭圆$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$的左焦点$F_{1}$,$O$为坐标原点,点$P$在椭圆上,点$Q$在椭圆的右准线上,若$\overrightarrow{PQ}=2\overrightarrow{F_{1}O}$,$\overrightarrow{F_{1}Q}=\lambda(\frac{\overrightarrow{F_{1}P}}{|\overrightarrow{F_{1}P}|}+\frac{\overrightarrow{F_{1}O}}{|\overrightarrow{F_{1}O}|})(\lambda>0)$,则椭圆的离心率为?

Fact list:
```
C:Ellipse
a, b, lambda:Number
F1, P, Q:Point
O:Origin
a>b 
b>0
Expression(C)=(x^2/a^2+y^2/b^2=1)
LeftFocus(C)=F1
PointOnCurve(P,C)
PointOnCurve(Q,RightDirectrix(C))
VectorOf(P,Q)=2*VectorOf(F1,O)
VectorOf(F1,Q) = lambda * (VectorOf(F1,P)/Abs(VectorOf(F1,P))+VectorOf(F1,O)/Abs(VectorOf(F1,O)))
lambda>0
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
(sqrt(5)-1)/2
```


## Question 70
已知双曲线$C$:$\frac{x^{2}}{4}-\frac{y^{2}}{5}=1$的右焦点为$F$,过$F$的直线$l$与$C$交于两点$A,B$,若$|AB|=5$,则满足条件的$l$的条数为?

Cannot annotate. Reason: 其他


## Question 71
过点$(1,2)$总可作两条直线与圆$x^{2}+y^{2}+kx+2y+k^{2}-15=0$相切,则实数$k$的取值范围是?

Fact list:
```
Point_1: Point 
l1, l2: Line
C: Circle
Coordinate(Point_1) = (1,2)
Expression(C) = (x^2+y^2+k*x+2*y+k^2-15=0)
{l1, l2} = TangentOfPoint(Point_1, C)
```

Query list:
```
Range(k)
```

Answer list:
```
(2, 8*sqrt(3)/3) + (-8*sqrt(3)/3, -3)
```


## Question 72
已知椭圆$C:\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$和圆$O:x^{2}+y^{2}=b^{2}$,若$C$上存在点$P$,使得过点$P$引圆$O$的两条切线,切点分别为$A,B$,满足$\angle APB=60^{\circ}$,则椭圆$C$的离心率的取值范围是?

Fact list:
```
C: Ellipse
O: Circle
a,b : Number
Expression(C) = (x^2/a^2 + y^2/b^2 = 1)
a>b
b>0
Expression(O) = (x^2 + y^2 = b^2)
P:Point
PointOnCurve(P, C)
L1, L2 : Line
TangentOfPoint(P, O) = {L1, L2}
A, B : Point
TangencyPoint(L1, O) = A
TangencyPoint(L2, O) = B
AngleOf(A, P, B) = ApplyUnit(60, degree)
```

Query list:
```
Range(Eccentricity(C))
```

Answer list:
```
[sqrt(3)/2, 1)
```


## Question 73
椭圆$\frac{x^{2}}{9}+\frac{y^{2}}{2}=1$的焦点为$F_{1}$、$F_{2}$,点$P$在椭圆上,若$|PF_{1}|=4$,$\angle F_{1}PF_{2}$的大小为?

Fact list:
```
C: Ellipse
Expression(C) = ( x^2/9 + y^2/2 = 1 )
F1, F2: Point
Focus(C) = {F1, F2}
P: Point
PointOnCurve(P, C) = True
Abs(LineSegmentOf(P, F1)) = 4
```

Query list:
```
AngleOf(F1, P, F2)
```

Answer list:
```
ApplyUnit(120, degree)
```


## Question 74
已知直线$y=kx$是曲线$y=\ln x$的切线,则$k$=?

Fact list:
```
l: Line
k: Number
Expression(l) = (y=k*x)
C: Curve
Expression(C) = (y=ln(x))
IsTangent(l, C) = True
```

Query list:
```
k
```

Answer list:
```
1/e
```


## Question 75
已知直线$y=m$与椭圆$\frac{x^{2}}{3}+\frac{y^{2}}{4}=1$有两个不同的交点,则实数$m$的取值范围是?

Fact list:
```
C: Ellipse
Expression(C) = ( x^2/3 + y^2/4 = 1 )
D: Line
m: Real
Expression(D) = ( y = m )
NumIntersection(D, C) = 2
```

Query list:
```
Range(m)
```

Answer list:
```
(-2, 2)
```


## Question 76
在直角坐标系中,曲线$C_{1}$的参数方程为$\left\{\begin{matrix}x=\cos\theta\\y=\sin\theta\\\end{matrix}\right.\theta\in[0,\pi]$,以$x$轴的正半轴为极轴建立极坐标系,曲线$C_{2}$在极坐标系中的方程为$\rho=\frac{b}{\sin\theta-\cos\theta}$.若曲线$C_{1}$与$C_{2}$有两个不同的交点,则实数$b$的取值范围是?

Cannot annotate. Reason: 知识点不符


## Question 77
已知$F$是双曲线C:$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a,b>0)$的左焦点,$B_{1}B_{2}$是双曲线的虚轴,$M$是$OB_{1}$的中点,过$F$的直线交双曲线C于$A$,且$\overrightarrow{FM}=2\overrightarrow{MA}$,则双曲线$C$离心率是?

Fact list:
```
C: Hyperbola
b, a: Number
a>0
b>0
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
F: Point 
LeftFocus(C) = F
B1, B2: Point
O: Origin
LineSegmentOf(B1,B2) = ImageinaryAxis(C)
M: Point
M = MidPoint(LineSegmentOf(O,B1))
Line_1: Line 
A: Point
PointOnCurve(F, Line_1) = True
A = Intersection(Line_1, C)
VectorOf(F,M) = 2*VectorOf(M,A)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
5/2
```


## Question 78
已知点$M(\sqrt{3},0)$,椭圆$\frac{x^{2}}{4}+y^{2}=1$与直线$y=k(x+\sqrt{3})$交于点$A$、$B$,则$\Delta ABM$的周长为?

Fact list:
```
C: Ellipse
Expression(C) = ( x^2/4 + y^2 = 1 )
D: Line
k: Number
Expression(D) = ( y = k* (x + sqrt(3)) )
M: Point
Coordinate(M) = (sqrt(3), 0)
A,B : Point
Intersection(C, D) = {A, B}
```

Query list:
```
Perimeter(TriangleOf(A,B,M))
```

Answer list:
```
8
```


## Question 79
已知$F$是抛物线$C:y^{2}=4x$的焦点,过$F$且斜率为$\sqrt{3}$的直线交$C$于$A$、$B$两点.设$|FA|<|FB|$,若$\overrightarrow{FA}=\lambda \overrightarrow{FB}$,则λ的值为?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 4*x )
F: Point
Focus(C) = F
l: Line
PointOnCurve(F, l) = True
Slope(l) = sqrt(3)
A, B: Point
Intersection(l, C) = {A, B}
Abs(VectorOf(F, A)) < Abs(VectorOf(F, B))
lambda_: Number
VectorOf(F, A) = lambda_ * VectorOf(F, B)
```

Query list:
```
lambda_
```

Answer list:
```
-1/3
```


## Question 80
曲线$y=x(3\ln x+1)$在点$(1,1)$处的切线方程为?

Fact list:
```
C: Curve
Expression(C) = (y=x*(3*ln(x)+1))
P: Point
Coordinate(P) = (1,1)
```

Query list:
```
Expression(TangentOnPoint(P, C))
```

Answer list:
```
4*x-3*y-3=0
```


## Question 81
点$P$是曲线$x^{2}-y-2\ln\sqrt{x}=0$上任意一点,则点$P$到直线$4x+4y+1=0$的最小距离是?

Fact list:
```
C: Line
Expression(C) = ( 4*x + 4*y + 1 = 0 )
D: Curve
Expression(D) = (x^2-y-2*ln(sqrt(x))=0)
P: Point
PointOnCurve(P, D) = True
```

Query list:
```
Min(Distance(P, C))
```

Answer list:
```
sqrt(2)/2*(1+ln(2))
```


## Question 82
过点$P(2,1)$的双曲线与椭圆$\frac{x^{2}}{4}+y^{2}=1$共焦点,则其渐近线方程是?

Fact list:
```
C: Hyperbola
D: Ellipse
Expression(D) = ( x^2/4 + y^2 = 1 )
P: Point
Coordinate(P) = (2,1)
PointOnCurve(P, C) = True
Focus(C) = Focus(D)
```

Query list:
```
Expression(Asymptote(C))
```

Answer list:
```
y=pm*sqrt(2)/2*x
```


## Question 83
已知曲线$C$的极坐标方程是$\rho=4\cos\theta$.以极点为平面直角坐标系的原点,极轴为$x$轴的正半轴,建立平面直角坐标系,直线$l$的参数方程是:$\left\{\begin{matrix}x=\frac{\sqrt{2}}{2}t+1\\y=\frac{\sqrt{2}}{2}t\\\end{matrix}\right.$($t$为参数),则直线$l$与曲线$C$相交所成的弦的弦长为?

Cannot annotate. Reason: 知识点不符


## Question 84
设直线$ax+by+c=0(c\neq0)$与抛物线$y^{2}=2x$交于$P$、$Q$两点,$F$为抛物线的焦点,直线$PF$、$QF$分别交抛物线点$M$、$N$,则直线$MN$的方程为?

Fact list:
```
P: Point
F: Point
Q: Point
L: Line
a, b, c: Number
Negation(c=0)
Expression(L) = (a*x+b*y+c=0)
C: Parabola
Expression(C) = ( y^2 = 2*x )
{P, Q} = Intersection(C, L)
F = Focus(C)
M = Intersection(LineOf(P, F), C)
N = Intersection(LineOf(Q, F), C)
```

Query list:
```
Expression(LineOf(M, N))
```

Answer list:
```
4*c*x-2*b*y+a=0
```


## Question 85
若双曲线$x^{2}-y^{2}=a^{2}(a>0)$的左、右顶点分别为$A$、$B$,点$P$是第一象限内双曲线上的点.若直线$PA$、$PB$的倾斜角分别为$\alpha$、$\beta$,且$\beta=m\alpha(m>1)$,那么$\alpha$的值是?

Fact list:
```
P: Point
A: Point
B: Point
C: Hyperbola
a: Number
a>0
Expression(C) = ( x^2 - y^2 = a^2 )
LeftVertex(C) = A
RightVertex(C) = B
Quadrant(P) = 1
PointOnCurve(P, C) = True
alpha, beta : Number
Inclination(LineOf(P, A)) = alpha
Inclination(LineOf(P,B)) = beta
m : Number
m > 1
beta = m * alpha
```

Query list:
```
alpha
```

Answer list:
```
pi/(2 *m +2)
```


## Question 86
两定点的坐标分别为$A(-1,0)$、$B(2,0)$,动点满足条件$\angle MBA=2\angle MAB$,动点$M$的轨迹方程是?

Fact list:
```
A, B, M: Point
Coordinate(A) = (-1, 0)
Coordinate(B) = (2, 0)
AngleOf(M,B,A) = 2*AngleOf(M,A,B)
```

Query list:
```
LocusEquation(M)
```

Answer list:
```
3*x^2-y^2=1(x>1)
```


## Question 87
已知圆$C:x^{2}+y^{2}=1$,过点$P(0,2)$作圆C的切线,交x轴正半轴于点$Q$.若$M(m,n)$为线段$PQ$(不包括端点)上的动点,则$\frac{\sqrt{3}}{m}+\frac{1}{n}$的最小值为?

Cannot annotate. Reason: 算子缺失


## Question 88
与抛物线$y^{2}=x$有且仅有一个公共点,并且过点$(1,1)$的直线方程为?

Fact list:
```
L:Line
C:Parabola
P:Point
Expression(C)=(y^2=x)
NumIntersection(C,L)=1
Coordinate(P)=(1,1)
PointOnCurve(P,L)
```

Query list:
```
Expression(L)
```

Answer list:
```
{(x-2*y+1=0),(y=1)}
```


## Question 89
已知$a>b>0$,$e_{1}$、$e_{2}$分别是圆锥曲线$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$和$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$的离心率,设$m=\lg e_{1}+\lg e_{2}$,则$m$的取值范围是?

Fact list:
```
a,b,e1,e2,m: Number
a>b
b>0
C1, C2: ConicSection
Expression(C1) = (x^2/a^2+y^2/b^2=1)
Expression(C2) = (x^2/a^2-y^2/b^2=1)
e1 = Eccentricity(C1)
e2 = Eccentricity(C2)
m = lg(e1) + lg(e2)
```

Query list:
```
Range(m)
```

Answer list:
```
(-oo, 0)
```


## Question 90
给出下列三个命题:1若直线$l$过抛物线$y=2x^{2}$的焦点,且与这条抛物线交于$A,B$两点,则$|AB|$的最小值为$2$;2双曲线$C:\frac{x^{2}}{16}-\frac{y^{2}}{9}=-1$的离心率为$\frac{5}{3}$;3若$C_{1}:x^{2}+y^{2}+2x=0,C_{2}:x^{2}+y^{2}+2y-1=0$,则这两圆恰有$2$条公切线.4若直线$l_{1}:$$a^{2}x-y+6=0$与直线$l_{2}:$$4x-(a-3)y+9=0$互相垂直,则$a=-1$.其中正确命题的序号是?

Cannot annotate. Reason: 题型不符


## Question 91
已知曲线$y=x^{2}-1$在$x=x_{0}$处的切线与曲线$y=1-x^{3}$在$x=x_{0}$处的切线互相平行,则$x_0$的值为?

Cannot annotate. Reason: 算子缺失


## Question 92
已知抛物线$y^{2}=2px$的准线与双曲线$x^{2}-y^{2}=2$的左准线重合,则$p$的值为?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2 - y^2 = 2 )
D: Parabola
p: Number
Expression(D) = ( y^2 = 2*(p*x) )
Directrix(D) = LeftDirectrix(C)
```

Query list:
```
p
```

Answer list:
```
2
```


## Question 93
曲线C:$y=\frac{b}{|x|-a}(a>0,b>0)$与$y$轴的交点关于原点的对称点称为“望点”,以“望点”为圆心,凡是与曲线C有公共点的圆,皆称之为“望圆”,则当a=1,b=1时,所有的“望圆”中,面积最小的“望圆”的面积为?

Cannot annotate. Reason: 新定义问题


## Question 94
.已知正方形ABCD边长为1,图形如示,点E为边BC的中点,正方形内部一动点P满足:P到线段AD的距离等于P到点E的距离,那么P点的轨迹与正方形的上、下底边及BC边所围成平面图形的面积为?

Cannot annotate. Reason: 算子缺失


## Question 95
已知两定点$A(-2,0)$、$B(1,0)$,如果动点$P$满足$|PA|=2|PB|$,则点$P$的轨迹方程为?

Fact list:
```
P, A, B: Point
Coordinate(A) = (-2, 0)
Coordinate(B) = (1, 0)
Abs(LineSegmentOf(P, A)) = 2 * Abs(LineSegmentOf(P, B))
```

Query list:
```
LocusEquation(P)
```

Answer list:
```
x^2 + y^2 - 4*x = 0
```


## Question 96
抛物线$x^{2}=2y$的焦点$F$到准线$l$的距离是?

Fact list:
```
C: Parabola
Expression(C) = ( x^2 = 2*y )
l: Line
F: Point
F = Focus(C)
l = Directrix(C)
```

Query list:
```
Distance(F, l)
```

Answer list:
```
1/2
```


## Question 97
在等边$\Delta ABC$中,若以$A,B$为焦点的椭圆经过点$C$,则该椭圆的离心率为?

Cannot annotate. Reason: 算子缺失


## Question 98
若抛物线$y^{2}=4x$上一点$M$到焦点$F$的距离为$4$,则点$M$的横坐标为?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 4*x )
M: Point
PointOnCurve(M, C) = True
F: Point
Focus(C) = F
Distance(M, F) = 4
```

Query list:
```
XCoordinate(M)
```

Answer list:
```
3
```


## Question 99
设$F_{1}$、$F_{2}$为双曲线$\frac{x^{2}}{a^{2}}-y^{2}=1$的两个焦点,点$P$在此双曲线上,$\overrightarrow{PF_{1}}\cdot\overrightarrow{PF_{2}}=0$,如果此双曲线的离心率等于$\frac{\sqrt{5}}{2}$,那么点$P$到$x$轴的距离等于?

Fact list:
```
C: Hyperbola
a: Number
Expression(C) = ( -y^2 + x^2/a^2 = 1 )
F1: Point
F2: Point
P: Point
PointOnCurve(P, C)
{F1, F2} = Focus(C)
DotProduct(VectorOf(P, F1), VectorOf(P, F2)) = 0
Eccentricity(C) = sqrt(5)/2
```

Query list:
```
Distance(P, xAxis)
```

Answer list:
```
sqrt(5)/5
```


## Question 100
下列关于圆锥曲线的命题:其中真命题的序号?(写出所有真命题的序号)。1设$A,B$为两个定点,若$|PA|-|PB|=2$,则动点$P$的轨迹为双曲线;2设$A,B$为两个定点,若动点$P$满足$|PA|=10-|PB|$,且$|AB|=6$,则$|PA|$的最大值为8;3方程$2x^{2}-5x+2=0$的两根可分别作椭圆和双曲线的离心率;4双曲线$\frac{x^{2}}{25}-\frac{y^{2}}{9}=1$与椭圆$x^{2}+\frac{y^{2}}{35}=1$有相同的焦点

Cannot annotate. Reason: 题型不符


## Question 101
设抛物线的顶点在原点,准线方程为$x=-2$,则抛物线的方程是?

Fact list:
```
C: Parabola
O: Origin
Vertex(C) = O
Expression(Directrix(C)) = (x = -2)
```

Query list:
```
Expression(C)
```

Answer list:
```
y^2 = 8*x
```


## Question 102
已知双曲线$\frac{x^{2}}{16}-\frac{y^{2}}{25}=1$的左焦点为$F_{1}$,点$P$为双曲线右支上一点,且$PF_{1}$与圆$x^{2}+y^{2}=16$相切于点$N$,$M$为线段$PF_{1}$的中点,$O$为坐标原点,则$|MN|-|MO|$=?

Fact list:
```
P: Point
F1: Point
C: Hyperbola
Expression(C) = ( x^2/16 - y^2/25 = 1 )
D: Circle
Expression(D) = ( x^2 + y^2 = 16 )
LeftFocus(C) = F1
PointOnCurve(P, RightPart(C)) = True
M,N : Point
TangencyPoint(LineSegmentOf(P, F1), D) = N
M = MidPoint(LineSegmentOf(P, F1))
O: Origin
```

Query list:
```
Abs(LineSegmentOf(M, N)) - Abs(LineSegmentOf(M, O))
```

Answer list:
```
-1
```


## Question 103
设$AB$是椭圆$\Gamma$的长轴,点$C$在$\Gamma$上,且$\angle CBA=\frac{\pi}{4}$,若$AB=4,BC=\sqrt{2}$,则$\Gamma$的两个焦点之间的距离为?

Fact list:
```
E: Ellipse
A, B, F1, F2: Point
MajorAxis(E) = LineSegmentOf(A, B)
C: Point
PointOnCurve(C, E) = True
AngleOf(C, B, A) = pi/4
{F1, F2} = Focus(E)
LineSegmentOf(A, B) = 4
LineSegmentOf(B, C) = sqrt(2)
```

Query list:
```
Distance(F1, F2)
```

Answer list:
```
4*sqrt(6)/3
```


## Question 104
抛物线$y^{2}=2px(p>0)$的焦点为$F$,$A$、$B$在抛物线上,且$\angle AFB=\frac{\pi}{2}$,弦$AB$的中点$M$在其准线上的射影为$N$,则$\frac{|MN|}{|AB|}$的最大值为?

Fact list:
```
C: Parabola
F, A, B, N, M: Point
p: Number
p > 0
Expression(C) = (y^2=2*p*x)
Focus(C) = F
PointOnCurve(A, C)
PointOnCurve(B, C)
AngleOf(A, F, B) = pi/2
IsChordOf(LineSegmentOf(A, B), C)
M = MidPoint(LineSegmentOf(A, B))
Projection(M, Directrix(C)) = N
```

Query list:
```
Max(Abs(LineSegmentOf(M, N))/Abs(LineSegmentOf(A, B)))
```

Answer list:
```
sqrt(2)/2
```


## Question 105
若抛物线$y^{2}=2px$的焦点坐标为$(1,0)$,则$p$=?;准线方程为?

Fact list:
```
p: Number
C: Parabola
Focus(C) = (1, 0)
Expression(C) = (y^2=2*p*x)
```

Query list:
```
p
Directrix(C)
```

Answer list:
```
2
x=-1
```


## Question 106
抛物线$y^{2}=-4x$的准线方程是?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = -4*x )
```

Query list:
```
Expression(Directrix(C))
```

Answer list:
```
x=1
```


## Question 107
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$与抛物线$y^{2}=8x$有一个公共的焦点$F$,且两曲线的一个交点为$P$,若$|PF|=5$,则双曲线的渐近线方程为?

Cannot annotate. Reason: 其他


## Question 108
双曲线$mx^{2}+y^{2}=1$的虚轴长是实轴长的$2$倍,则$m$等于?

Fact list:
```
C: Hyperbola
m: Number
Expression(C) = ( m*x^2 + y^2 = 1 )
Length(ImageinaryAxis(C)) = 2*Length(RealAxis(C))
```

Query list:
```
m
```

Answer list:
```
-1/4
```


## Question 109
已知椭圆的两焦点$F_{1}(-1,0),F_{2}(1,0),P$是椭圆上一点且$|F_{1}F_{2}|$是$|PF_{1}|$与$|PF_{2}|$的等差中项,则此椭圆的标准方程为?

Cannot annotate. Reason: 知识点不符


## Question 110
如右图,抛物线C:$y^{2}=2px(p>0)$的焦点为$F$,$A$为$C$上的点,以$F$为圆心,$\frac{P}{2}$为半径的圆与线段$AF$的交点为$B$,$\angle AFx=60°$,$A$在$y$轴上的射影为$N$,则$\angle ONB$=?

Cannot annotate. Reason: 题型不符


## Question 111
以$2x\pm 3y=0$为渐近线,且经过点$(1,2)$的双曲线标准方程是?

Fact list:
```
C: Hyperbola
P: Point
P = (1, 2)
PointOnCurve(P, C)
Asymptote(C) = (2*x+pm*3*y=0)
```

Query list:
```
Expression(C)
```

Answer list:
```
9*y^2/32 - x^2/8 = 1
```


## Question 112
已知椭圆$\frac{x^{2}}{6}+y^{2}=1$的左右焦点为$F_{1}$、$F_{2}$,直线$AB$过点$F_{1}$且交椭圆于$A$、$B$两点,则$\triangle ABF_{2}$的周长为?

Fact list:
```
C: Ellipse
Expression(C) = ( x^2/6 + y^2 = 1 )
F1, F2: Point
A, B: Point
F1 = LeftFocus(C)
F2 = RightFocus(C)
PointOnCurve(F1, LineOf(A,B))
{A,B} = Intersection(LineOf(A,B),C)
```

Query list:
```
Perimeter(TriangleOf(A,B,F2))
```

Answer list:
```
4*sqrt(6)
```


## Question 113
过点$M(-1,0)$的直线$l_{1}$与抛物线$y^{2}=4x$交于$P_{1},P_{2}$两点,记线段$P_{1}P_{2}$的中点为$P$,过点$P$和这个抛物线的焦点$F$的直线为$l_{2},l_{1}$的斜率为$k$,则直线$l_{2}$的斜率与直线$l_{1}$的斜率之比可表示为$k$的函数$f(k)=$?

Cannot annotate. Reason: 知识点不符


## Question 114
在直角坐标系$xOy$中,点$B$与点$A(-1,0)$关于原点$O$对称.点$P(x_{0},v_{0})$在抛物线$y^{2}=4x$上,且直线$AP$与$BP$的斜率之积等于$-2$,则$x_{0}=$?

Cannot annotate. Reason: 算子缺失


## Question 115
双曲线$\frac{x^{2}}{b^{2}}-\frac{y^{2}}{a^{2}}=1$的两条渐近线互相垂直,那么该双曲线的离心率是?

Fact list:
```
C: Hyperbola
a, b: Number
Expression(C) = ( x^2/b^2 - y^2/a^2 = 1 )
l1, l2: Line
Asymptote(C) = {l1, l2}
IsPerpendicular(l1, l2) = True
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(2)
```


## Question 116
若直线的极坐标方程为$\rho\cos(\theta-\frac{\pi}{4})=3\sqrt{2}$,曲线$C$:$\rho=1$上的点到直线的距离为$a$,则$a$的最大值为?

Cannot annotate. Reason: 知识点不符


## Question 117
若直线$x-y=2$与抛物线$y^{2}=4x$交于$A,B$两点,则线段$AB$的中点坐标是?

Fact list:
```
A: Point
B: Point
C: Parabola
Expression(C) = ( y^2 = 4*x )
D: Line
Expression(D) = ( x - y = 2 )
{A, B} = Intersection(C, D)
```

Query list:
```
Coordinate(MidPoint(LineSegmentOf(A, B)))
```

Answer list:
```
(4, 2)
```


## Question 118
点$A(2,3)$关于直线$x-y-1=0$的对称点$A^{\prime}$的坐标为?

Cannot annotate. Reason: 算子缺失


## Question 119
已知$AB$是过抛物线$y^{2}=2x$焦点的弦,$|AB|=4$,则$AB$中点的横坐标是?

Fact list:
```
C: Parabola
A, B: Point
Expression(C) = ( y^2 = 2*x )
Abs(LineSegmentOf(A, B))= 4
PointOnCurve(Focus(C), LineSegmentOf(A, B))
IsChordOf(LineSegmentOf(A, B), C)
```

Query list:
```
XCoordinate(MidPoint(LineSegmentOf(A, B)))
```

Answer list:
```
3
```


## Question 120
过抛物线$y^{2}=2px,(p>0)$焦点的直线与抛物线交于$A$、$B$两点,$|AB|=3$,且$AB$中点的纵坐标为$\frac{1}{2}$,则$p$的值为?

Fact list:
```
C: Parabola
p: Number
p>0
Expression(C) = ( y^2 = 2*(p*x) )
D: Line
PointOnCurve(Focus(C), D)
A, B: Point
{A, B} = Intersection(D, C)
Abs(LineSegmentOf(A, B)) = 3
YCoordinate(MidPoint(LineSegmentOf(A, B))) = 1/2
```

Query list:
```
p
```

Answer list:
```
{(3+sqrt(5))/4, (3-sqrt(5))/4}
```


## Question 121
抛物线$y^{2}=2px(p>0)$的焦点为$F$,过焦点$F$倾斜角为$30^{\circ}$的直线交抛物线于$A$,$B$两点,点$A,B$在抛物线准线上的射影分别是$A^{\prime},B^{\prime}$,若四边形$AA^{\prime}B^{\prime}B$的面积为$48$,则抛物线的方程为?

Cannot annotate. Reason: 算子缺失


## Question 122
已知椭圆$\frac{x^{2}}{16}+\frac{y^{2}}{12}=1$,则以点$M(-1,2)$为中点的弦所在直线方程为?

Fact list:
```
C: Ellipse
Expression(C) = ( x^2/16 + y^2/12 = 1 )
D: LineSegment
M: Point
Coordinate(M) = (-1, 2)
IsChordOf(D, C) = True
MidPoint(D) = M
```

Query list:
```
Expression(OverlappingLine(D))
```

Answer list:
```
3*x-8*y+19=0
```


## Question 123
已知双曲线$x^{2}-y^{2}=4$,直线$l:y=k(x-1)$与该双曲线只有一个公共点,则k=?(写出所有可能的取值)

Fact list:
```
C: Hyperbola
k: Number
Expression(C) = ( x^2 - y^2 = 4 )
l: Line
Expression(l) = ( y = k*(x - 1) )
NumIntersection(l, C) = 1
```

Query list:
```
k
```

Answer list:
```
{1, -1, 2*sqrt(3)/3, -2*sqrt(3)/3}
```


## Question 124
已知$F$是抛物线$C:y^{2}=4x$的焦点,$A,B$是$C$上的两个点,线段$AB$的中点为$M(2,2)$,则$\Delta ABF$的面积等于?

Fact list:
```
C: Parabola
F: Point
F = Focus(C)
Expression(C) = (y^2 = 4*x)
A,B: Point
PointOnCurve(A,C)
PointOnCurve(B,C)
M: Point
M = MidPoint(LineSegmentOf(A,B))
Coordinate(M) = (2,2)
```

Query list:
```
Area(TriangleOf(A,B,F))
```

Answer list:
```
2
```


## Question 125
椭圆$\left\{\begin{matrix}x=3\cos\theta\\y=4\sin\theta\\\end{matrix}\right.$($\theta$为参数)的离心率是?

Cannot annotate. Reason: 知识点不符


## Question 126
椭圆$\frac{x^{2}}{16}+\frac{y^{2}}{12}=1$上的点到直线$x-2y-12=0$的距离的最小值为?

Fact list:
```
C: Ellipse
Expression(C) = ( x^2/16 + y^2/12 = 1 )
D: Line
Expression(D) = ( x - 2*y - 12 = 0 )

A: Point
PointOnCurve(A, C) = True
```

Query list:
```
Min(Distance(A, D))
```

Answer list:
```
4/5 * sqrt(5)
```


## Question 127
在椭圆$\frac{x^{2}}{9}+\frac{y^{2}}{2}=1$的焦点为$F_{1},F_{2}$,点$P$在椭圆上,若$|PF_{1}|=4$,则$|PF_{2}|$=?，$\angle F_1PF_2$=?

Fact list:
```
C: Ellipse
Expression(C) = (x^2/9 + y^2/2 = 1)
F1, F2: Point
{F1, F2} = Focus(C)
p: Point
PointOnCurve(P, C) = True
Abs(LineSegmentOf(P, F1)) = 4
```

Query list:
```
Abs(LineSegmentOf(P, F2))
AngleOf(F1, P, F2)
```

Answer list:
```
2
2/3 * pi
```


## Question 128
若点$P(3,m)$在以点$F$为焦点的抛物线$\begin{matrix}x=4t^{2}\\y=4t\end{matrix}$上,则$|PF|$等于?

Cannot annotate. Reason: 知识点不符


## Question 129
曲线C的直角坐标方程为$x^{2}+y^{2}-2x=0$,以原点为极点,x轴的正半轴为极轴建立极坐标系,则曲线C的极坐标方程为?

Cannot annotate. Reason: 知识点不符


## Question 130
已知$F_1,F_2$是椭圆$C$的两个焦点,焦距为$4$.若$P$为椭圆$C$上一点,且$\Delta PF_{1}F_{2}$的周长为$14$,则椭圆$C$的离心率$e$为?

Fact list:
```
C: Ellipse
F1, F2: Point
{F1, F2} = Focus(C)
FocalLength(C) = 4
P: Point
PointOnCurve(P, C)
Perimeter(TriangleOf(P,F1,F2)) = 14
e: Number
Eccentricity(C) = e
```

Query list:
```
e
```

Answer list:
```
2/5
```


## Question 131
已知双曲线的方程为$\frac{x^{2}}{3}-y^{2}=1$,则此双曲线的焦点到渐近线的距离为?

Fact list:
```
C: Hyperbola
Expression(C) = (x^2/3-y^2=1)
```

Query list:
```
Distance(Focus(C), Asymptote(C))
```

Answer list:
```
1
```


## Question 132
椭圆$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$上的任意一点$M$(除短轴端点除外)与短轴两个端点$B_{1}$、$B_{2}$的连线交$x$轴于点$N$和$K$,则$|ON|+|OK|$的最小值是?

Fact list:
```
C: Ellipse
b, a: Number
a > b
b > 0
Expression(C) = ( y^2/b^2 + x^2/a^2 = 1 )
M, N, K, B1, B2: Point
PointOnCurve(M, C)
Negation(In(M, Endpoint(MinorAxis(C))))
{B1, B2} = Endpoint(MinorAxis(C))
N = Intersection(LineOf(M, B1), xAxis)
K = Intersection(LineOf(M, B2), xAxis)
```

Query list:
```
Min(Abs(LineSegmentOf(O, K)) + Abs(LineSegmentOf(O, N)))
```

Answer list:
```
2a
```


## Question 133
对于抛物线$y^{2}=4x$上任意一点$Q$,点$P(a,0)$都满足$|PQ|\geq|a|$,则$a$的取值范围是?

Cannot annotate. Reason: 其他


## Question 134
在平面直角坐标系$xOy$中,已知$ABC$顶点$A(-4,0)$和$C(4,0)$,顶点B在椭圆$\frac{x^{2}}{25}+\frac{y^{2}}{9}=1$上,则$\frac{\sin A+\sin C}{\sin B}=$?

Cannot annotate. Reason: 其他


## Question 135
已知抛物线$C:y^{2}=8x$的焦点为$F$,准线与$x$轴的交点为$K$,点$A$在$C$上且$|AK|=\sqrt{2}|AF|$,则$\Delta AFK$的面积为?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 8*x )
F: Point
Focus(C) = F
A, K: Point
Intersection(Directrix(C), xAxis) = K
PointOnCurve(A, C)
Abs(LineSegmentOf(A, K)) = sqrt(2)*Abs(LineSegmentOf(A, F))
```

Query list:
```
Area(TriangleOf(A, F, K))
```

Answer list:
```
8
```


## Question 136
$F$是椭圆$C:\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$的右焦点,定点A$(-1,1)$,$M$是椭圆上的动点,则$\frac{1}{2}|MA|+|MF|$的最小值?

Fact list:
```
C: Ellipse
F: Point
Expression(C) = (x^2/4+y^2/3=1)
F = RightFocus(C)
A: Point
Coordinate(A) = (-1,1)
M: Point
PointOnCurve(M, C)
```

Query list:
```
Min(1/2*Abs(LineSegmentOf(M,A)) + Abs(LineSegmentOf(M,F)))
```

Answer list:
```
5/2
```


## Question 137
过椭圆$4x^{2}+2y^{2}=1$的一个焦点$F_{1}$的直线与椭圆交于$A$、$B$两点,则$A$、$B$与椭圆的另一焦点$F_{2}$构成$\Delta ABF_{2}$,那么$\Delta ABF_{2}$的周长是?

Fact list:
```
C: Ellipse
Expression(C) = ( 4*x^2 + 2*y^2 = 1 )
F1: Point
In(F1, Focus(C))
L: Line
PointOnCurve(F1, L)
A,B: Point
{A,B} = Intersection(L, C)
F2: Point
In(F2, Focus(C))
Negation(F1=F2)
```

Query list:
```
Perimeter(TriangleOf(A,B,F2))
```

Answer list:
```
2*sqrt(2)
```


## Question 138
若椭圆的两个焦点与它的短轴的两个端点是一个正方形的四个顶点,则椭圆的离心率为?

Cannot annotate. Reason: 算子缺失


## Question 139
(1)已知$y=\frac{1}{x}$的图象为双曲线,在双曲线的两支上分别取点$P$、$Q$,则线段$PQ$的最小值为?

Cannot annotate. Reason: 算子缺失


## Question 140
长为$3$的线段$AB$的端点$A$、$B$分别在$x$、$y$轴上移动,动点$C(x,y)$满足$\overrightarrow{AC}=2\overrightarrow{CB}$,则动点$C$的轨迹方程是.

Fact list:
```
A, B, C: Point
Length(LineSegmentOf(A, B)) = 3
Endpoint(LineSegmentOf(A, B)) = {A, B}
PointOnCurve(A, xAxis)
PointOnCurve(B, yAxis)
x, y: Number
Coordinate(C) = (x, y)
VectorOf(A, C) = 2 * VectorOf(C, B)
```

Query list:
```
LocusEquation(C)
```

Answer list:
```
x^2 + y^2/4 = 1
```


## Question 141
与双曲线$x^{2}-4y^{2}=4$有共同的渐近线,且经过点$(2,\sqrt{5})$的双曲线方程是.

Fact list:
```
C, D: Hyperbola
 Expression(C) = (x^2 - 4*y^2=4)
 P: Point
 Asymptote(C) = Asymptote(D)
 PointOnCurve(P, D)
 Coordinate(P) = (2, sqrt(5))
```

Query list:
```
Expression(D)
```

Answer list:
```
y^2/4-x^2/16=1
```


## Question 142
过抛物线$y^{2}=4x$的焦点作直线$l$交抛物线于$A,B$两点,若线段$AB$中点的横坐标为$3$,则$|AB|$等于.

Fact list:
```
A: Point
B: Point
l: Line
C: Parabola
Expression(C) = ( y^2 = 4*x )
PointOnCurve(Focus(C), l)
{A,B} = Intersection(C, l)
XCoordinate(MidPoint(LineSegmentOf(A,B))) = 3
```

Query list:
```
Abs(LineSegmentOf(A,B))
```

Answer list:
```
8
```


## Question 143
椭圆$ax^2+by^2+ab=0(a<b<0)$的焦点坐标是?

Fact list:
```
C: Ellipse
a, b: Number
a < b
b < 0
Expression(C) = ( a*b + a*x^2 + b*y^2 = 0 )
```

Query list:
```
Coordinate(Focus(C))
```

Answer list:
```
{(0,sqrt(b-a)),(0,-sqrt(b-a))}
```


## Question 144
椭圆的一个顶点与两个焦点构成等边三角形,则离心率$e$=?

Cannot annotate. Reason: 算子缺失


## Question 145
如果方程$x^{2}+ky^{2}=2$表示焦点在$y$轴的椭圆,那么实数$k$的取值范围是?

Fact list:
```
C: Ellipse
k: Real
Expression(C) = (x^2 + k*y^2 = 2)
PointOnCurve(Focus(C), yAxis) = True
```

Query list:
```
Range(k)
```

Answer list:
```
(0, 1)
```


## Question 146
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的一条渐近线方程是$y=\sqrt{3}x$,它的一个焦点在抛物线$y^{2}=8x$的准线上,则双曲线的方程为?

Fact list:
```
C: Hyperbola
b, a: Number
a>0
b>0
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
Expression(OneOf(Asymptote(C))) = (y = sqrt(3)*x)
D: Parabola
Expression(D) = ( y^2 = 8*x )
PointOnCurve(OneOf(Focus(C)), Directrix(D)) = True
```

Query list:
```
Expression(C)
```

Answer list:
```
x^2-y^2/3=1
```


## Question 147
方程$\frac{x^{2}}{a}+\frac{y^{2}}{b}=1(a,b\in\{1,2,3,4,\dots,2013\})$的曲线中,所有圆面积的和等于?

Cannot annotate. Reason: 其他


## Question 148
过椭圆$\frac{x^{2}}{9}+\frac{y^{2}}{5}=1$左焦点$F$且不垂直于$x$轴的直线交椭圆与$A$、$B$两点,$AB$的垂直平分线交$x$轴于点$N$,则$\frac{|NF|}{|AB|}$=?

Fact list:
```
C: Ellipse
Expression(C) = (x^2/9 + y^2/5 = 1)
N, F, A, B: Point
F = LeftFocus(C)
l: Line
PointOnCurve(F, l)
Negation(IsPerpendicular(l, xAxis))
Intersection(l, C) = {A, B}
Intersection(PerpendicularBisector(LineSegmentOf(A, B)), xAxis) = N
```

Query list:
```
Abs(LineSegmentOf(N, F))/Abs(LineSegmentOf(A,B))
```

Answer list:
```
1/3
```


## Question 149
已知点$P(x,y)$是抛物线$y^{2}=-12x$的准线与双曲线$\frac{x^{2}}{6}-\frac{y^{2}}{2}=1$的两条渐近线所围成的三角形平面区域内(含边界)的任意一点,则$z=2x-y$的最大值为?

Cannot annotate. Reason: 算子缺失


## Question 150
双曲线虚轴的一个端点为$M$,两个焦点为$F_{1},F_{2}$,$\angle F_{1}MF_{2}=120^{\circ}$,则双曲线的离心率为?

Fact list:
```
C: Hyperbola
M, F1, F2: Point
{F1, F2} = Focus(C)
M = OneOf(Endpoint(ImageinaryAxis(C)))
AngleOf(F1, M, F2) = ApplyUnit(120, degree)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(6)/2
```


## Question 151
已知点$P$到点$F(-3,0)$的距离比它到直线$x=2$的距离大$1$,则点$P$满足的方程为?

Fact list:
```
P, F: Point
l: Line
Expression(l) = (x=2)
Coordinate(F) = (-3, 0)
Distance(P, F) = Distance(P, l) +1
```

Query list:
```
LocusEquation(P)
```

Answer list:
```
y^2=-12*x
```


## Question 152
直线$y=x+3$与曲线$\frac{y^{2}}{9}-\frac{x|x|}{4}=1$的交点的个数是?个.

Fact list:
```
C: Line
Expression(C) = ( y = x + 3 )
D: Curve
Expression(D) = ( -x*Abs(x)/4 + y^2/9 = 1 )
```

Query list:
```
NumIntersection(C, D)
```

Answer list:
```
3
```


## Question 153
直线$(m+1)x+(2m-1)y-2m+1=0$经过的定点的坐标是?

Cannot annotate. Reason: 算子缺失


## Question 154
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的左右顶点分别是$A$、$B$,点$P$是双曲线上异于点$A$、$B$的任意一点。若直线$PA$、$PB$的斜率之积等于$2$,则该双曲线的离心率等于?

Fact list:
```
P: Point
A: Point
B: Point
C: Hyperbola
b, a: Number
a>0
b>0
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
LeftVertex(C) = A
RightVertex(C) = B 
PointOnCurve(P, C)
Negation(Eq(P,A))
Negation(Eq(P,B))
Slope(LineOf(P,A))*Slope(LineOf(P,B)) = 2
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(3)
```


## Question 155
设椭圆$\frac{x^{2}}{6}+\frac{y^{2}}{2}=1$和双曲线$\frac{x^{2}}{2}-\frac{y^{2}}{2}=1$的公共焦点为$F_{1}$、$F_{2}$,$P$是两曲线的一个交点,则$\angle F_{1}PF_{2}$=?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/2 - y^2/2 = 1 )
D: Ellipse
Expression(D) = ( x^2/6 + y^2/2 = 1 )
F1, F2: Point
{F1, F2} = Focus(C)
{F1, F2} = Focus(D)
P: Point
P = OneOf(Intersection(C,D))
```

Query list:
```
AngleOf(F1,P,F2)
```

Answer list:
```
ApplyUnit(90,degree)
```


## Question 156
已知曲线$C:x^{2}+y^{2}=m$恰有三个点到直线$12x+5y+26=0$距离为$1$,则$m$=?

Cannot annotate. Reason: 其他


## Question 157
以椭圆$\frac{x^{2}}{9}+\frac{y^{2}}{5}=1$的中心为顶点,右焦点为焦点的抛物线方程是?

Fact list:
```
C: Parabola
D: Ellipse
Expression(D) = ( x^2/9 + y^2/5 = 1 )
Vertex(C) = Center(D)
Focus(C) = RightFocus(D)
```

Query list:
```
Expression(C)
```

Answer list:
```
(y^2 = 8*x)
```


## Question 158
已知经过抛物线$y^{2}=4x$的焦点$F$的直线交抛物线于$A$、$B$两点,满足$|AF|=3|FB|$,则弦$AB$的中点到准线的距离为?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 4*x )
D: Line
F: Point
Focus(C) = F
PointOnCurve(F, D) = True
A, B: Point
Intersection(D, C) = {A, B}
Abs(LineSegmentOf(A, F)) = 3*Abs(LineSegmentOf(F, B))
IsChordOf(LineSegmentOf(A, B), C) = True
```

Query list:
```
Distance(MidPoint(LineSegmentOf(A, B)), Directrix(C))
```

Answer list:
```
8/3
```


## Question 159
抛物线$y^{2}=4x$上一点$M$到焦点的距离为$3$,则点$M$的横坐标是?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 4*x )
M: Point
PointOnCurve(M, C)
Distance(M, Focus(C)) = 3
```

Query list:
```
XCoordinate(M)
```

Answer list:
```
2
```


## Question 160
若双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$的一条渐近线方程为$x+3y=0$,则此双曲线的离心率为?

Fact list:
```
C: Hyperbola
b, a: Number
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
Expression(OneOf(Asymptote(C))) = (x+3*y=0)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(10)/3
```


## Question 161
已知椭圆的长轴长是短轴长的$\sqrt{2}$倍,则椭圆的离心率等于?

Fact list:
```
C: Ellipse
Length(MajorAxis(C)) = sqrt(2) * Length(MinorAxis(C))
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(2)/2
```


## Question 162
已知椭圆的方程是$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{25}=1(a>5)$,它的两个焦点分别为$F_{1}$、$F_{2}$,且$|F_{1}F_{2}|=8$,弦$AB$(椭圆上任意两点的线段)过点$F_1$,则$\triangle ABF_2$的周长为?

Fact list:
```
C: Ellipse
a: Number
a > 5
Expression(C) = (x^2/a^2 + y^2/25=1)
F1,F2,A,B: Point
{F1, F2} = Focus(C)
Abs(LineSegmentOf(F1, F2)) = 8
IsChordOf(LineSegmentOf(A, B), C)
PointOnCurve(F1, LineSegmentOf(A, B))
```

Query list:
```
Perimeter(TriangleOf(A, B, F2))
```

Answer list:
```
4*sqrt(41)
```


## Question 163
如图,把椭圆$\frac{x^{2}}{25}+\frac{y^{2}}{16}=1$的长轴$AB$分成$8$等份,过每个分点作$x$轴的垂线交椭圆的上半部分于$P_{1},P_{2},P_{3},P_{4},P_{5},P_{6},P_{7}$七个点,$F$是椭圆的一个焦点,则$|P_{1}F|+|P_{2}F|+|P_{3}F|+|P_{4}F|+|P_{5}F|+|P_{6}F|+|P_{7}F|$=?

Cannot annotate. Reason: 算子缺失


## Question 164
若抛物线$y^{2}=4x$上一点$P(x_{0},y_{0})$到其焦点$F$的距离等于$4$,则$x_{0}$=?

Fact list:
```
C: Parabola
Expression(C) = (y^2 = 4*x)
P: Point
x0, y0: Number
Coordinate(P) = (x0, y0)
PointOnCurve(P, C) = True
F: Point
F = Focus(C)
Distance(P, F) = 4
```

Query list:
```
x0
```

Answer list:
```
3
```


## Question 165
若双曲线$\frac{x^{2}}{m}-\frac{y^{2}}{4}=1$的右焦点与抛物线$y^{2}=12x$的焦点重合,则$m$=?

Fact list:
```
C: Hyperbola
m: Number
Expression(C) = ( -y^2/4 + x^2/m = 1 )
D: Parabola
Expression(D) = ( y^2 = 12*x )
RightFocus(C) = Focus(D)
```

Query list:
```
m
```

Answer list:
```
5
```


## Question 166
过点$P(3,2)$且与双曲线$\frac{x^{2}}{4}-\frac{y^{2}}{2}=1$有相同渐近线方程的双曲线的标准方程为?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/4 - y^2/2 = 1 )
P: Point
Coordinate(P) = (3, 2)
Hyperbola_1: Hyperbola
PointOnCurve(P, Hyperbola_1)
Expression(Asymptote(Hyperbola_1)) = Expression(Asymptote(C))
```

Query list:
```
Expression(Hyperbola_1)
```

Answer list:
```
x^2 - y^2/(1/2) = 1
```


## Question 167
已知$F_{1}(0,-2),F_{2}(0,2)$为椭圆的两个焦点,过$F_{2}$作椭圆的弦$AB$,若$\Delta AF_{1}B$的周长为$16$,则该椭圆的标准方程为?

Fact list:
```
C: Ellipse
F1, F2, A, B: Point
Coordinate(F1) = (0,-2)
Coordinate(F2) = (0,2)
{F1, F2} = Focus(C)
PointOnCurve(F2, LineSegmentOf(A,B))
IsChordOf(LineSegmentOf(A,B),C)
Perimeter(TriangleOf(A,F1,B)) = 16
```

Query list:
```
Expression(C)
```

Answer list:
```
y^2/16+x^2/12=1
```


## Question 168
已知焦点在$x$轴上的双曲线的渐近线方程为$y=\pm\frac{3}{4}x$,则此双曲线的离心率为?

Fact list:
```
C: Hyperbola
PointOnCurve(Focus(C), xAxis)
Expression(Asymptote(C)) = (y=pm*3/4*x)
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
5/4
```


## Question 169
已知$F_{1}$、$F_{2}$为椭圆$\frac{x^{2}}{25}+\frac{y^{2}}{9}=1$的两个焦点,过$F_{1}$的直线交椭圆于$A$、$B$两点。若$|F_{2}A|+|F_{2}B|=12$,则$|AB|$=?

Fact list:
```
C: Ellipse
Expression(C) = (x^2/25 + y^2/9 = 1)
D: Line
F1, F2: Point
Focus(C) = {F1, F2}
PointOnCurve(F1, D) = True
A, B: Point
Intersection(D, C) = {A, B}
Abs(LineSegmentOf(F2, A)) + Abs(LineSegmentOf(F2, B)) = 12
```

Query list:
```
Abs(LineSegmentOf(A, B))
```

Answer list:
```
8
```


## Question 170
已知双曲线$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1(a>0,b>0)$的一条渐近线经过点$(4,4\sqrt{3})$,则该双曲线的离心率为?

Fact list:
```
C: Hyperbola
a, b: Number
a>0
b>0
Expression(C) = (x^2/a^2-y^2/b^2 = 1)
P: Point
PointOnCurve(P, OneOf(Asymptote(C)))
Coordinate(P) = (4, 4*sqrt(3))
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
2
```


## Question 171
已知$F$是抛物线$C:y^{2}=4x$的焦点,过$F$且斜率为$\sqrt{3}$的直线交$C$于$A$、$B$两点.设$|FA|>|FB|$,则$\frac{|FA|}{|FB|}$的值等于?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 4*x )
L: Line
F, A, B: Point
F = Focus(C)
PointOnCurve(F, L)
Slope(L) = sqrt(3)
{A, B} = Intersection(L, C)
Abs(LineSegmentOf(F, A))>Abs(LineSegmentOf(F, B))
```

Query list:
```
Abs(LineSegmentOf(F, A))/Abs(LineSegmentOf(F, B))
```

Answer list:
```
3
```


## Question 172
从双曲线$\frac{x^{2}}{3}-\frac{y^{2}}{5}=1$的左焦点$F$引圆$x^{2}+y^{2}=3$的切线$FP$交双曲线右支于点$P$,$T$为切点,$M$为线段$FP$的中点,$O$为坐标原点,则$|MO|-|MT|$=?

Fact list:
```
C: Hyperbola
Expression(C) = (x^2/3-y^2/5=1)
F: Point
F = LeftFocus(C)
E: Circle
Expression(E) = (x^2+y^2=3)
P,T: Point
TangentOfPoint(F, E) = LineOf(F,P)
Intersection(RightPart(C), LineOf(F,P)) = P
T = TangencyPoint(LineOf(F,P),E)
M: Point
M = MidPoint(LineSegmentOf(F,P))
O: Origin
```

Query list:
```
Abs(LineSegmentOf(M,O))-Abs(LineSegmentOf(M,T))
```

Answer list:
```
sqrt(5)-sqrt(3)
```


## Question 173
若抛物线$y^2=2px$的焦点与双曲线$x^2/6-y^2/3=1$的右焦点重合,则$p$的值为？

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/6 - y^2/3 = 1 )
D: Parabola
p: Number
Expression(D) = ( y^2 = 2*(p*x) )
Focus(D) = RightFocus(C)
```

Query list:
```
p
```

Answer list:
```
6
```


## Question 174
椭圆$\frac{x^{2}}{9}+\frac{y^{2}}{2}=1$的焦点为$F_{1}$、$F_{2}$,点$P$在椭圆上,若$|PF_{1}|=4$,$\angle F_{1}PF_{2}$的大小为?

Fact list:
```
C: Ellipse
Expression(C) = ( x^2/9 + y^2/2 = 1 )
F1, F2, P: Point
Focus(C) = {F1, F2}
PointOnCurve(P, C)
Abs(LineSegmentOf(P, F1)) = 4
```

Query list:
```
AngleOf(F1, P, F2)
```

Answer list:
```
ApplyUnit(120, degree)
```


## Question 175
若抛物线$y^{2}=2px(p>0)$的焦点在圆$x^{2}+y^{2}+2x-3=0$上,则$p$=?

Fact list:
```
C: Parabola
D: Circle
p : Number
Expression(C) = (y^2 = 2*p*x)
p > 0
Expression(D) = (x^2 + y^2 + 2*x -3 =0)
PointOnCurve(Focus(C), D)
```

Query list:
```
p
```

Answer list:
```
2
```


## Question 176
在$Rt\Delta ABC$中,$AB=AC=1$,以点$C$为一个焦点作一个椭圆,使这个椭圆.的另一焦点在$AB$边上,且这个椭圆过$A$、$B$两点,则这个椭圆的焦距长为?

Cannot annotate. Reason: 算子缺失


## Question 177
已知F是抛物线$y^{2}=4x$的焦点,$A$、$B$是抛物线上两点,若$\Delta AFB$是正三角形,则$\Delta AFB$的边长为?

Cannot annotate. Reason: 算子缺失


## Question 178
若正三角形的一个顶点在原点,另两个顶点在抛物线$y^{2}=12x$上,则这个三角形的面积为?

Cannot annotate. Reason: 算子缺失


## Question 179
椭圆的离心率等于$\frac{\sqrt{3}}{3}$,且与双曲线$\frac{x^{2}}{16}-\frac{y^{2}}{9}=1$有相同的焦距,则椭圆的标准方程为?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/16 - y^2/9 = 1 )
D: Ellipse
Eccentricity(D) = sqrt(3)/3
FocalLength(C) = FocalLength(D)
```

Query list:
```
Expression(D)
```

Answer list:
```
{(x^2/75+y^2/50=1), (y^2/75+x^2/50=1)}
```


## Question 180
双曲线的实轴长、虚轴长与焦距的和为$8$,则半焦距的取值范围是?(答案用区间表示)

Fact list:
```
C: Hyperbola
Length(RealAxis(C))+Length(ImageinaryAxis(C))+FocalLength(C)=8
```

Query list:
```
Range(HalfFocalLength(C))
```

Answer list:
```
[4*sqrt(2)-4,2)
```


## Question 181
一双曲线与椭圆$\frac{x^{2}}{27}+\frac{y^{2}}{36}=1$有共同焦点,并且与其中一个交点的纵坐标为$4$,则这个双曲线的方程为?

Fact list:
```
C: Hyperbola
D: Ellipse
Expression(D) = ( x^2/27 + y^2/36 = 1 )
Focus(C) = Focus(D)
YCoordinate(OneOf(Intersection(C,D))) = 4
```

Query list:
```
Expression(C)
```

Answer list:
```
(-x^2/5 +y^2/4 = 1)
```


## Question 182
双曲线$\frac{x^{2}}{9}-\frac{y^{2}}{16}=1$上有一点$P$到左准线的距离为$\frac{16}{5}$,则$P$到右焦点的距离为?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/9 - y^2/16 = 1 )
P: Point
PointOnCurve(P, C)
Distance(P, LeftDirectrix(C)) = 16/5
```

Query list:
```
Distance(P, RightFocus(C))
```

Answer list:
```
34/3
```


## Question 183
已知直线$ax+y+2=0$与双曲线$x^{2}-\frac{y^{2}}{4}=1$的一条渐近线平行,则这两条平行直线之间的距离是?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2 - y^2/4 = 1 )
D: Line
a: Number
Expression(D) = ( a*x + y + 2 = 0 )
IsParallel(L,OneOf(Asymptote(C)))
```

Query list:
```
Distance(L,D)
```

Answer list:
```
2*sqrt(5)/5
```


## Question 184
已知点$P$是抛物线$y^{2}=2x$上的动点,点$P$在$y$轴上的射影是$M$,$A(\frac{7}{2},4)$,则$|PA|+|PM|$的最小值是?

Fact list:
```
P, M, A: Point
C: Parabola
Expression(C) = (y^2=2*x)
PointOnCurve(P, C)
Projection(P, yAxis) = M
Coordinate(A) = (7/2,4)
```

Query list:
```
Min(LineSegmentOf(P, A) + LineSegmentOf(P, M))
```

Answer list:
```
9/2
```


## Question 185
已知点$Q(2\sqrt{2},0)$及抛物线$y=\frac{x^{2}}{4}$上的动点$P(x,y)$,则$y+|PQ|$的最小值为?

Fact list:
```
C: Parabola
Expression(C) = ( y = x^2/4 )
Q: Point
Coordinate(Q) = (2*sqrt(2), 0)
P: Point
PointOnCurve(P, C) = True
Coordinate(P) = (x, y)
```

Query list:
```
Min(y + Abs(LineSegmentOf(P, Q)))
```

Answer list:
```
2
```


## Question 186
若双曲线$\frac{y^{2}}{5}-\frac{x^{2}}{m}=1$的离心率$e\in(1,2)$,则$m$的取值范围为?

Fact list:
```
C: Hyperbola
m: Number
Expression(C) = ( y^2/5 - x^2/m = 1 )
e: Number
Eccentricity(C) = e
In(e, (1, 2)) = True
```

Query list:
```
Range(m)
```

Answer list:
```
(0, 15)
```


## Question 187
直线$y=x$被曲线$2x^{2}+y^{2}=2$截得的弦长为?

Fact list:
```
L: Line
Expression(L) = (y=x)
C: Curve
Expression(C) = (2*x^2 + y^2 = 2)
```

Query list:
```
Length(InterceptChord(L, C))
```

Answer list:
```
4*sqrt(3)/3
```


## Question 188
若点$P$到点$F(4,0)$的距离比它到直线$x+5=0$的距离少$1$,则动点$P$的轨迹方程是?

Fact list:
```
P, F: Point
l: Line
Expression(l) = (x+5=0)
Coordinate(F) = (4, 0)
Distance(P, F) = Distance(P, l) - 1
```

Query list:
```
LocusEquation(P)
```

Answer list:
```
y^2 = 16*x
```


## Question 189
焦点在$y$轴上,虚轴长为$8$,焦距为$10$的双曲线的标准方程是?

Fact list:
```
C: Hyperbola
PointOnCurve(Focus(C),xAxis)
Length(ImageinaryAxis(C)=8)
FocalLength(C)=10
```

Query list:
```
Expression(C)
```

Answer list:
```
y^2/9 - x^2/16 = 1
```


## Question 190
平面$\alpha,\beta,\gamma$两两垂直,定点$A\in \alpha$,A到$\beta,\gamma$距离都是1,P是$\alpha$上动点,P到$\beta$的距离等于P到点$A$的距离,则P点轨迹上的点到$\beta$距离的最小值是?

Cannot annotate. Reason: 知识点不符


## Question 191
若椭圆长轴长与短轴长之比为$2$,它的一个焦点是$(2\sqrt{15},0)$,则椭圆的标准方程是?

Cannot annotate. Reason: 算子缺失


## Question 192
若抛物线$y^{2}=2px$的焦点与双曲线$\frac{x^{2}}{3}-y^{2}=1$的左焦点重合,则实数$p$=?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/3 - y^2 = 1 )
D: Parabola
p: Real
Expression(D) = ( y^2 = 2*(p*x) )
Focus(D) = LeftFocus(C)
```

Query list:
```
p
```

Answer list:
```
-4
```


## Question 193
椭圆$\frac{x^{2}}{4}+\frac{y^{2}}{3}=1$的左、右焦点为$F_{1}$、$F_{2}$,直线$x=m$过$F_{2}$且与椭圆相交于$A,B$两点,则$\Delta F_{1}AB$的面积等于?

Fact list:
```
L: Line
C: Ellipse
Expression(C) = ( x^2/4 + y^2/3 = 1 )
F1: Point
F2: Point
LeftFocus(C) = F1
RightFocus(C) = F2
m: Number
Expression(L) = (x=m)
A, B: Point
PointOnCurve(F2, L)
Intersection(L, C) = {A, B}
```

Query list:
```
Area(TriangleOf(F1, A, B))
```

Answer list:
```
3
```


## Question 194
已知$A$、$B$、$C$是椭圆$\frac{x^{2}}{25}+\frac{y^{2}}{16}=1$上的三点,点$F(3,0)$,若$\overrightarrow{FA}+\overrightarrow{FB}+\overrightarrow{FC}=\overrightarrow{0}$,则$|\overrightarrow{FA}|+|\overrightarrow{FB}|+|\overrightarrow{FC}|$=?

Fact list:
```
A,B,C,F:Point
E:Ellipse
Expression(E)=(x^2/25+y^2/16=1)
PointOnCurve(A,E)
PointOnCurve(B,E)
PointOnCurve(A,E)
Coordinate(F)=(3,0)
VectorOf(F,A)+VectorOf(F,B)+VectorOf(F,C)=0
```

Query list:
```
Abs(VectorOf(F,A))+Abs(VectorOf(F,B))+Abs(VectorOf(F,C))
```

Answer list:
```
48/5
```


## Question 195
设AB是平面$a$的斜线段,$A$为斜足,若点$P$在平面$a$内运动,使得△ABP的面积为定值,则动点P的轨迹是?

Cannot annotate. Reason: 题型不符


## Question 196
在平面直角坐标系$xOy$中,对于任意两点$P_{1}(x_{1},y_{1})$与$P_{2}(x_{2},y_{2})$的“非常距离”给出如下定义:若$|x_{1}-x_{2}|\ge|y_{1}-y_{2}|$,则点$P_{1}$与点$P_{2}$的“非常距离”为$|x_{1}-x_{2}|$,若$|x_{1}-x_{2}|<|y_{1}-y_{2}|$,则点$P_{1}$与点$P_{2}$的“非常距离”为$|y_{1}-y_{2}|$.已知$C$是直线$y=\frac{3}{4}x+3$上的一个动点,点$D$的坐标是(0,1),则点$C$与点$D$的“非常距离”的最小值是?

Cannot annotate. Reason: 题型不符


## Question 197
设点$P$在曲线$y=x^{2}+2$上,点$Q$在曲线$y=\sqrt{x-2}$上,则$|PQ|$的最小值等于?

Fact list:
```
C1, C2: Curve
Expression(C1) = ( y = x^2 + 2 )
P: Point
PointOnCurve(P, C1) = True
Expression(C2) = ( y = sqrt(x - 2) )
Q: Point
PointOnCurve(Q, C2) = True
```

Query list:
```
Min(Abs(LineSegmentOf(P, Q)))
```

Answer list:
```
7*sqrt(2)/4
```


## Question 198
双曲线$\frac{x^{2}}{3}-y^{2}=1$的两条渐近线的夹角大小等于?

Cannot annotate. Reason: 算子缺失


## Question 199
椭圆$\frac{x^{2}}{4a^{2}}+\frac{y^{2}}{3a^{2}}=1(a>0)$的左焦点为$F$,直线$x=m$与椭圆相交于点$A$、$B$,当$\Delta FAB$的周长最大时,$\Delta FAB$的面积是?

Cannot annotate. Reason: None


## Question 200
等轴双曲线$C$的中心在原点,焦点在$x$轴上,$C$与抛物线$y^{2}=16x$的准线交于$A$、$B$两点,$|AB|=4\sqrt{3}$;则$C$的实轴长为?

Cannot annotate. Reason: 算子缺失


## Question 201
已知直线$y=k(x-2)$$(k>0)$与抛物线$y^{2}=8x$相交于$A$、$B$两点,$F$为抛物线的焦点,若$|FA|=2|FB|$,则$k$的值为?

Fact list:
```
l: Line
k: Number
k > 0
Expression(l) = (y = k*(x-2))
C: Parabola
Expression(C) = (y^2 = 8*x)
A, B: Point
Intersection(l, C) = {A, B}
F: Point
Focus(C) = F
Abs(LineSegmentOf(F, A)) = 2*Abs(LineSegmentOf(F, B))
```

Query list:
```
k
```

Answer list:
```
2*sqrt(2)
```


## Question 202
如图,椭圆的中心在坐标原点,$F$为左焦点,当$\overrightarrow{FB}\bot\overrightarrow{AB}$时,其离心率为$\frac{\sqrt{5}-1}{2}$,此类椭圆称为“黄金椭圆”,类比“黄金椭圆”,可推出“黄金双曲线”的离心率为?

Cannot annotate. Reason: 新定义问题


## Question 203
设$M(-5,0)$、$N(5,0)$,$\triangle MNP$的周长是$36$,则$\Delta MNP$的顶点$P$的轨迹方程为?

Fact list:
```
M, N, P: Point
Coordinate(M) = (-5, 0)
Coordinate(N) = (5, 0)
Perimeter(TriangleOf(M,N,P)) = 36
```

Query list:
```
LocusEquation(P)
```

Answer list:
```
x^2/169 + y^2/144 = 1 (y!=0)
```


## Question 204
已知点$P$为抛物线$y^{2}=4x$上一点,记点$P$到$y$轴距离$d_{1}$,点$P$到直线$l:3x-4y+12=0$的距离$d_{2}$,则$d_{1}+d_{2}$的最小值为?

Fact list:
```
C: Parabola
Expression(C) = ( y^2 = 4*x )
l: Line
Expression(l) = ( 3*x - 4*y + 12 = 0 )
P:Point
d1,d2:Number
PointOnCurve(P,C)
Distance(P,yAxis)=d1
Distance(P,l)=d2
```

Query list:
```
Min(d1 + d2)
```

Answer list:
```
2
```


## Question 205
若曲线$\frac{x^{2}}{4+k}+\frac{y^{2}}{1-k}=1$表示双曲线,则$k$的取值范围是?

Fact list:
```
C: Hyperbola
k: Number
Expression(C) = ( x^2/(k + 4) + y^2/(1 - k) = 1 )
```

Query list:
```
Range(k)
```

Answer list:
```
(-oo,-4)+(1,+oo)
```


## Question 206
双曲线:$\frac{y^{2}}{4}-x^{2}=1$的渐近线方程是?

Fact list:
```
C: Hyperbola
Expression(C) = ( -x^2 + y^2/4 = 1 )
```

Query list:
```
Expression(Asymptote(C))
```

Answer list:
```
y=pm*2*x
```


## Question 207
已知平面$\alpha$经过点$A(1,1,1)$,且$\overrightarrow{n}=(1,2,3)$是它的一个法向量.类比曲线方程的定义以及求曲线方程的基本步骤,可求得平面$\alpha$的方程是?

Cannot annotate. Reason: 知识点不符


## Question 208
点$P$在双曲线$x^{2}-y^{2}=1$上运动,$O$为坐标原点,线段$PO$中点$M$的轨迹方程是?

Fact list:
```
O: Origin
P: Point
C: Hyperbola
PointOnCurve(P, C)
Expression(C) = (x^2-y^2=1)
M = MidPoint(LineSegmentOf(P, O))
```

Query list:
```
LocusEquation(P)
```

Answer list:
```
4*x^2-4*y^2=1
```


## Question 209
在平面直角坐标系$xOy$中,双曲线$y^{2}-x^{2}=1$的离心率为?

Fact list:
```
C: Hyperbola
Expression(C) = ( -x^2 + y^2 = 1 )
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
sqrt(2)
```


## Question 210
中心在原点,焦点在$x$轴上,若长轴长为$18$,且两个焦点恰好将长轴三等分,则此椭圆的标准方程为?

Cannot annotate. Reason: 算子缺失


## Question 211
过椭圆$\frac{x^{2}}{5}+\frac{y^{2}}{4}=1$的右焦点作一条斜率为$2$的直线与椭圆交于$A$、$B$两点,$O$为坐标原点,求弦$AB$的长?

Fact list:
```
C: Ellipse
Expression(C) = (x^2/5 + y^2/4 = 1)
D: Line
Slope(D) = 2
PointOnCurve(RightFocus(C), D) = True
A, B: Point
Intersection(D, C) = {A, B}
O: Origin
IsChordOf(LineSegmentOf(A, B), C) = True
```

Query list:
```
Length(LineSegmentOf(A, B))
```

Answer list:
```
5*sqrt(5)/3
```


## Question 212
$F_{1}$、$F_{2}$分别是双曲线$\frac{x^{2}}{16}-\frac{y^{2}}{9}=1$的左、右焦点,$P$为双曲线右支上一点,$I$是$\Delta PF_{1}F_{2}$的内心,且$S_{\Delta IPF_{2}}=S_{\Delta IPF_{1}}-\lambda S_{\Delta IF_{1}F_{2}}$,则$\lambda$=?

Cannot annotate. Reason: 算子缺失


## Question 213
已知点$A$、$B$是双曲线$x^{2}-\frac{y^{2}}{2}=1$上的两点,$O$为原点,若$\overrightarrow{OA}\cdot\overrightarrow{OB}=0$,则点$O$到直线$AB$的距离为?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2 - y^2/2 = 1 )
A, B: Point
O: Origin
PointOnCurve(A, C)
PointOnCurve(B, C)
DotProduct(VectorOf(O, A),VectorOf(O, B)) = 0
```

Query list:
```
Distance(O, LineOf(A, B))
```

Answer list:
```
sqrt(2)
```


## Question 214
若直线$y=x+b$与曲线$y=3-\sqrt{4x-x^{2}}$有公共点,则$b$的取值范围是?

Fact list:
```
C: Line
b: Number
Expression(C) = ( y = b + x )
D: Curve
Expression(D) = ( y = 3 - sqrt(-x^2 + 4*x) )
IsIntersect(C, D) = True
```

Query list:
```
Range(b)
```

Answer list:
```
[1-2*sqrt(2),3]
```


## Question 215
已知$F_{1},F_{2}$为双曲线$\frac{x^{2}}{9}-\frac{y^{2}}{36}=1$的焦点,点$A$在双曲线上,点$M$坐标为$(\sqrt{3},\sqrt{3})$且$\Delta AF_1F_2$的一条中线恰好在直线$AM$上,则线段$AM$的长度为?

Cannot annotate. Reason: 算子缺失


## Question 216
已知双曲线$\frac{x^{2}}{4}-\frac{y^{2}}{21}=1$,$F_{1},F_{2}$分别为它的左、右焦点,$P$为双曲线上一点,且$|PF_1|,|F_1F_2|,|PF_2|$成等差数列,则$\Delta PF_1F_2$的面积为?

Cannot annotate. Reason: 知识点不符


## Question 217
若椭圆$\frac{x^{2}}{m}+\frac{y^{2}}{4}=1$的离心率为$\frac{1}{2}$,则$m$为?

Fact list:
```
C: Ellipse
m: Number
Expression(C) = ( y^2/4 + x^2/m = 1 )
Eccentricity(C) = 1/2
```

Query list:
```
m
```

Answer list:
```
{3, 16/3}
```


## Question 218
抛物线$x^{2}=4y$的准线方程为?

Fact list:
```
C: Parabola
Expression(C) = ( x^2 = 4*y )
```

Query list:
```
Expression(Directrix(C))
```

Answer list:
```
y=-1
```


## Question 219
若直线$y=-x+m$与曲线$y=\sqrt{5-\frac{1}{4}x^{2}}$只有一个公共点,则$m$的取值范围是?

Fact list:
```
C: Line
m: Number
Expression(C) = ( y = m - x )
D: Curve
Expression(D) = ( y = sqrt(5 - x^2/4) )
NumIntersection(C, D) = 1
```

Query list:
```
Range(m)
```

Answer list:
```
[-2*sqrt(5),2*sqrt(5))+{5}
```


## Question 220
椭圆$4x^{2}+my^{2}=4m$的焦距为2,则$m$=?

Fact list:
```
C : Ellipse
m : Number
Expression(C) = (4*x^2 + m*y^2 = 4*m)
FocalLength(C) = 2
```

Query list:
```
m
```

Answer list:
```
{3,5}
```


## Question 221
如果双曲线过点$P(6,\sqrt{3})$,渐近线方程为$y=\pm\frac{x}{3}$,则此双曲线的方程为?

Fact list:
```
C: Hyperbola
P: Point
Coordinate(P) = (6, sqrt(3))
PointOnCurve(P, C) = True
Expression(Asymptote(C)) = (y=pm*x/3)
```

Query list:
```
Expression(C)
```

Answer list:
```
(x^2/9 - y^2 = 1)
```


## Question 222
已知椭圆的焦点是双曲线的顶点,双曲线的焦点是椭圆的长轴顶点,若两曲线的离心率分别为$e_{1}$、$e_{2}$则$e_{1}\cdot e_{2}$=?

Fact list:
```
C: Ellipse
D: Hyperbola
Focus(C) = Vertex(D)
Focus(D) = Endpoint(MajorAxis(C))
e1, e2: Number
e1 = Eccentricity(C)
e2 = Eccentricity(D)
```

Query list:
```
e1*e2
```

Answer list:
```
1
```


## Question 223
已知$F_1$、$F_2$为双曲线$\frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}=1(a>0,b>0)$的左、右焦点,过点$F_2$作此双曲线一条渐近线的垂线,垂足为$M$,且满足$|\overrightarrow{MF_{1}}|=3|\overrightarrow{MF_{2}}|$,则此双曲线的渐近线方程为?

Fact list:
```
F1, F2, M: Point
C: Hyperbola
a, b: Number
a>0
b>0
Expression(C) = (x^2/a^2-y^2/b^2=1)
F1 = LeftFocus(C)
F2 = RightFocus(C)
l,r: Line
In(r, Asymptote(C))
PointOnCurve(F2, l)
IsPerpendicular(l, r)
FootPoint(l, r) = M
Abs(VectorOf(M, F1)) = 3*Abs(VectorOf(M, F2))
```

Query list:
```
Expression(Asymptote(C))
```

Answer list:
```
y=pm*sqrt(2)/2*x
```


## Question 224
方程$\frac{x|x|}{16}+ \frac{y|y|}{9}= \lambda(\lambda <0)$的曲线即为函数$y=f(x)$的图象,对于函数$y=f(x)$,下列命题中正确的是.(请写出所有正确命题的序号)<br>1函数$y=f(x)$在$R$上是单调递减函数;2函数$y=f(x)$的值域是$R$;<br>3函数$y=f(x)$的图象不经过第一象限;4函数$y=f(x)$的图象关于直线$y=x$对称;<br>5函数$F(x)=4f(x)+3$至少存在一个零点.

Cannot annotate. Reason: 题型不符


## Question 225
椭圆$C$的焦点在$x$轴上,焦距为$2$,直线$n:x-y-1=0$与椭圆$C$交于$A$、$B$两点,$F_1$是左焦点,且$F_{1}A \bot F_{1}B$,则椭圆$C$的标准方程是?

Fact list:
```
C: Ellipse
n: Line
FocalLength(C) = 2
Expression(n) = ( x - y - 1 = 0 )
PointOnCurve(Focus(C), xAxis) = True
A,B, F1 : Point
Intersection(C, n) = {A,B}
F1= LeftFocus(C)
IsPerpendicular(LineSegmentOf(F1, A), LineSegmentOf(F1, B))
```

Query list:
```
Expression(C)
```

Answer list:
```
x^2/(2 + sqrt(3)) + y^2/(1+sqrt(3)) = 1
```


## Question 226
已知椭圆$C: \frac{x^{2}}{2}+ \frac{y^{2}}{4}=1$,过椭圆$C$上一点$P(1, \sqrt{2})$作倾斜角互补的两条直线$PA$、$PB$,分别交椭圆$C$于$A$、$B$两点.则直线$AB$的斜率为?

Cannot annotate. Reason: 算子缺失


## Question 227
已知直线$x=t$交抛物线$y^{2}=4x$于$A$、$B$两点.若该抛物线上存在点$C$,使得$AC\bot BC$,则$t$的取值范围为?

Fact list:
```
E: Parabola
Expression(E) = ( y^2 = 4*x )
D: Line
t: Number
Expression(D) = ( x = t )
A, B: Point
Intersection(D, E) = {A, B}
C: Point
PointOnCurve(C, E)
IsPerpendicular(LineSegmentOf(A, C), LineSegmentOf(B, C))
```

Query list:
```
Range(t)
```

Answer list:
```
[4, +oo)
```


## Question 228
抛物线$y=x^{2}(-2 \leq x \leq 2)$绕$y$轴旋转一周形成一个如图所示的旋转体,在此旋转体内水平放入一个正方体,该正方体的一个面恰好与旋转体的开口面平齐,则此正方体的体积是?

Cannot annotate. Reason: 知识点不符


## Question 229
已知双曲线$\frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}=1(a>0,b>0)$的两条渐近线与抛物线$y^{2}=2px(p>0)$的准线分别交于$A,B$两点,$O$为坐标原点.若双曲线的离心率为$2$,$\Delta AOB$的面积为$\sqrt{3}$,则$p$=?

Fact list:
```
C1:Hyperbola
Expression(C1)=(x^2/a^2-y^2/b^2=1)
a,b,p:Number
a>0
b>0
p>0
C2:Parabola
Expression(C2)=(y^2=2*p*x)
A,B:Point
Intersection(Directrix(C2),Asymptote(C1))={A,B}
O:Origin
Eccentricity(C1)=2
Area(TriangleOf(A,O,B))=sqrt(3)
```

Query list:
```
p
```

Answer list:
```
3/2
```


## Question 230
设$AB$是椭圆的长轴,点$C$在椭圆上,且$\angle CBA= \frac{\pi}{4}$,若$AB=4$,$BC= \sqrt{2}$,则椭圆的两个焦点之间的距离为?

Fact list:
```
Ellipse_1: Ellipse
A, B: Point
LineSegmentOf(A,B) = MajorAxis(Ellipse_1)
C: Point
PointOnCurve(C,Ellipse_1)
AngleOf(C,B,A) = pi/4
LineSegmentOf(A,B) = 4
LineSegmentOf(B,C) = sqrt(2) 
F1, F2:Point
{F1, F2} = Focus(Ellipse_1)
```

Query list:
```
Distance(F1, F2)
```

Answer list:
```
4*sqrt(6)/3
```


## Question 231
以抛物线$y^{2}=20x$的焦点为圆心,且与双曲线$\frac{x^{2}}{16}- \frac{y^{2}}{9}=1$的两条渐近线都相切的圆的方程为?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/16 - y^2/9 = 1 )
D: Parabola
Expression(D) = ( y^2 = 20*x )
M: Circle
Center(M) = Focus(D)
l1, l2: Line
Asymptote(C) = {l1, l2}
IsTangent(l1, M) = True
IsTangent(l2, M) = True
```

Query list:
```
Expression(M)
```

Answer list:
```
(x-5)^2 + y^2 = 9
```


## Question 232
若对于给定的负实数$k$,函数$f(x)= \frac{k}{x}$的图象上总存在点C,使得以C为圆心,1为半径的圆上有两上不同的点到原点的距离为2,则$k$的取值范围为?

Cannot annotate. Reason: 知识点不符


## Question 233
直线$l$过椭圆$\frac{x^{2}}{2}+y^{2}=1$的左焦点F,且与椭圆相交于P、Q两点,M为PQ的中点,O为原点.若△FMO是以OF为底边的等腰三角形,则直线l的方程为?

Cannot annotate. Reason: 算子缺失


## Question 234
若实数$a,b,c,d$满足$(b-e\ln(a))^{2}+(c-d+3)^{2}=0$(其中$e$是自然底数),则$(a-c)^{2}+(b-d)^{2}$的最小值为?

Fact list:
```
a,b,c,d:Real
(b-e*ln(a))^2+(c-d+3)^2=0
```

Query list:
```
Min((a - c)^2 + (b - d)^2)
```

Answer list:
```
9/2
```


## Question 235
过抛物线$x^2=2py(p>0)$的焦点作斜率为1的直线与该抛物线交于A,B两点,A,B在x轴上的正射影分别为D,C.若梯形ABCD的面积为12$\sqrt{2}$,则P=?

Cannot annotate. Reason: 算子缺失


## Question 236
已知$A , B$是椭圆$\frac{x^{2}}{a^{2}}+ \frac{y^{2}}{b^{2}}=1(a>b>0)$和双曲线$\frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}=1(a>0,b>0)$的公共顶点。$P$是双曲线上的动点,$N$是椭圆上的动点($P$、$M$都异于$A$、$B$),且满足$\overrightarrow{AP}+ \overrightarrow{BP}= \lambda(\overrightarrow{AM}+ \overrightarrow{BM})$,其中$\lambda \in R$,设直线$AP$、$BP$、$AM$、$BM$的斜率 分别记为$k_{1},k_{2},k_{3},k_{4}$, $k_{1}+k_{2}=5$,则$k_{3}+k_{4}=$?

Cannot annotate. Reason: 其他


## Question 237
抛物线$y^{2}=2px(p>0)$的焦点为$F$,$A,B$在抛物线上,且$\angle AFB= \frac{\pi}{2}$,弦$A B$的中点$M$在其准线上的射影为$N$,则$\frac{|MN|}{|AB|}$的最大值为?

Fact list:
```
C: Parabola
p: Number
p>0
Expression(C) = (y^2=2*p*x)
F, A, B, M, N: Point
F = Focus(C)
PointOnCurve(A, C)
PointOnCurve(B, C)
AngleOf(A, F, B) = pi/2
IsChordOf(LineSegmentOf(A, B), C)
N = Projection(MidPoint(LineSegmentOf(A, B)), Directrix(C))
```

Query list:
```
Max(Abs(LineSegmentOf(M,N))/Abs(LineSegmentOf(A, B)))
```

Answer list:
```
sqrt(2)/2
```


## Question 238
已知抛物线$y^{2}=2px(p>0)$的准线经过椭圆$\frac{x^{2}}{a^{2}}+ \frac{y^{2}}{b^{2}}=1(a>b>0)$的左焦点,且经过抛物线与椭圆两个交点的弦过抛物线的焦点,则椭圆的离心率为?

Fact list:
```
C: Parabola
p: Number
p>0
Expression(C) = ( y^2 = 2*(p*x) )
D: Ellipse
b, a: Number
a > b
b > 0
Expression(D) = ( y^2/b^2 + x^2/a^2 = 1 )
PointOnCurve(LeftFocus(D), Directrix(C)) = True
s: LineSegment
IsChordOf(s, C)
IsChordOf(s, D)
M, N: Point
{M, N} = Intersection(C, D)
PointOnCurve(M, s)
PointOnCurve(N, s)
PointOnCurve(Focus(C), s)
```

Query list:
```
Eccentricity(D)
```

Answer list:
```
sqrt(2)-1
```


## Question 239
在平面直角坐标系下,曲线$C_{1}:\left\{ \begin{matrix} x=2t+2a \\ y=-t \\ \end{matrix} \right.$($t$为参数),曲线$C_{2}:$$\left\{ \begin{matrix} x=2 \cos \theta \\ y=2+2 \sin \theta \\ \end{matrix} \right.$($\theta$为参数).若曲线$C_{1}$、$C_{2}$有公共点,则实数$a$的取值范围_____.

Cannot annotate. Reason: 知识点不符


## Question 240
已知双曲线的中心在原点,离心率为$\sqrt{3}$,若它的一条准线与抛物线$y^{2}=4x$的准线重合,则该双曲线的方程是?

Fact list:
```
C: Hyperbola
O: Origin
Center(C) = O
Eccentricity(C) = sqrt(3)
D: Parabola
Expression(D) = ( y^2 = 4*x )
Directrix(D) = OneOf(Directrix(C))
```

Query list:
```
Expression(C)
```

Answer list:
```
x^2/3-y^2/6=1
```


## Question 241
设$A(x_1,y_1),B(x_2,y_2)$是抛物线$y=2x^2$上的两点,直线$l$是$AB$的垂直平分线

当直线$l$的斜率为$\frac{1}{2}$时,则直线$l$在y轴上截距的取值范围是?

当且仅当$x_1+x_2$取?值时,直线$l$过抛物线的焦点$F$.

Cannot annotate. Reason: 其他


## Question 242
抛物线$y=x^{2}$上两点$A(1,1)$、$B(-2,4)$处的切线交于$M$点,则$\Delta MAB$的面积为?

Fact list:
```
C: Parabola
Expression(C) = ( y = x^2 )
A, B: Point
Coordinate(A) = (1, 1)
Coordinate(B) = (-2, 4)
M: Point
Intersection(TangentOnPoint(A, C), TangentOnPoint(B, C)) = M
```

Query list:
```
Area(TriangleOf(M, A, B))
```

Answer list:
```
27/4
```


## Question 243
椭圆$\frac{x^{2}}{a^{2}}+ \frac{y^{2}}{b^{2}}=1(a>b>0)$的右焦点$F$,其右准线与$x$轴的交点为$A$,在椭圆上存在点$P$满足线段$AP$的垂直平分线过点$F$,则椭圆离心率的取值范围是?

Cannot annotate. Reason: 无


## Question 244
顶点在原点,焦点在$x$轴上,截直线$2x-y-4=0$所得弦长为$3\sqrt{5}$的抛物线方程为?

Fact list:
```
C: Parabola
O: Origin
Vertex(C) = O
PointOnCurve(Focus(C), xAxis)
L: Line
Expression(L) = (2*x-y-4=0)
InterceptChord(L, C) = 3*sqrt(5)
```

Query list:
```
Expression(C)
```

Answer list:
```
y^2=4x
```


## Question 245
双曲线$\frac{x^{2}}{64}- \frac{y^{2}}{36}=1$上一点$P$到双曲线右焦点的距离为$4$,那么点$P$到左准线的距离是?

Fact list:
```
C: Hyperbola
Expression(C) = ( x^2/64 - y^2/36 = 1 )
P: Point
PointOnCurve(P, C) = True
Distance(P, RightFocus(C)) = 4
```

Query list:
```
Distance(P,LeftDirectrix(C))
```

Answer list:
```
16
```


## Question 246
已知点$M$是抛物线$y^{2}=4x$上的一点,$F$为抛物线的焦点,$A$在圆$C:(x-4)^{2}+(y-1)^{2}=1$上,则$|MA|+|MF|$的最小值为?

Fact list:
```
M: Point
E: Parabola
Expression(E) = (y^2 = 4*x)
PointOnCurve(M, E) = True
F: Point
Focus(E) = F
A: Point
C: Circle
Expression(C) = ((x-4)^2 + (y-1)^2 = 1)
PointOnCurve(A, C) = True
```

Query list:
```
Min(Abs(LineSegmentOf(M, A)) + Abs(LineSegmentOf(M, F)))
```

Answer list:
```
4
```


## Question 247
已知双曲线的方程为$\frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}=1(a>0,b>0)$,过左焦点$F_{1}$作斜率为$\frac{\sqrt{3}}{3}$的直线交双曲线的右支于点$P$,且$y$轴平分线段$F_{1}P$,则双曲线的离心率是?

Cannot annotate. Reason: 算子缺失


## Question 248
已知双曲线$\frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}=1(a,b>0)$的离心率为$\frac{\sqrt{6}}{2}$,则$\frac { a ^ { 2 } + 4 } { b }$的最小值为?

Fact list:
```
C: Hyperbola
b, a: Number
a>0
b>0
Expression(C) = ( -y^2/b^2 + x^2/a^2 = 1 )
Eccentricity(C) = sqrt(6)/2
```

Query list:
```
Min((a^2+4)/b)
```

Answer list:
```
4*sqrt(2)
```


## Question 249
已知双曲线$C_{1}: \frac{x^{2}}{a^{2}}- \frac{y^{2}}{b^{2}}=1(a>0,b>0)$的左、右焦点分别为$F_{1}$、$F_{2}$,抛物线$C_{2}$的顶点在原点,它的准线与双曲线$C_{1}$的左准线重合,若双曲线$C_{1}$与抛物线$C_{2}$的交点$P$满足$PF_{2}\bot F_{1}F_{2}$,则双曲线$C_{1}$的离心率为?

Cannot annotate. Reason: 其他


## Question 250
中心在原点,对称轴为坐标轴的双曲线$C$的两条渐近线与圆$(x-2)^{2}+y^{2}=1$都相切,则双曲线$C$的离心率是?

Fact list:
```
C: Hyperbola
D: Circle
O : Origin
Expression(D) = ( y^2 + (x - 2)^2 = 1 )
Center(C) = O
L1, L2 : Line
{L1, L2} = Asymptote(C)
IsTangent(L1, D) = True
IsTangent(L2, D) = True
SymmetryAxis(C) = axis
```

Query list:
```
Eccentricity(C)
```

Answer list:
```
{2*sqrt(3)/3, 2}
```


## Question 251
如图,点$P$在椭圆$\frac{x^{2}}{a^{2}}+ \frac{y^{2}}{b^{2}}=1(a>b>0)$上,$F_{1}$、$F_{2}$分别是椭圆的左、右焦点,过点$P$作椭圆右准线的垂线,垂足为M,若四边形$PF_{1}F_{2}M$为菱形,则椭圆的离心率是?

Cannot annotate. Reason: 题型不符


## Question 252
 已知棱长为2的正方体$ABCD-A_{1}B_{1}C_{1}D_{1}$中,$M$为$AB$的中点,P是平面$A B C D$内的动点,且满足条件$PD_{1}=3PM$,则动点P在平面$A BC D$内形成的轨迹是?

Cannot annotate. Reason: 知识点不符


## Question 253
已知椭圆$\frac{x^{2}}{4}+y^{2}=1$的焦点为$F_{1}$、$F_{2}$,点$P$为椭圆上任意一点,过$F_{2}$作$\angle F_{1}PF_{2}$的外角平分线的垂线,垂足为点$Q$,过点$Q$作$y$轴的垂线,垂足为$N$,线段$QN$的中点为$M$,则点$M$的轨迹方程为

Cannot annotate. Reason: 题型不符


## Question 254
双曲线$x^{2}-y^2=1$的渐近线被圆$x^{2}+y^{2}-6x-2y+1=0$所截得的弦长为?

Fact list:
```
C: Hyperbola
D: Circle
Expression(C) = (x^2 - y^2 = 1)
Expression(D) = (x^2 + y^2 - 6*x - 2*y + 1 = 0)
```

Query list:
```
Length(InterceptChord(Asymptote(C), D))
```

Answer list:
```
4
```


## Question 255
点P在焦点为$F_{1}(0,-1)$、$F_{2}(0,1)$,一条准线为$y = 4$的椭圆上,且$|PF_{1}|-|PF_{2}|=1$,$\tan \angle F_{1}PF_{2}$=?

Fact list:
```
C: Ellipse
F1, F2: Point
Coordinate(F1) = (0, -1)
Coordinate(F2) = (0,1)
{F1,F2} = Focus(C)
Expression(OneOf(Directrix(C))) = (y=4)
P: Point
PointOnCurve(P,C)
Abs(LineSegmentOf(P,F1))-Abs(LineSegmentOf(P,F2))=1
```

Query list:
```
Tan(AngleOf(F1, P, F2))
```

Answer list:
```
4/3
```


## Question 256
直线$y=-x + a$与曲线$y= \sqrt{1-x^{2}}$有两个交点,则$a$的取值范围是?

Fact list:
```
C: Line
a: Number
Expression(C) = ( y = a - x )
D: Curve
Expression(D) = ( y = sqrt(1 - x^2) )
NumIntersection(C, D) = 2
```

Query list:
```
Range(a)
```

Answer list:
```
[1, sqrt(2))
```


