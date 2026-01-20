# Differentiation of Complex Functions

## Complex Functions

### Definition and Mapping
A complex function $f$ is a rule or mapping that assigns every complex number $z$ in a set $S$ (domain) to a complex number $w$ in a set $T$ (range). Mathematically, this is expressed as $w = f(z)$. Given $z = x + iy$ and $w = u + iv$, the function can be decomposed into real and imaginary parts: $w = f(z) = u(x, y) + iv(x, y)$.

### Diagram Interpretation: Mapping Process
The provided diagram illustrates the transformation of a point $z$ from the $z$-plane to a point $w$ in the $w$-plane. The $z$-plane represents the domain of the function $f$, while the $w$-plane represents the range. The arrow indicates the mapping $w = f(z)$, showing how a region in the complex domain is transformed into a corresponding region in the complex range.

## Limit and Continuity

### Limit of a Complex Function
A function $f(z)$ has a limit $L$ as $z$ approaches $z_0$ if $f(z)$ is defined in the neighborhood of $z_0$ and approaches the same complex number $L$ from all possible directions. Formally, $\lim_{z \to z_0} f(z) = L$ if for every $\epsilon > 0$, there exists a $\delta > 0$ such that $|f(z) - L| < \epsilon$ whenever $0 < |z - z_0| < \delta$.

### Continuity
A function $f(z)$ is continuous at $z = z_0$ if it satisfies three conditions: $f(z_0)$ exists, the limit $\lim_{z \to z_0} f(z)$ exists, and $\lim_{z \to z_0} f(z) = f(z_0)$. A function is considered continuous over a domain $S$ if it is continuous at every point within that domain.

## Differentiability and Analyticity

### Derivatives of Complex Functions
The derivative of a complex function $f$ at a point $z_0$, denoted as $f'(z_0)$, is defined by the limit:
$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$
Standard differentiation rules from real calculus, such as the power rule $\frac{d}{dz}(z^n) = nz^{n-1}$, generally apply to complex functions, provided the limit exists and is independent of the path taken by $\Delta z$.

### Analytic Functions
A function $f(z)$ is analytic at a point $z_0$ if its derivative exists at $z_0$ and at every point in some neighborhood of $z_0$. Analyticity is a stronger condition than differentiability at a single point and implies both differentiability and continuity throughout a region. A point where a function fails to be analytic is called a singular point or a singularity.

## Cauchy-Riemann Equations

### Testing for Analyticity
The Cauchy-Riemann (C-R) equations provide a necessary condition for a function $f(z) = u(x, y) + iv(x, y)$ to be analytic. For a function to be analytic at $z_0$, the partial derivatives of $u$ and $v$ must exist, be continuous, and satisfy:
$u_x = v_y$ and $v_x = -u_y$
In polar coordinates $(r, \theta)$, the C-R equations are expressed as:
$u_r = \frac{1}{r}v_\theta$ and $v_r = -\frac{1}{r}u_\theta$

### Derivative Expressions via C-R Equations
If a function is differentiable, its derivative can be calculated using the partial derivatives of its real and imaginary components:
$f'(z) = u_x + iv_x = v_y - iu_y$
In polar form, the derivative is given by:
$f'(z) = e^{-i\theta}(u_r + iv_r) = \frac{1}{r}e^{-i\theta}(v_\theta - iu_\theta)$

### Common Analytic Functions
Certain classes of functions possess inherent analyticity:
*   **Polynomials:** Functions of the form $f(z) = c_0 + c_1z + \dots + c_nz^n$ are analytic everywhere in the complex plane.
*   **Rational Functions:** Quotients of polynomials $f(z) = \frac{g(z)}{h(z)}$ are analytic everywhere except at points where the denominator $h(z) = 0$.
*   **Partial Fractions:** Functions of the form $f(z) = \frac{c}{(z - z_0)^m}$ are analytic everywhere except at the point $z_0$.