# Complex Integration

## Fundamentals of Complex Line Integrals

### Definition and Parametric Representation
A complex definite integral, or line integral, denoted as $\int_C f(z) dz$, is evaluated along a curve $C$ (the contour or path of integration) in the complex plane. If the contour is closed, it is denoted by $\oint_C f(z) dz$. A contour can be represented parametrically as $z(t) = x(t) + iy(t)$ for $a \le t \le b$, where $t$ is a real parameter. This establishes a continuous mapping from the interval $[a, b]$ to the $z$-plane, with the direction of the path determined by increasing values of $t$.

### Evaluation Method
The practical method to evaluate a complex line integral involves substituting the parametric representation into the integral. For a continuous function $f(z)$ on a piecewise smooth path $C$ represented by $z = z(t)$, the integral is calculated as:
$$\int_C f(z) dz = \int_a^b f[z(t)] \frac{dz}{dt} dt$$

### Basic Properties of Complex Line Integrals
Complex line integrals follow three fundamental properties:
1.  **Linearity:** $\int_C [k_1 f_1(z) + k_2 f_2(z)] dz = k_1 \int_C f_1(z) dz + k_2 \int_C f_2(z) dz$
2.  **Subdivision of Path:** $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$, where $C$ is the union of paths $C_1$ and $C_2$.
3.  **Sense of Integration:** $\int_{z_1}^{z_2} f(z) dz = -\int_{z_2}^{z_1} f(z) dz$

## Topology of the Complex Plane

### Simple Closed Paths
A simple closed path is a contour that starts and ends at the same point without intersecting or touching itself at any other point. Diagrams distinguish "Simple" paths (single loops without self-intersection) from "Not Simple" paths (figures that cross over themselves, such as a figure-eight).

### Simply and Multiply Connected Domains
A simply connected domain $D$ is a region where every simple closed path encloses only points that are also within $D$; intuitively, it is a domain without "holes." A domain that is not simply connected is called multiply connected. These are classified by the number of holes: "Doubly Connected" (one hole) or "Triply Connected" (two holes).

## Cauchy’s Integral Theorems and Formulas

### Cauchy’s Integral Theorem
If a function $f(z)$ is analytic in a simply connected domain $D$, then for every simple closed path $C$ in $D$:
$$\oint_C f(z) dz = 0$$
This theorem implies that the integral of an entire function (analytic for all $z$) over any closed path is always zero.

### Independence of Path
In a simply connected domain $D$ where $f(z)$ is analytic, the line integral between two points $z_1$ and $z_2$ is independent of the path taken. This is a direct consequence of Cauchy's Integral Theorem, as the integral over a closed loop formed by two different paths must sum to zero.

### Cauchy’s Integral Formula
This formula allows the evaluation of integrals where the integrand has singularities. If $f(z)$ is analytic in a simply connected domain $D$, then for any point $z_0$ enclosed by a simple closed path $C$ in $D$:
$$\oint_C \frac{f(z)}{z - z_0} dz = 2\pi i f(z_0)$$
The general version for higher-order derivatives is:
$$\oint_C \frac{f(z)}{(z - z_0)^m} dz = \frac{2\pi i}{(m - 1)!} f^{(m-1)}(z_0), \text{ where } m = 1, 2, 3, \dots$$

### Extension to Multiply Connected Domains
For a multiply connected domain with an outer boundary $C$ and inner boundaries $C_1, C_2, \dots, C_n$ (all positively oriented), if $f(z)$ is analytic in the region between them, the integral over the outer boundary equals the sum of the integrals over the inner boundaries:
$$\oint_C f(z) dz = \sum_{k=1}^n \oint_{C_k} f(z) dz$$

## Applications to Real Integrals

### Evaluation of Trigonometric Integrals
Real integrals of the form $\int_0^{2\pi} F(\cos \theta, \sin \theta) d\theta$ can be evaluated by transforming them into complex line integrals around a unit circle $C$ using the substitution $z = e^{i\theta}$. The following relations are used:
*   $\cos \theta = \frac{z + z^{-1}}{2}$
*   $\sin \theta = \frac{z - z^{-1}}{2i}$
*   $d\theta = \frac{dz}{iz}$

### Improper Integrals of Rational Functions
Complex integration can evaluate real improper integrals $\int_{-\infty}^{\infty} f(x) dx$ by considering a contour in the Upper Half Plane (UHP). This method is valid if:
1.  $f(x) = \frac{p(x)}{q(x)}$ is a real rational function where $q(x) \ne 0$ for all real $x$.
2.  The degree of the denominator $q(x)$ is at least two greater than the degree of the numerator $p(x)$ ($\text{deg}(q) \ge \text{deg}(p) + 2$).
The relationship is defined as:
$$\int_{-\infty}^{\infty} f(x) dx = \oint_{\text{UHP}} f(z) dz = \sum_{k=1}^n \oint_{C_k \text{ in UHP}} f(z) dz$$