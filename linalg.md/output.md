## ID2107 Tutorial 1 Linear Algebra

$$
\mathbf{A b s t r a c t}
$$

This tutorial is about ERO, RRE and Solving System of Linear Equations via EROs. In the tutorial class, focus on Exercises 1-4, 1-5 and 1-6

ixercise $I-I$ . [Gaussian Elimination Method, Slides 1-30 olve the linear system using the Gaussian elimination method

Solve the linear system using the Gaussian elimination method

(a)
$$
\begin{array} {l} {\left\{\begin{array} {r c r c r c r c r} {-3 x} & {-} & {2 y} & {+} & {2 z} & {=} & {-2} \\ {-x} & {-} & {3 y} & {+} & {z} & {=} & {-3} \\ {x} & {-} & {2 y} & {+} & {z} & {=} & {-2} \\ {} & {} & {} & {} & {} & {} & {} \\ {-2 x} & {-} & {2 y} & {+} & {2 z} & {=} & {1} \\ {x} & {} & {} & {+} & {5 z} & {=} & {-1} \\ {3 x} & {+} & {2 y} & {+} & {3 z} & {=} & {-2} \\ \end{array} \right.} \\ \end{array}
$$
(d
$$
) \ \left\{\begin{array} {r r r r r r} {3 x_{1}} & {-3 x_{2}} & {+x_{3}} & {+3 x_{4}} & {=} & {-3} \\ {x_{1}} & {+x_{2}} & {-x_{3}} & {-2 x_{4}} & {=} & {3} \\ {4 x_{1}} & {-2 x_{2}} & {} & {+x_{4}} & {=} & {0} \\ \end{array} \right.
$$
(C
$$
) \ \left\{\begin{array} {r r r r r r} {-x_{1}} & {} & {+3 x_{3}} & {+x_{4}} & {=} & {2} \\ {2 x_{1}} & {+3 x_{2}} & {-3 x_{3}} & {+x_{4}} & {=} & {2} \\ {2 x_{1}} & {-2 x_{2}} & {-2 x_{3}} & {-x_{4}} & {=} & {-2} \\ \end{array} \right.
$$
(b

$$
\mathrm{( a )} \ \left\{\begin{array} {r c r c r c r c r} {-3 x} & {-} & {2 y} & {+} & {2 z} & {=} & {-2} \\ {-x} & {-} & {3 y} & {+} & {z} & {=} & {-3} \\ {x} & {-} & {2 y} & {+} & {z} & {=} & {-2} \\ \end{array} \right.
$$
{
$$
c ) \ \left\{\begin{array} {r r r r r r} {-x_{1}} & {} & {+3 x_{3}} & {+x_{4}} & {=} & {2} \\ {2 x_{1}} & {+3 x_{2}} & {-3 x_{3}} & {+x_{4}} & {=} & {2} \\ {2 x_{1}} & {-2 x_{2}} & {-2 x_{3}} & {-x_{4}} & {=} & {-2} \\ \end{array} \right.
$$

$$
\begin{array} {r l} {[ \ ( x=0 , \, y=1 , \, z=0 ) ;} \\ {\{x=-1-5 t , \, y=6 t+\frac{1} {2} , \, z=t ) ;} \\ {( x_{1}=1-\frac{1} {2} x_{4} , \, x_{2}=1-\frac{1} {2} x_{4} , \, x_{3}=1-\frac{1} {2} x_{4} , \, x_{4} \in\mathcal{R} ) ;} \\ {( x_{1}=1+\frac{1} {3} x_{3}+\frac{1} {2} x_{4} , \, x_{2}=2+\frac{2} {3} x_{3}+\frac{3} {2} x_{4} , \, x_{3} , x_{4} \in\mathcal{R} ) \ \ ]} \\ \end{array}
$$

## Exercise 1-2. [Reduced Row Echelon Form, Slides 23-26

Find the reduced row echelon form of the matrices

0
$$
i ) \ \left[ \begin{array} {r r r r} {-2} & {2} & {-1} & {2} \\ {0} & {3} & {3} & {-3} \\ {1} & {-4} & {2} & {2} \\ \end{array} \right]
$$
$$
\mathrm{( b )} \; \left[ \begin{array} {r r r r} {4} & {-3} & {-4} & {-2} \\ {-4} & {2} & {1} & {-4} \\ {-1} & {-3} & {1} & {-4} \\ \end{array} \right]
$$

Can you write a computer program to convert a $m \times n$ matrix to reduced row echelon form?

$$
[ \; \left[ \begin{array} {r r r r} {1} & {0} & {0} & {-2} \\ {0} & {1} & {0} & {-1} \\ {0} & {0} & {1} & {0} \\ \end{array} \right] \! ; \; \left[ \begin{array} {r r r r} {1} & {0} & {0} & {2} \\ {0} & {1} & {0} & {\frac{6} {5}} \\ {0} & {0} & {1} & {\frac{8} {5}} \\ \end{array} \right] \; \; ]
$$

## Exercise 1-3 Unique, Many and No Solution

The angmentation matik of a linear system has the form

$$
\left[ \begin{array} {r r r | r} {-2} & {3} & {1} & {a} \\ {1} & {1} & {-1} & {b} \\ {0} & {5} & {-1} & {c} \\ \end{array} \right]
$$

(a) Determinethe valus of $a$ . $\it b$ and $c$ for which the linar yste i consistent.
(b) Dtemine the vales of $a$  $\it b$ and $c$ forwhich he linea stem is inonsistent. (c) When it is consistent, does the linear systerm have a unidque solution or infinitely many solutions?
(d cive a seciconsistnt nea stm and nd ne atiular outio.

Determine the values of $a$ , $\it b$ and $c$ for which the linear system is consistent

(e) When t is consistent, dos the linear system have a unique solution or infinitely many solutions?

dtieasecficonstet inar sem and ind on ariular solution

consistent when $a \,+\, 2 b \,-\, c \,=\, 0$ ; inconsistent when $a+2 b-c \neq0$ 1 $z$ , then choose $a=b=c=0$ , then if the variables are denoted by $x$ , $y$ ; when consistent, the is a free ariales. so ifinitely many ample, one solution is by setting $z=1$ , then $x=\frac{4} {5}$ and $y=\frac1 5$ and
1

Exercise 1-4. [Unique, Many and No Solution The augmented matrix

$$
\left[ \begin{array} {c c c c | c} {k} & {1} & {1} & {1} & {a} \\ {1} & {k} & {1} & {1} & {1} \\ {1} & {1} & {k} & {1} & {1} \\ {1} & {1} & {1} & {k} & {1} \\ \end{array} \right]
$$

 $a$ reprosonts a system of lincar exquations with $4$ unknowns. Determine the values of $k$ and such that the system a ti n sotion, ti unique soltion, and fii many solutions.

$$
\begin{array} {r} {\mathrm{[ ~ ( i ) ~} k=-3 , a \neq-3 , \mathrm{~ o r ~} k=1 , a \neq1 ;} \\ {\mathrm{( i i ) ~} k \neq-3 \mathrm{~ a n d ~} k \neq1 ;} \\ {\mathrm{( i i i ) ~} k=a=1 \mathrm{~ o r ~} k=a=-3 . \ \mathrm{]}} \\ \end{array}
$$

Exercise 1-5. [Unique, Many and No Solution The augmented matrix

$$
\left[ \begin{array} {c c c c | c} {4 0} & {7 0} & {5 0} & {1 2} & {1 2 0} \\ {2 0} & {1 0} & {4 0} & {5 6} & {3 0} \\ {4 0} & {3 0} & {6 0} & {9 2} & {b} \\ {1 0} & {1 1} & {1 5} & {c} & {a} \\ \end{array} \right]
$$
resnsasonolinea csuations ih $4$ unknowns.

Determine the values of $a , b , c$ such that the system has (1) unique solutio, (ii) many solutions, lii) no solution, and $( \mathrm{i v} )$ with $a=2 2 , b=7 0$ , write down the solution for cases (i)ad in)

[ (i) Condition for unique solution: $5 c-8 0 \neq0$ . (ii) Condition for many solution: $5 c-8 0=0$ and $1 0 a-b-1 5 0=0$ . (i) Condition for no solution: $5 c-8 0=0$ and $1 0 a-b-1 5 0 \neq0$ 
MucMaHausadw $\left[ \begin{array} {c c c c c} {\frac{4} {7}} & {\frac{9} {7}} & {\frac{1} {7}} & {0} \\ \end{array} \right]^{T}$ 
 $\left[ \begin{array} {c c c c} {\frac{4} {7}-\frac{1 9 \, \alpha} {5}} & {2 \, \alpha+\frac{9} {7}} & {\frac{1} {7}} & {\alpha} \\ \end{array} \right]^{T} \, \, ]$ BCaUE $z-8$ 上电话区S区线区50区 5区5c86093 d0m07 Exercise 海NS $1-5$ . Instead cecodrctaconae (which mathematical questions
 $1-5 )$ 
to find answers.

AME线 电 区 TS  LC 451541045324040 343 9402 $\mathrm{A}$ contains
Three types of food will be used. One packet of food type
40mg of calcium, 20mg of potassium, 40mg of magnesium and 10mg of zinc. One packet of food type $\mathrm{B}$ contains 7Omg of calcium, 10mg of potassium, 30mg of magnesium and llmg of zinc. One packet of food type $\mathrm{C}$ contains 50mg of calcium, 40mg of potassium, 60rng of magnesium and 15mg of zinc.

(a) If a meal is to contain 120mg of calcium, 30mg of potassium, 70mg of magnesium types $\mathrm{A , \, B}$ 上d 国艺od上区Td世n世 T世电区e 世ded世e区cununano $\mathrm{A}$ , B and $\mathrm{C}$ to prepare
 $\mathrm{C}$ should be consumed in a meal to meet the dietary requirements. Suppose it is only possible to mix whole packets of food types
the required meal, how would you advise the dietician to prepare the meal, and state how many meals would the dietician prepared with your advise. Are there any other ratio of food types $\mathrm{A}$ , $\mathrm{B}$ and $\mathrm{C}$ which would satisfy the requirement?

(b) Gan the dietician prepare a meal to contain 120mg of calcium, 30mg of potassium, 7Omg of magnesium but with varying amount of zine? Why?

(o) What combinations of magnesium and zine can the dietician prepare if the meal is to contain 120mg of calcium and 30mg of potassium?

SST52 nutrition mixed can be prepared. S food type $\mathrm{D}$ HAD
She decided that one packet of the new
12mg of
could not decide on the amount of zinc. What recommendation would you give to the dieticiam? Why?

it: orsimpliciy consider thesanerint handsite a in art(a

(e) With your proposal in part (d), would the dietician now be able to produce meals at will? -ustify your answer.

 $[ \: \: \: ( \mathrm{a} ) \: \: 4 / 7$ packet of $\mathrm{A} , \, 9 / 7$ packet of $\mathrm{B}$ and $1 / 7$ packet of $\mathrm{C}$ ; $7$ meals with $4 , \, 9 , \, 1$ packets of $\mathrm{A}$ ,
 $\mathrm{B} , \, \mathrm{C} ; \, \mathrm{A} , \, \mathrm{B}$ , $\mathrm{C}$ have to be in this ratio.
(0)6.521 $7 \leq$ magnesium < 72grn and (b) $\mathrm{N o}$ :
 $2 1 . 6 5 \leq\mathrm{z i n c} \leq2 2 . 2 g m .$ 
(d) The amount of zine in type $\mathrm{D}$ food must NOT be equal to 16mg () $\mathrm{N o}$ , although now there are $4$ independent equations, the dietician still cannot mix negative
amount of food type to form a meal! ] For the circuit shown in Fig $-$ , set up a system of three equations for the loop currents $I_{1} , I_{2} , I_{3}$ . Write the corresponding augmented matrix and hence find the eact solution in terms of the unspecified voltages $V_{1} , V_{2}$ .

Find the interpolating polynomial $p ( t )=a_{0}+a_{1} t+a_{2} t^{2}$ that passes through the points
$$
( 1 , 1 2 ) , \; ( 2 , 1 5 ) , \; ( 3 , 1 6 ) .
$$

## Excrcise 1-7. Appicaio: Gircuig

![](figures\4-3-FIGURE.jpg)

$$
\mathrm{F i g u r e ~ 1 :}
$$

## Exercise 1-8. Appliation Gure fitting

$$
[ \begin{array} {l} {\left[ \begin{array} {l} {\medskip I_{1}=-\frac{5 0 9} {2 8 6 5} V_{1}-\frac{2} {1 9 1} V_{2}} \\ {\medskip I_{2}=-\frac{2 1} {9 5 5} V_{1}-\frac{4} {1 9 1} V_{2}} \\ {\medskip I_{3}=-\frac{2} {1 9 1} V_{1}-\frac{1 1} {1 9 1} V_{2}} \\ \end{array} \right]} \\ \end{array} ]
$$

$$
\left[ \; a_{0}=7 , \; a_{1}=6 , \; a_{2}=-1 \; \right]
$$

## IE2107 Tutorial 2 Linear Algebra: More EROs, Matrix Algebra, Matrix Inverse

$$
\mathbf{A b s t r a c t}
$$

nthe tutoral las fouson Exercis 24, 2-5 and 26

Exercise $2-7$ . [Matrix Operations, Slides 31-42 Let

$$
A=\left[ \begin{array} {r r r} {2} & {0} & {-1} \\ {1} & {0} & {-2} \\ \end{array} \right] , \quad B=\left[ \begin{array} {r r r} {-3} & {1} & {1} \\ {-3} & {1} & {1} \\ \end{array} \right] , \quad C=\left[ \begin{array} {r r} {3} & {-1} \\ {-1} & {-3} \\ \end{array} \right]
$$

explain why. Note: $A^{T}$ perform the following operations. $\mathit{A}$ . If a computation canmot be made, Whenever possible, means the trauspose of

(a $\begin{array} {l} {2 A^{T}-B^{T} ,} \\ {( A^{T}+B^{T} ) C} \\ \end{array}$ （b $B^{T}-2 A$ .8 $A B^{T}$ .出 $( A^{T} \dot{B}^{T} ) C$ (e ,印 (O ) (d)
(f) $C ( A^{T}+B^{T} )$  $( A^{T} C ) B$ 

Exercise $2-2$ . [Cross Product Let $\textbf{a}=\left[ \begin{array} {c c c} {a_{1}} & {a_{2}} & {a_{3}} \\ \end{array} \right]^{T}$ and $\textbf{x}=\big[ \begin{array} {c c c} {x_{1}} & {x_{2}} & {x_{3}} \\ \end{array} \big]^{T} .$ Write the cross product ${\bf a} \times{\bf x}$ as a matrix-vector multiplication. In other find matrix $\mathit{A}$ such that a $\times\mathbf{x}=A \mathbf{x} $ .

$$
[ ~ A=\left[ \begin{array} {c c c} {0} & {-a_{3}} & {a_{2}} \\ {a_{3}} & {0} & {-a_{1}} \\ {-a_{2}} & {a_{1}} & {0} \\ \end{array} \right] ~ ]
$$

 $n$  T5
Exercise $2=3$ . ICash flow to bank account balance] Let $\mathbf{c} \,=\, \left[ \begin{array} {c c c c} {c_{1}} & {c_{2}} & {\ldots} & {c_{n}} \\ \end{array} \right]^{T}$ 海0 $c_{i}$ indicate $\mathrm{a}$ deposit, and negative values indicate $\mathrm{a}$  $n$ time periods. We have $b_{1}=c_{1}$ ngs eweWmnecWLudsc wWowW
 $\mathbf{b}=\left[ \begin{array} {c c c c} {b_{1}} & {b_{2}} & {\ldots} & {b_{n}} \\ \end{array} \right]^{T}$ 

$$
b_{t}=( 1+r ) b_{t-1}+c_{t} , \quad t=2 , \ldots, n
$$

where $r > 0$ is the per period interest rate. Express b in terms of $\mathbf{c} , \mathrm{~ i . e}$ , find the matrix $\mathit{A}$ such that $\mathbf{b}=A \mathbf{c}$ .

$$
[ \begin{array} {c} {A=\left[ \begin{array} {c c c c} {1} \\ {( 1+r )} & {1} \\ {( 1+r )^{2}} & {( 1+r )} & {1} \\ {\vdots} \\ {( 1+r )^{n-1}} & {\dots} & {\dots} & {1} \\ \end{array} \right]} \\ \end{array} ]
$$

Exercise $2-4$ . Block Mariy Cosidr the matris

$$
K=\left[ \begin{array} {c c} {I} & {A^{T}} \\ {A} & {0} \\ \end{array} \right]
$$

ake sane, which of the folowing statsmets must be true!

(a) $K$ is square.
(b) $\mathit{A}$ is square or wide.
(c) $K$ is symetric, .e., $K^{T}=K$ 
(d) "The identity and zero submatrices in $\mathit{K}$ have the same dimensions. (e) The zero submatrix is square.

C $K$ is symmetric, i $K^{T}=K$ 
i.e.,

e) The zero submatrik is square.

Assume $\mathit{A}$ has $m$ rows and $n$ colus,and denote $\mathit{A}$ as $A_{m \times n}$ . Then
$$
K=\left[ \begin{array} {c c} {I_{n \times n}} & {A_{n \times m}^{T}} \\ {A_{m \times n}} & {0_{m \times m}} \\ \end{array} \right]_{( m+n ) \times( m+n )}
$$
Hence, statements $( \mathrm{a} ) , \, ( \mathrm{c} )$ , and $( \mathrm{e} )$ must be true. ]

Hence, statements $( \mathrm{a} ) , \, ( \mathrm{c} )$ , and $( \mathrm{e} )$ must be true. ]

## Exercise 2-5. [Matrix Operations, Slides 31-42

(a) 1f A is 3-by-5, $\mathit{B}$ is $2 \mathrm{-b y-3}$ , and if you stack the matrices A, $B$ . $C$ and $\mathit{D}$ into matrix $\mathit{D}$ puds $P=\left[ \begin{array} {c c} {A} & {C} \\ {D} & {B} \\ \end{array} \right]$ , what should be the dimensions of matrix $C$ and bigger $P$ 

中公am $\mathit{G}$ is 3-by-4, what should the dimensions of matrices $B$ and $\mathit{E}$ be
and
that multipication $\left[ \begin{array} {c c} {A} & {B} \\ \end{array} \right] \left[ \begin{array} {c} {E} \\ {G} \\ \end{array} \right]$ make sense?

中生区建金海公品科生中品服区有司 $\left[ \begin{array} {c c} {A} & {B} \\ \end{array} \right] \left[ \begin{array} {c} {E} \\ {G} \\ \end{array} \right]$ dimensions of matrices $\mathit{E}$ and $\mathit{G}$ be
and $B$ is 3-by-4, what should the
that make sense?

[C' is 3-by-3 and $\mathit{D}$ is $2 \mathrm{-b y-5}$ : $\mathit{E}$ is $2$ B is 3-by-3 and $\mathit{E}$ is 2-by-4;
by-n and $\mathit{G}$ is 4-by-n, $\mathrm{n=1 , 2 , 3 , \; . . . \;} ]$ ## Exercise 2-6. [Use ERO to find inverse, Slides 43-52

中市海中州中海中有店生中限服限司
$$
\mathrm{n v e r s e ~ o f ~ t h e ~ 2-b y-2 ~ m a t r i x} \; \biggl[ \begin{array} {c c} {a} & {b} \\ {c} & {d} \\ \end{array} \biggr] .
$$
What
ERO to derive the formula for the i

 $\left[ \begin{array} {c c} {A} & {B} \\ {C} & {D} \\ \end{array} \right]$ Assuming that only $\mathit{A}$ AAAANE
where $A , B , C , D$ are matrices of compatible dimensions. Pay particular $B A^{-1}$ on $\frac{B} {A} ?$ tcnrean un $A^{-1} B$ 

(e) Repeat part $\mathrm{( b )}$ ,asuring tat ong $\mathit{D}$ is invertible.

(d) What further assumptions do you need in parts (b) and $\mathrm{( c )}$ for the inverse of the block partition matrix $\left[ \begin{array} {c c} {A} & {B} \\ {C} & {D} \\ \end{array} \right]$ to exist?

## IE2107 Tutorial 3 Linear Algebra: Determinant, Elementary Matrices

## Abstract

nthe tuoral as, doal Berdies

## Exercise 3-1. Propris of Determimant, Slides 52-57,59-60 62

(a) If Ais a $n \times n$ 1 find $\operatorname* {d e t} ( 3 A ) , \, \operatorname* {d e t} ( 2 A^{-1} )$ , and $\mathrm{d e t} [ ( 2 A )^{-1} ]$ ,in terms of $\mathrm{d e t} ( A )$ 
matrix.

(b) If A= d e
$$
\left[ \begin{array} {c} {c} \\ {f} \\ {i} \\ \end{array} \right] \mathrm{~ a n d ~} \operatorname* {d e t} ( A )=1 0 \mathrm{, ~ f i n d ~} \operatorname* {d e t} \left[ \begin{array} {c c c} {a} & {g} & {d} \\ {b} & {h} & {e} \\ {c} & {i} & {f} \\ \end{array} \right]
$$
a b
g h

ec Listhe roetiesof otecminant tat you have used n arts $\mathrm{\, ( a )}$ and $\mathrm{( b )}$ 

$$
[ \; 3^{n} \operatorname* {d e t} ( A ) ; 2^{n} / \operatorname* {d e t} ( A ) ; 1 / ( 2^{n} \operatorname* {d e t} ( A ) ) \; ]
$$

## Exercise 3-2. |Elementary Matrices, Slides 63-65

(a)Find the matrix $\mathit{P}$ ill re-arange the column vector $\mathbf{u}=\left[ \begin{array} {c c c c c c} {a} & {b} & {c} & {d} & {e} & {f} \\ \end{array} \right]^{T}$ 
that
to $\mathbf{v}={\left[ \begin{array} {c c c c c c} {a} & {c} & {e} & {b} & {d} & {f} \\ \end{array} \right]}^{T} .$ 

io
$$
\mathbf{v}={\left[ \begin{array} {c c c c c c} {a} & {c} & {e} & {b} & {d} & {f} \\ \end{array} \right]}^{T} .
$$
manladmnsa $\mathbf{u}=\left[ \begin{array} {c c c c c c} {a} & {b} & {c} & {d} & {e} & {f} \\ \end{array} \right]^{T}$ 
Qe id the matix $P$ 
Fulkrw $Q$ thawil earange th o veaor $\mathbf{p} \,=\, \left[ \begin{array} {c c c} {a} & {b} & {c} \\ \end{array} \right]$ to $\textbf{q}=$  $\left[ \begin{array} {c c c} {a} & {c} & {b} \\ \end{array} \right] .$ 
(e) If, in (b), the dimensions of $a , \, b$ ,and $c$ are $\mathrm{2-b y-2 , ~ 2-b y-3}$ , nd 2-by-4 respectively. What will be the dimensions of $Q$ ? Write down the matrix $Q$ . How would your answer change if the dimensions of $a , \, b$ , and $c$ are n-by-2, n-by-3, and n-by-4 respectively?

(b) Find the matrix $Q$ that will rearange the row vector $\mathbf{p} \;=\; \left[ \begin{array} {c c c} {a} & {b} & {c} \\ \end{array} \right] \; \mathrm{t o} \; \mathbf{q} \;=$ 
$$
\left[ \begin{array} {c c c} {a} & {c} & {b} \\ \end{array} \right] .
$$

(o) If, in $\mathrm{( b )}$ , the dimensions of $a , \, b$ , and $c$ are $\mathrm{2-b y-2 , ~ 2-b y-3} .$ and $2 \mathrm{-b y-4}$ respectively. What will be the dimensions of $Q ?$ Write down the matrix $Q$ . How would your answer change if the dimensions of $a , \, b$ ,and $c$ are n-by-2, n-by-3, and n-by-4 respec-
s of and
tively?

$$
\left[ \begin{array} {c} {\mathrm{~ ( a ) ~} v=P u \mathrm{~ w h e r e ~} P=\left[ \begin{array} {c c c c c c} {1} & {0} & {0} & {0} & {0} & {0} \\ {0} & {0} & {1} & {0} & {0} & {0} \\ {0} & {0} & {0} & {0} & {1} & {0} \\ {0} & {1} & {0} & {0} & {0} & {0} \\ {0} & {0} & {0} & {1} & {0} & {0} \\ {0} & {0} & {0} & {0} & {0} & {1} \\ \end{array} \right]} \\ {\mathrm{~ ( b ) ~} q=p Q \mathrm{~ w h e r e ~} Q=\left[ \begin{array} {c c c c} {1} & {0} & {0} \\ {0} & {0} & {1} \\ {0} & {1} & {0} \\ \end{array} \right]} \\ \end{array} \right]
$$

(C) $Q$ is $9 \mathrm{-b y-9}$ . Form $Q$ as folows(QO=  $\mathrm{c y e} ( 9 , 9 ) ; \ \mathrm{Q}=\mathrm{Q} ( : , [ 1 \ 2 \ 6 \ 7 \ 8 \ 9 \ 3 \ 4 \ 5 ]$ no change Exercise 3-3. [Elementary Matrices, ts $\mathbf{D}$ eterminants and Inverses, Slides $6 6$ 1 Write down the elementary matrix, its determinant and inverse for each of the following elementary row operation on a $4 \times4$ matrix?

The determinants are -1, 5 and $1$ ; The inverses are elementary matrices that would "undo' the corresponding elementary row operations

Exercise 3-4. [Determinant via ERO and Elementary Matrices, Slides 63-67 Find the determinant of the matrix

(a) nterchange rows $1$ and 3
(b) Multiply row $3$ by a factor of $5$ ec Adeigtimsof row $2$ to row 1

$$
\left[ \begin{array} {r r r} {-6} & {\phantom{-} 4} & {5} \\ {2} & {\phantom{-} 8} & {2} \\ {-1} & {-4} & {2} \\ \end{array} \right]
$$

Exercise 3-5. Find the determinant of the matrix

$$
\left[ \begin{array} {r r r r} {1} & {2} & {3} & {4} \\ {-1} & {1} & {2} & {3} \\ {1} & {-1} & {1} & {2} \\ {-1} & {1} & {-1} & {a} \\ \end{array} \right]
$$

where $a$ is a real number. Leave your answer in terms of $a$ . -168

$$
[ \ 9 ( a+2 ) \ ]
$$

## Exercise 3-6. [Determinant of Block Diagonal Matrix

中
$$
\operatorname* {d e t} ( B ) .
$$
that the determinant of th
$$
\mathrm{~ e ~ b l o c k ~ p a r t i t i o n e d ~ m a t r i x ~} \left[ \begin{array} {c c} {I_{n}} & {0} \\ {0} & {B} \\ \end{array} \right] \mathrm{~ i s ~}
$$
equal to
Show

(b)
$$
\mathrm{S h o w ~ t h a t ~ d e t} ( \left[ \begin{array} {c c} {A} & {C} \\ {0} & {I_{m}} \\ \end{array} \right] )=\operatorname* {d e t} ( A )
$$

AanaA $n \times m$ respecively. where $\mathit{P}$ is the block par-matrix show t $\operatorname* {d e t} ( P )=\operatorname* {d e t} ( A ) \operatorname* {d e t} ( B )$ , $B$ and $C$ have dimensions
that
 $P=\left[ \begin{array} {c c} {A} & {C} \\ {0} & {B} \\ \end{array} \right]$ and the sub-matrices $\mathit{A}$ 
 $n \times n , m \times m$ 

$$
\mathrm{( d ) \ \: G i v e n \ t h a t}
$$

$$
A=\left[ \begin{array} {r r r r} {3} & {2} & {0} & {2} \\ {6} & {8} & {2} & {1} \\ {0} & {0} & {4} & {7} \\ {0} & {0} & {2} & {5} \\ \end{array} \right] , \quad B=\left[ \begin{array} {r r r} {-6} & {4} & {5} \\ {2} & {8} & {2} \\ {-1} & {-4} & {2} \\ \end{array} \right] , \quad C=\left[ \begin{array} {r r r} {1 2} & {6} & {1} \\ {4} & {4} & {1} \\ {7} & {4} & {3} \\ {8} & {8} & {3} \\ \end{array} \right]
$$

Determine th
$$
\mathrm{e ~ d e t e r m i n a n t ~ o f ~ t h e ~ m a t r i x ~} P=\left[ \begin{array} {c c} {A} & {C} \\ {0} & {B} \\ \end{array} \right]
$$

[ (a)By expanding the determinant along the first row or first column;
(b)E
$$
\mathrm{( c ) B y ~ f a c t o r i z i n g ~} P=\left[ \begin{array} {c c} {I_{n}} & {0} \\ {0} & {B} \\ \end{array} \right] \left[ \begin{array} {c c} {A} & {C} \\ {0} & {I_{m}} \\ \end{array} \right] ;
$$

## 1D2107 Tutorial 4

Linear Algebra: Linear Combination, Independence, Span, Basis

## Abstract

海饰 $A x=b$ problems with concepts
connect the mechanism
 $A x \,=\, b$ problems with concepts discussed from slides $7 4$ onwards, i., connecting the three possible outcomes of solving
such as Linear Combinations, Linear Independence, Span, as well as Invertibility, Colunn/Row /Null-spaces of the $\mathit{A}$ matrix.

Exercise 4-1. Translation Game, two sides of the same coin, Slides $\mathbf{7 7-8 8 ]}$ Refer to Tutorial 1, Exercise 1. Rephrase the question using the language of linear algebra using terms such as linearly independence/dependence, linear cornbination, span, colurn row unll space, basis, etc

ereas ene ntra Leacdi seroduced hore

![](figures\11-6-FIGURE.jpg)

Figure $2$ : Tutorial , Exercise

Exercise $4-2$ . [Essentially same as Exercise $\mathrm{1-2}$ , but using the language of Linear Algebra

CSNE NCTSESCTESTEc c d ON
different units of the following
unit of food type $\mathrm{A}$ contains 40mg of calcium, 20mg of potassium, 40mg of magnesium and 10mg of zinc. One unit of food type $\mathrm{B}$ contains 70mg of calcium, 10mg of potassium, 30mg of magnesium and 11mg of zinc. One unit of food type $\mathrm{C}$ contains 50mg of calcium, 40ng of potassium, 60mng of magnesium and 15mg of zinc.

$$
\mathrm{L e t}
$$

$$
A=\left[ \begin{array} {c c c c} {4 0} & {2 0} & {4 0} & {1 0} \\ \end{array} \right]^{T} , \, \, B=\left[ \begin{array} {c c c c} {7 0} & {1 0} & {3 0} & {1 1} \\ \end{array} \right]^{T} , \, \, C=\left[ \begin{array} {c c c c} {5 0} & {4 0} & {6 0} & {1 5} \\ \end{array} \right]^{T}
$$

bevetors rersating fod ypes $\mathrm{A , \; B , \; C} .$ 

(a) Show that $\mathrm{A , \ B}$ , $\mathrm{C}$ are linearly independent. What practical advantage does this have? What does $S p a n \{A , \, \, B , \, \, C \}$ represent? Give a practical interpretation to the linear combination $4 \mathrm{A+9 B+C} .$ 
 $\mathrm{C} , \, \mathrm{E} \rbrace?$ 12 56 92 $1 7 \, ]^{T}$ ncanacrcnc ane n $\rbrack^{T}$ wWatos this say $\{\mathrm{A , \, B}$ 
 $D=$ 
 $E=\left[ \begin{array} {l} {{1 2 0}} \\ \end{array} \right.$  $\{\mathrm{A} , \, \mathrm{B} , \, \mathrm{C} , \, \mathrm{D} \}$ and
about the linear independence or dependence of the sets
(c) Find the amount of food type $\mathrm{A , B}$ . $\mathrm{C}$ mix needed to produce meal $\mathrm{E}$ . stis solution unique? Explain.
(d) The dietician decided to add a fourth basic food type so that meals with any required nutrient mixed can be prepared. Should the dietician choose D or $\mathrm{E}$ as the fourth basic food type?
(e) Will there still be meals that cannot be physically produced from the proposed set of 4 basic food types? Explain.

(a) Show that $\mathrm{A , \ B}$ . $\mathrm{C}$ represent? CGive a practical interpretation to the
independent. What practical advantage does this have? What does $S p a n \{A , \, \, B , \, \, C \}$ 
linear combination $4 \mathrm{A+9 B+C}$ 

宝中7 $\{\mathrm{A} , \, \mathrm{B} , \, \mathrm{C} , \, \mathrm{D} \}$ and $\{\mathrm{A , \, B}$ 
per unit nutrition $D=$ 12 56 92 $1 7 \, ]^{T}$ but can for $E=\left[ \begin{array} {c c c} {1 2 0} & {3 0} & {6 8} \\ \end{array} \right]$ sets $\rbrack^{T}$ . What does this say about the linear independence or
 $\mathrm{C} , \, \mathrm{E} \rbrace?$ 

(c) Find the amount of food $\mathrm{A , B}$ , $\mathrm{C}$ mix needed to produce meal $\mathrm{E}$ . Is this solution
type
unique? Explain.

(d) The dietician decided to add a fourth basic food type so that meals with any required nutrient mixed can be prepared. Should the dietician choose D or $\mathrm{E}$ as the fourth basic food type?

e il thestilhe meastat anot hsialy roduced from th rposd se of 4 basic food types? Explain.

## Exercise 4-3. [Linearly Independenc, Slides 86-88

Determine whether the following are linearly independent or dependent. Justify your answers.

(a) The vectors
$$
\left[ \begin{array} {r} {1} \\ {1} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {r} {0} \\ {1} \\ {1} \\ \end{array} \right] \mathrm{~ a n d ~} \left[ \begin{array} {r} {1} \\ {0} \\ {-1} \\ \end{array} \right] \! .
$$
b The mairces $\left[ \begin{array} {r r} {1} & {2} \\ {2} & {1} \\ \end{array} \right] , \left[ \begin{array} {r r} {-1} & {1} \\ {1} & {-1} \\ \end{array} \right] \mathrm{~ a n d ~} \left[ \begin{array} {r r} {2} & {2} \\ {1} & {1} \\ \end{array} \right] .$ 
(e) The polynomials $\boldsymbol{p} ( \boldsymbol{x} )=\boldsymbol{1}+\boldsymbol{x} , \boldsymbol{q} ( \boldsymbol{x} )=\boldsymbol{1}-\boldsymbol{x}$ and $h ( x )=1-x^{2} .$ 

(a
$$
\mathrm{~ T h e ~ v e c t o r s ~} \left[ \begin{array} {r} {1} \\ {1} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {r} {0} \\ {1} \\ {1} \\ \end{array} \right] \mathrm{~ a n d ~} \left[ \begin{array} {r} {1} \\ {0} \\ {-1} \\ \end{array} \right] \! .
$$

(b)Thematico
$$
s \, \left[ \begin{array} {r r} {1} & {2} \\ {2} & {1} \\ \end{array} \right] , \left[ \begin{array} {r r} {-1} & {1} \\ {1} & {-1} \\ \end{array} \right] \, \mathrm{a n d} \, \left[ \begin{array} {r r} {2} & {2} \\ {1} & {1} \\ \end{array} \right] \! .
$$

cThe poly
$$
p ( x )=1+x , q ( x )=1-x \, \, \mathrm{a n d} \, \, h ( x )=1-x^{2} .
$$
lynomials

Exercise 4-4. Linearly Independence, Column Spae lides 86-88,100-103
By using the results from Exercise $4-4$ , or otherwise, answer the following and justify your answers:

Mecnecnugn d odams $\mathit{A}$ must be linearly dependent. A is a $3 \times5$ non-zero matrix,
 $n u l l i t y ( A ) ?$ 

$$
\mathrm{( a ) ~ A r e ~ t h e ~ v e c t o r s}
$$

$$
\left[ \begin{array} {c} {4} \\ {1} \\ {1} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {c} {1} \\ {4} \\ {1} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {c} {1} \\ {1} \\ {4} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {c} {1} \\ {1} \\ {1} \\ {4} \\ \end{array} \right] \; \mathrm{l i n e a r l y ~ i n d e p e n d e n t ?}
$$

$$
\mathrm{( b ) ~ A r e ~ t h e ~ v e c t o r s}
$$

$$
\left[ \begin{array} {r} {-3} \\ {1} \\ {1} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {r} {1} \\ {-3} \\ {1} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {r} {1} \\ {1} \\ {-3} \\ {1} \\ \end{array} \right] , \left[ \begin{array} {r} {1} \\ {1} \\ {1} \\ {-3} \\ \end{array} \right] \mathrm{~ l i n e a r l y ~ i n d e p e n d e n t ?}
$$

(0) ls the veter
$$
\left[ \begin{array} {c} {1} \\ {2} \\ {3} \\ {4} \\ \end{array} \right] \mathrm{~ i n ~ t h e ~ c o l u m n ~ s p a c e ~ o f ~} \left[ \begin{array} {c c c c} {7} & {1} & {1} & {1} \\ {1} & {7} & {1} & {1} \\ {1} & {1} & {7} & {1} \\ {1} & {1} & {1} & {7} \\ \end{array} \right] \mathrm{?}
$$

## Exercise 45. Rank and uliy Sldes 1-119

$$
\left[ \mathrm{~} n u l l i t y ( A )=2 , 3 \mathrm{~ o r ~} 4 \ \right]
$$

$$
\mathrm{E x e r c i s e ~ 4-6 . ~ L e t}
$$

$$
A=\left[ \begin{array} {r r r r r r} {1} & {3} & {-2} & {0} & {2} & {0} \\ {2} & {6} & {-5} & {-2} & {4} & {-3} \\ {0} & {0} & {5} & {1 0} & {0} & {1 5} \\ {2} & {6} & {0} & {8} & {4} & {1 8} \\ \end{array} \right] , \quad\mathbf d=\left[ \begin{array} {r} {0} \\ {-1} \\ {5} \\ {6} \\ \end{array} \right] \quad\mathrm{a n d} \quad\mathbf x=\left[ \begin{array} {r} {x_{1}} \\ {x_{2}} \\ {x_{3}} \\ {x_{4}} \\ {x_{5}} \\ {x_{6}} \\ \end{array} \right] .
$$

（a) Find all $\mathbf{x}$ which solve $A \mathbf{x}=\mathbf{d}$ 
bh Lnene oheis fn basi fo th l space of $\mathit{A}$ 
(s)Lcl $\mathbf{b} \ =\ \left[ \begin{array} {c c c c} {b_{1}} & {b_{2}} & {b_{3}} & {b_{4}} \\ \end{array} \right]^{T} \$  $b_{i} , i ~=~ 1 , 2 , 3 , 4$ are real numbers. Find the
where
condition for $b_{1} , b_{2} , b_{3} , b_{4}$ such that $A {\bf x}={\bf b}$ is consistent.
d ronotrwis finabais o the counmsac o A

a)Find all $\mathbf{x}$ which solve $A \mathbf{x}=\mathbf{d}$ 

b) Hence o otherwise, find a basis for the nul pace of $\mathit{A}$ 

(c) Let $\mathbf{b} \ =\ \left[ \begin{array} {c c c c} {b_{1}} & {b_{2}} & {b_{3}} & {b_{4}} \\ \end{array} \right]^{T}$ where $b_{i} , i ~=~ 1 , 2 , 3 , 4$ are real numbers. Find the condition for $b_{1} , b_{2} , b_{3} , b_{4}$ such that $A {\bf x}={\bf b}$ is consistent

(a) He,o thewis, find a basis forthe coum space of $\mathit{A}$ ## IE2107 Tutorial 5 Linear Algebra: Diagonalisation, Eigenvalues and Eigenvectors

## ID2107 Tutorial 5

## Exercis 5-1. [Diagonalisation of matriv, Slidos 128

上东业南山州 市热世话区 车业世区业服车装电区业业业业CEN
used to diagonalise a $n \times n$ matrix. What condition $( \mathrm{s} ) ~ \mathrm{i s ( a r e )}$ needed so that a matrix $\mathrm{A}$ 
reinforce the concept.

$$
\left[ \mathrm{~ s e e ~ l e c t u r e ~ n o t e s ~} \right]
$$

## Exercise 5-2 Diagonalisation of matrix, Slidos 128

Let $A=\left[ \begin{array} {r r r} {0} & {0} & {2} \\ {0} & {2} & {0} \\ {0} & {0} & {-1} \\ \end{array} \right]$ 

a Find the cgeavalesof $\mathit{A}$ 

(a) Find the oigenvalues of $\mathit{A}$ 
(b) Tro your seutin part (a) an yuconclude whether $\mathit{A}$ is diagonaliable Kpain. (e) Find the eigenvectos corresponding to each eigenvalue.
(d) Are the eigenvectors found in part $\mathrm{( c )}$ lincarly independent? Explain.
e) Fo ou resut in art (d) can you oncldewhether $\mathit{A}$ is digoaiableEBphan (f) If your answer to part $( \mathrm{e} )$ msuaiu mn that diagonalizes $\mathit{A}$ . Specify the
 $\mathit{P}$ 
diagonal matrix $\mathit{D}$ such that $D=P^{-1} A P .$ 

n your result in patg a) an you conclude whether $\mathit{A}$ isdiagoalzable? Expa

e) Find the eigevectors oresondin o ac eienvalue.

(d) Are the eigenvectors found in part (e y independent? Explain.
linearly

$$
\begin{array} {r c l} {} & {\mathrm{( c ) ~} \left[ \begin{array} {c} {1} \\ {0} \\ {0} \\ \end{array} \right] , \left[ \begin{array} {c} {\mathrm{( a ) ~} 0 , 2 ,-1} \\ {0} \\ {0} \\ \end{array} \right]} \\ {\mathrm{( f ) ~} P=\left[ \begin{array} {c c c} {1} & {0} & {-2} \\ {0} & {1} & {0} \\ {0} & {0} & {1} \\ \end{array} \right] , D=\left[ \begin{array} {c} {0} & {\mathrm{( a ) ~} 0 , 2 ,-1} \\ {2} & {\mathrm{~} 0} \\ {1} \\ \end{array} \right]} \\ \end{array}
$$

Exercise 5-3. [Diagonalisation of matrix, Slides 128] Rerpeat the previous exercise with

$$
A=\left[ \begin{array} {c c c c} {1} & {0} & {1} & {0} \\ {1} & {1} & {1} & {0} \\ {0} & {0} & {0} & {0} \\ {1} & {0} & {1} & {0} \\ \end{array} \right]
$$

$$
\mathrm{( c ) ~ F o r ~} \lambda=0 , \left[ \begin{array} {r} {-1} \\ {0} \\ {1} \\ {0} \\ \end{array} \right] , \left[ \begin{array} {r} {0} \\ {0} \\ {0} \\ {1} \\ \end{array} \right] ; \mathrm{~ f o r ~} \lambda=1 , \left[ \begin{array} {r} {0} \\ {1} \\ {0} \\ {0} \\ \end{array} \right] \left] \right]
$$

Exercise
$$
5 \mathrm{-} 4 . \ \mathrm{L e t} \ A=\left[ \begin{array} {r r r} {0} & {0} & {-2} \\ {1} & {2} & {1} \\ {1} & {0} & {3} \\ \end{array} \right] .
$$

(a) Verify that $\lambda_{1}$ . $\mathbf{v}_{1}={\left[ \begin{array} {l l l} {-1} & {0} & {1} \\ \end{array} \right]}^{T}$ is an eigenvector of $\mathit{A}$ , and also find its corspond-ing eigenvalue

b)The eigervalue $\lambda_{1}$ in pat a) asanohe eienvetor $\mathbf{v}_{2}$ . Find $\mathbf{v}_{2}$ .

(c) Are the vectors $\mathbf{v}_{1}$ in part (a) and $\mathbf{v}_{2}$ in part $\mathrm{( b )}$ linearly independent? Justify your answer.

(d) Hence, or otherwise, show that the matrix $\mathit{A}$ can be expressed at $A \,=\, P D P^{-1} .$ State the numerical values of $\mathit{P}$ and $\mathit{D}$ matrices and find $P^{-1} \, \mathrm{~ b y}$ using the ERO (Elementary Row Operation) method.

(e)Denote $D$ ） $\mathit{P}$ and $P^{-1}$ in part $\mathrm{( c )}$ as

$$
D=\left[ \begin{array} {c c c} {\lambda_{1}} \\ {} & {\lambda_{2}} \\ {} & {} & {\lambda_{3}} \\ \end{array} \right] , \quad P=\left[ \begin{array} {c c c} {\mathbf{v}_{1}} & {\mathbf{v}_{2}} & {\mathbf{v}_{3}} \\ \end{array} \right] , \quad\mathrm{a n d} \quad P^{-1}=\left[ \begin{array} {c} {\mathbf{u}_{1}^{T}} \\ {\mathbf{u}_{2}^{T}} \\ {\mathbf{u}_{3}^{T}} \\ \end{array} \right] .
$$

DOI $\mathit{A}$ as a linear combination of rank one matrices $\mathbf{v}_{i} \mathbf{u}_{i}^{T} , \, \, i=1 , 2 , 3 .$  You need compute numerically the rank one matrice.

Exercise 5-5. |Eigenvalues and Eigenvectors of Block Triangular Matrix] $\overbrace{\Im}$ d In an earlier Tutorial, we studied the determinant of block triangular matrices. We sh
出北中全中司 $A$ . $B$ and $C$ have dimensions $n \times n$ is the block partitioned matrix $\left[ \begin{array} {c c} {A} & {C} \\ {0} & {B} \\ \end{array} \right]$ and the
 $\operatorname* {d e t} ( P )=\operatorname* {d e t} ( A ) \operatorname* {d e t} ( B )$ where $\mathit{P}$ 
. $m \times m$ and $n \times m$ rospectively.

What can you say about the cigenvalues and eigenvectors of $P ?$ State all assumptions made.

With the help of MATLAB,verify that your conclusion with the following numerical example (or any numerical exanmple of your own)

$$
A=\left[ \begin{array} {r r r r} {3} & {2} & {0} & {2} \\ {6} & {8} & {2} & {1} \\ {0} & {0} & {4} & {7} \\ {0} & {0} & {2} & {5} \\ \end{array} \right] , \quad B=\left[ \begin{array} {r r r} {-6} & {4} & {5} \\ {2} & {8} & {2} \\ {-1} & {-4} & {2} \\ \end{array} \right] , \quad C=\left[ \begin{array} {r r r} {1 2} & {6} & {1} \\ {4} & {4} & {1} \\ {7} & {4} & {3} \\ {8} & {8} & {3} \\ \end{array} \right]
$$

If $\mathbf{v_{A}}$ ugmeaue 公uode  $\mathit{P}$ are the eigenvalues of $\mathit{A}$ and $B$ 
 $\mathit{A}$ satisfy $( \lambda_{A}^{2}-1 1 \lambda_{A}+1 2 ) ( \lambda_{A}^{2}-9 \lambda_{A}+6 )=0 ;$  $\left[ \begin{array} {c} {{\bf v_{A}}} \\ {0} \\ \end{array} \right]$ 
Eigenvalues of $B$ satisfy $\lambda_{B}^{3}-4 \lambda_{B}^{2}-3 9 \lambda_{B}+1 6 8=0$ and v: are eigenvectors of $\mathit{A}$ and $B$ respectively, then
$$
\left[ \begin{array} {c} {( \lambda_{B} I-A )^{-1} C \mathbf{v}_{\mathbf{B}}} \\ {\mathbf{v}_{\mathbf{B}}} \\ \end{array} \right] \; \left] \begin{array} {c} {\mathbf{v}_{\mathbf{B}}} \\ \end{array} \right]
$$

## IE2107 Tutorial 6 Linear Algebra: Applications

## Exercise 6-1. [System of Linear Differential Equations, Slides 132-137

Sole thealon aicnial aualion

$$
\frac{d \mathbf{u}} {d t}=A \mathbf{u}
$$

$$
\mathrm{w h e r e}
$$

$$
A=\left[ \begin{array} {r r r} {0} & {-1} & {0} \\ {1} & {0} & {-1} \\ {0} & {1} & {0} \\ \end{array} \right] ,
$$

and isaveto of aporiate dimensions

In acdition, find a time $\mathit{T}$ at which the solution $\mathbf{u} ( t )$ is equal to the initial value ${\bf u} ( 0 )$ Justify your answer.

Exercise $8-2$ . [Application, system of linear first order differential equations Two brine storage tanks are connected with two pipes used to exchange solutions between them. The first pipe allows water from tank 1 to enter tank $2$ at a rate of $5$ litre/min. The second pipe reverses the process allowing water to flow from tank $2$ to tank $1$ , also at a rate of $5$ litre/min. Initially, the first tank contains a wel-mixed solution of $8$ kg of salt in $5 0$ litre of water, while the second tank contains 100 litre of pure water.

(a) Develop a mathermnatical model to describe the amount of sat in ec tank at time t.

b) tetern t anoutifatin eat tankatadt tate and eplinthe resul

(b) $\frac{8} {3}$ and $\frac{1 6} {3}$ [(a) 公
$$
\begin{array} {l} {( t )} \\ {( t )} \\ \end{array} {}=\left[ \begin{array} {r r} {-\frac{5} {5 0}} & {\frac{5} {1 0 0}} \\ {\frac{5} {5 0}} & {-\frac{5} {1 0 0}} \\ \end{array} \right] \left[ \begin{array} {c} {y_{1} ( t )} \\ {y_{2} ( t )} \\ \end{array} \right] \, \mathrm{w i t h} \ y_{1} ( 0 )=8 , y_{2} ( 0 )=0
$$
mixed and divided
4n
at
at
eventually be thoroughly
proportionally between the two tanks in a ratio of 1:2. ## Exercise 6-3. [State Transition Matrix, Steady State condition

味 $2 5$ 5业0 $\mathrm{A , \ B}$ , o A group of insurance plan allows three different options for
 $\mathrm{C}$ total number of participants enrolled in each plan
percent, 30 percent, and.45 past experience

(a) $1 5$ percent and 10 percent of the participants who originally enrolled in plan $\mathrm{A}$ will switch to plan $\mathrm{B}$ and plan $\mathrm{C}$ respectively.
(b) 25 percent and 30 percent of the participants who originally enroled in plan $\mathrm{B}$ will switch to plan $\mathrm{A}$ and plan $\mathrm{C}$ respectively.
(0) $2 0$ percent and.40 percent of the participants who originally enrolled in plan $\mathrm{C}$ will switch to plan $\mathrm{A}$ and plan B respectively.

Construct a mathematical modiel for this system, and hence determine, in the long term, the percentage of enrollment in each plan.

$$
[ \; \ T=\left[ \begin{array} {c c c} {0 . 7 5} & {0 . 2 5} & {0 . 2} \\ {0 . 1 5} & {0 . 4 5} & {0 . 4} \\ {0 . 1} & {0 . 3} & {0 . 4} \\ \end{array} \right] ; \, \mathrm{P l a n ~ A ~ 4 7 . 7 3 Y_0^\prime, ~ P l a n ~ B ~ 2 9 . 5 4 Y_0 , ~ P l a n ~ C ~ 2 2 . 7 3 Y_0 ~} \; ]
$$

Exercise 6-4. Let $x_{k+1}=A x_{k} , \quad k=0 , 1 , 2 , \ldots,$ where

$$
A=\left[ \begin{array} {r r r} {3} & {-1} & {1} \\ {-2} & {4} & {2} \\ {-1} & {1} & {5} \\ \end{array} \right] , \quad x_{0}=\left[ \begin{array} {c} {c_{1}} \\ {c_{2}} \\ {c_{3}} \\ \end{array} \right] , \mathrm{~ a n d ~} c_{1} , \ c_{2} , \ c_{3} \mathrm{~ a r e ~ u n k n o w n ~ r e a l ~ c o n s t a n t s .}
$$

ae inthe iganales and cganetors ofth mari $\mathit{A}$ .

(b) Derive an expression for $x_{k}$ as a linear combination of the eigenvectors you obtained in part (a)
