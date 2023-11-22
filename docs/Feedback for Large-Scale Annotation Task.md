# Feedback for Large-Scale Annotation Task

This document reports the validation results for the large-scale annotation task.

## Validation Plans

1. In main stage, we will do validations at each checkpoint during the annotation. We set the checkpoints at ~~200, 500, 1000, 2000, 3000, ..., 14000~~ 200, 700, 1200, 2200, 3200, ..., 14200. Once the number of annotated questions reaches the checkpoint, we'll randomly pick 10 questions to do validation. We'll report details of the validation result.
2. In the final stage, we will randomly pick 200 questions to do validation. We'll only report the error types of the validation result but not the IDs of the question.

## Pass Rate

80%. We'll take further actions if the accuracy fails to meet this standard.

## Validation Reports

### Checkpoint 01

Date: 2022/06/24

Range: 0-200

Result:

|  ID   | Can Annotate? | Status | Reason |
| :---: | :-----------: | :----: | :----: |
| 17068 |               |   ✔    |        |
| 7195  |               |   ✔    |        |
| 12812 |               |   ✔    |        |
| 11146 |      no       |   ✔    |        |
| 10030 |               |   ✖    |  span  |
| 15825 |      no       |   ✔    |        |
| 14545 |               |   ✔    |        |
| 12854 |               |   ✖    |  can   |
| 2965  |               |   ✔    |        |
| 16353 |               |   ✔    |        |

Pass: ✔ 8/10

#### 10030

http://47.102.141.251/#/questions/10030

句子没有问题。本题描述比较特殊，我们认为span的标注方式，cyzhh的标注方法更合适一些。

`$\frac{x^{2}}{16}-\frac{y^{2}}{9}=1$，则此双曲线的离心率为?`

将`$\frac{x^{2}}{16}-\frac{y^{2}}{9}=1$`视为一个双曲线，然后后面的双曲线直接指代前面的这个表达式。这样，`G: Hyperbola`就对应两个span。

#### 12854

http://47.102.141.251/#/questions/12854

这题属于圆锥曲线问题，实质上$a$、$b$构成了一个半椭圆，$c$、$d$构成了一条直线，而问题是在询问他们之间的最短距离。因此选择知识点不符不是很恰当。

这样的问题，直接按照普通方法标注即可。参考cyzhh的标注。

#### Conclusion

总体来看标注的质量非常高，两道验收中的题目也都是不太关键的小问题。希望继续保持！


### Checkpoint 02

Date: 2022/06/28

Range: 200-700

Result:

|  ID   | Can Annotate? | Status | Reason |
| :---: | :-----------: | :----: | :----: |
| 16080 |               |   ✖    |  span  |
| 6826  |               |   ✔    |        |
| 13755 |               |   ✔    |        |
| 6492  |      no       |   ✔    |        |
| 9020  |               |   ✔    |        |
| 6899  |               |   ✖    |  span  |
| 15015 |               |   ✔    |        |
| 5704  |      no       |   ✔    |        |
| 16397 |      no       |   ✔    |        |
| 6789  |      no       |   ✔    |        |

Pass: ✔ 8/10

#### 16080

http://47.102.141.251/#/questions/16080

`Coordinate(J) = (sqrt(5), -3*sqrt(3))`对应的span应为`点$(\sqrt{5},-3 \sqrt{3})$`，而不是`$(\sqrt{5},-3 \sqrt{3})$`.

注意：声明（带冒号的表达式）标注中的span，在断言（带等号的表达式）的span中一般是不可拆分的。

![](https://pad.degrowth.net/uploads/upload_652b73dd919ff5afcc3fed7e4f88a499.png)

#### 6899

http://47.102.141.251/#/questions/6899

`E: Circle`的span标注少了一个`圆$E$`。

注意：标注声明（带冒号的表达式）时，可以每标一个都把整个句子过一遍，不容易遗漏。

#### Conclusion

这次两个span上的问题都比较基础。还请务必重视。表达式的标注准确率很高，希望继续保持。至于是否需要检查上一批次中存在类似的问题，可以向标注员了解情况后自行决定。

注：以上两个问题都已经修复，覆盖了之前的标注。


### Checkpoint 03

Date: 2022/07/05

Range: 700-1200

Result:

|  ID   | Can Annotate? | Status | Reason |
| :---: | :-----------: | :----: | :----: |
| 17051 |               |   ✔    |        |
| 16119 |               |   ✔    |        |
| 4479  |               |   ✔    |        |
| 8686  |               |   ✔    |        |
| 14360 |      no       |   ✔    |        |
| 7674  |               |   ✔    |        |
| 14878 |               |   ✔    |        |
| 16620 |      no       |   ✔    |        |
| 9665  |               |   ✔    |        |
| 6587  |               |   ✔    |        |

Pass: ✔ 10/10

#### Conclusion

恭喜，全部通过！


### Checkpoint 04

Date: 2022/07/11

Range: 1200-2200

Result:

|  ID   | Can Annotate? | Status | Reason |
| :---: | :-----------: | :----: | :----: |
| 9865  |      no       |   ✔    |        |
| 9551  |      no       |   ✖    | cannot |
| 15564 |      no       |   ✔    |        |
| 15051 |               |   ✔    |        |
| 9618  |               |   ✔    |        |
| 12917 |      no       |   ✔    |        |
| 5460  |               |   ✔    |        |
| 11827 |      no       |   ✔    |        |
| 12906 |      no       |   ✔    |        |
| 9293  |               |   ✖    | redundant     |

Pass: ✔ 8/10

#### 9551

http://47.102.141.251/#/questions/9551

:::info
9551: 椭圆$\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1(a>b>0)$的左焦点为$F$, 直线$x=m$与椭圆相交于$A$, $B$两点, 若$\Delta F A B$的周长最大时,$\Delta F A B$的面积为$b c$, 则椭圆的离心率为?
:::

题目其实隐含了$c$为椭圆半焦距，知道了这一点，我们才能知道$\Delta F A B$的面积到底是多少，才能求解这道题。

但也有一些情况，$c$不是隐含条件，如：

:::info
6794: 已知点$F(c , 0)$为双曲线$C$: $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1  (a>0 , b>0)$的右焦点，点$B$为双曲线虚轴的一个端点，直线$B F$与双曲线的一条渐近线垂直，则双曲线$C$的离心率为?
:::

这里我们已知$F$是右焦点，所以$F(c , 0)$其实为$c$给出了定义（即半焦距）。

现在我们总结一下可以标注的情况。
1. 题目为$c$给出了定义，表示椭圆或双曲线的半焦距
    i. $c$出现在焦点坐标中。如：$F_1(-c , 0)$, $F_2(c , 0)$ ([6885](http://47.102.141.251/#/questions/6885)); $F(-c, 0)$ ([7362](http://47.102.141.251/#/questions/7362)); $F(c, 0)$ ([7559](http://47.102.141.251/#/questions/7559)); $F(0, c)$; 右焦点坐标为$(c, 0)$ ([2689](http://47.102.141.251/#/questions/2689)).
    ii. 指出焦距长为 $2c$ ([6938](http://47.102.141.251/#/questions/6938))，或半焦距为 $c$ ([8926](http://47.102.141.251/#/questions/8926))。
    iii. 用其他字母（如$a, b, e$）为$c$给出定义. 如：$c=\sqrt{a^{2}-b^{2}}$ ([7799](http://47.102.141.251/#/questions/7799)), $c^{2}=a^{2}-b^{2}$ ([11102](http://47.102.141.251/#/questions/11102), 注意背景在抛物线中，但其实表示椭圆半焦距), $a^{2}=b^{2}+c^{2}$ ([13266](http://47.102.141.251/#/questions/13266))
    iv. 出现在准线方程中，如：椭圆准线$x=\frac{a^2}{c}$. 注意需要明确指出这是准线。
    v. ...
2. $c$不表示椭圆或双曲线的半焦距。如([6232](http://47.102.141.251/#/questions/6232)), ([10744](http://47.102.141.251/#/questions/10744))

而一些题目需要默认$c$表示椭圆或双曲线的半焦距，这种题目属于无法标注-省略条件。如：([9805](http://47.102.141.251/#/questions/9805)), ([10311](http://47.102.141.251/#/questions/10311)), ([9511](http://47.102.141.251/#/questions/9511)), ([6709](http://47.102.141.251/#/questions/6709)).

我们已经检查过了所有已经标注的题目，并对其作了更正。之后的标注中，如有疑问，可以及时询问我们。

以上内容没有更新到标注文档中。

#### 9293

http://47.102.141.251/#/questions/9293


:::info
直线$l$与抛物线$C$相切于$Q$点

✔:
```
TangentPoint(l, C) = Q
```

✖:
```
TangentPoint(l, C) = Q
IsTangent(l, C)
```
:::

相切于某点使用`TangentPoint`即可，不必再单独表示两曲线相切。

查阅7月8日聊天记录。这个例子已经更新到了标注文档中。

可以根据实际标注情况自行决定是否需要检查已经标注的内容。

#### Conclusion

第一次发现句子标注有问题，还需多加注意。这次验证中span全部正确，继续保持！

平时有问题可以随时提问，平时多问一些，后面修正的工作量就少一些。我们虽然不一定能马上回答，但肯定会尽快给出回复。提问中加上序号可以帮助我们有序地给出答复。
