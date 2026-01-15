# 4 - Complex Integration

## 1. Introduction to Complex Line Integrals

### Definition and Notation
A complex definite integral, or line integral, denoted as $\int_C f(z) dz$, represents integration performed along a curve $C$ (the contour or path of integration) in the complex plane.
*   If $C$ is a closed contour, it is denoted as $\oint_C f(z) dz$.
*   If the path $C$ lies entirely on the real axis, then $z = x$, and the integral reduces to a standard real definite integral $\int_a^b f(x) dx$.

### Parametric Representation of Contours
A contour $C$ in the complex plane is typically represented parametrically by a real parameter $t$:
$$z(t) = x(t) + iy(t), \quad a \le t \le b$$
The direction of the path follows increasing values of $t$.

**Theorem 1: Integration by Use of the Path**
If $C$ is a piecewise smooth path represented by $z = z(t)$ for $a \le t \le b$, and $f(z)$ is continuous on $C$, then:
$$\int_C f(z) dz = \int_a^b f[z(t)] \frac{dz}{dt} dt$$

### Basic Properties of Complex Line Integrals
1.  **Linearity:** $\int_C [k_1 f_1(z) + k_2 f_2(z)] dz = k_1 \int_C f_1(z) dz + k_2 \int_C f_2(z) dz$
2.  **Subdivision of Path:** $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$ (where $C$ is composed of $C_1$ and $C_2$)
3.  **Sense of Integration:** $\int_{z_1}^{z_2} f(z) dz = -\int_{z_2}^{z_1} f(z) dz$

---

## 2. Cauchy’s Integral Theorem

### Simple Closed Paths and Simply Connected Domains
*   **Simple Closed Path:** A path that does not intersect or touch itself (e.g., a circle or a simple loop). A "not simple" path intersects itself (e.g., a figure-eight).
*   **Simply Connected Domain ($D$):** A domain where every simple closed path in $D$ encloses only points belonging to $D$. Intuitively, it is a domain without "holes."
*   **Multiply Connected Domain:** A domain that contains one or more "holes" (e.g., doubly connected has one hole, triply connected has two holes).

### Cauchy’s Integral Theorem (Theorem 2)
If $f(z)$ is analytic in a simply connected domain $D$, then for every simple closed path $C$ in $D$:
$$\oint_C f(z) dz = 0$$
*Example:* $\oint_C e^z dz = 0$ and $\oint_C \cos z dz = 0$ for any closed path because these functions are entire (analytic everywhere).

### Independence of Path (Theorem 3)
If $f(z)$ is analytic in a simply connected domain $D$, the integral of $f(z)$ between two points $z_1$ and $z_2$ is independent of the path taken within $D$.
*   **Proof Sketch:** For two paths $C_1$ and $C_2$ from $z_1$ to $z_2$, forming a closed loop $C_1 - C_2$, Cauchy's theorem states $\int_{C_1} f dz + \int_{C_2^*} f dz = 0$ (where $C_2^*$ is the reverse of $C_2$). Thus, $\int_{C_1} f dz = \int_{C_2} f dz$.

### Cauchy’s Theorem for Multiply Connected Domains
If $f(z)$ is analytic in a region bounded by an outer contour $C$ and several inner contours $C_1, C_2, ..., C_n$ (all oriented positively/counter-clockwise), then:
$$\oint_C f(z) dz = \sum_{k=1}^n \oint_{C_k} f(z) dz$$
This allows "shrinking" a complex contour around singular points where the function is not analytic.

---

## 3. Cauchy’s Integral Formula

### The General Formula (Theorem 4)
Cauchy's Integral Formula is used to evaluate integrals where the integrand has a singularity (a point where it is not analytic) inside the contour.
If $f(z)$ is analytic in a simply connected domain $D$, then for any point $z_0$ in $D$ enclosed by a simple closed path $C$:
$$\oint_C \frac{f(z)}{z - z_0} dz = 2\pi i f(z_0)$$

**General Form for Derivatives:**
$$\oint_C \frac{f(z)}{(z - z_0)^m} dz = \frac{2\pi i}{(m - 1)!} f^{(m-1)}(z_0), \quad m = 1, 2, 3, ...$$
*Note: Integration is assumed to be counter-clockwise.*

---

## 4. Applications to Real Integrals

### Evaluation of Real Trigonometric Integrals
Complex integration can evaluate real integrals of the form $\int_0^{2\pi} F(\cos \theta, \sin \theta) d\theta$.
**Method:**
Let $z = e^{i\theta}$. As $\theta$ goes from $0$ to $2\pi$, $z$ moves around the unit circle $C$ counter-clockwise.
*   $\cos \theta = \frac{z + z^{-1}}{2}$
*   $\sin \theta = \frac{z - z^{-1}}{2i}$
*   $dz = i e^{i\theta} d\theta \implies d\theta = \frac{dz}{iz}$
The integral becomes: $\oint_C f(z) \frac{1}{iz} dz$.

### Improper Integrals of Rational Functions
Complex integration evaluates $\int_{-\infty}^{\infty} f(x) dx$ where $f(x) = \frac{p(x)}{q(x)}$ under two conditions:
1.  $f(x)$ is a real function with no common factors, and $q(x) \neq 0$ for all real $x$.
2.  $\text{Degree of } q(x) \ge \text{Degree of } p(x) + 2$.

**Method:**
The real integral is evaluated by closing the path with a large semi-circle in the Upper Half Plane (UHP):
$$\int_{-\infty}^{\infty} f(x) dx = \oint_{\text{UHP}} f(z) dz = \sum_{k=1}^n \oint_{C_k \text{ in UHP}} f(z) dz$$
The result is determined by the residues of the poles located specifically in the Upper Half Plane.