# 3 - Complex Differentiation

## 1. Complex Functions
### Definition and Mapping
A complex function $f$ is a rule or mapping that assigns every complex number $z$ in a set $S$ (the domain) to a complex number $w$ in a set $T$ (the range).
*   **Mathematical Expression:** $w = f(z)$
*   **Diagram Interpretation:** The notes illustrate this as a mapping from the **$z$-plane** (with axes $x$ and $y$) to the **$w$-plane** (with axes $u$ and $v$). A point $z$ in a region of the $z$-plane is transformed into a point $w$ in the $w$-plane.

### Real and Imaginary Components
Any complex function can be decomposed into its real and imaginary parts, which are themselves real-valued functions of two variables ($x$ and $y$):
$$w = f(z) = u(x, y) + iv(x, y)$$
Where:
*   $z = x + iy$
*   $u(x, y)$ is the real part.
*   $v(x, y)$ is the imaginary part.

---

## 2. Limits and Continuity
### Limit of a Complex Function
A function $f(z)$ has a limit $L$ as $z$ approaches $z_0$ ($\lim_{z \to z_0} f(z) = L$) if:
1.  $f(z)$ is defined in the neighborhood of $z_0$ (except possibly at $z_0$ itself).
2.  $f(z)$ approaches the same complex number $L$ from **all directions** within its neighborhood.

**Formal Definition ($\epsilon-\delta$):**
For any $\epsilon > 0$, there exists a $\delta > 0$ such that:
$$|f(z) - L| < \epsilon \text{ whenever } 0 < |z - z_0| < \delta$$

**Path Dependency:** If the limit depends on the direction of approach (e.g., approaching along the real axis vs. the imaginary axis), the limit does not exist.

### Continuity
A function $f(z)$ is continuous at $z = z_0$ if it satisfies three conditions:
1.  $f(z_0)$ exists.
2.  $\lim_{z \to z_0} f(z)$ exists.
3.  $\lim_{z \to z_0} f(z) = f(z_0)$.

A function is called a **continuous function** if it is continuous for all $z$ in its domain $S$.

---

## 3. Derivatives of Complex Functions
### Definition of the Derivative
The derivative of a complex function $f$ at a point $z_0$, denoted $f'(z_0)$, is defined as:
$$f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}$$
Alternatively, using $\Delta z$:
$$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$

### Differentiation Rules
Standard differentiation formulas from real calculus apply to complex variables:
*   $\frac{d}{dz}(c) = 0$
*   $\frac{d}{dz}(z) = 1$
*   $\frac{d}{dz}(z^n) = nz^{n-1}$
*   **Chain Rule Example:** $\frac{d}{dz}(2z^2 + i)^5 = 5(2z^2 + i)^4 \cdot 4z = 20z(2z^2 + i)^4$

**Important Note:** Some functions, like the complex conjugate $f(z) = \bar{z}$, are **not differentiable anywhere** because the limit depends on the angle $\theta$ of approach.

---

## 4. Analytic Functions
### Definition
A function $f(z)$ is **analytic** at a point $z_0$ if its derivative exists not only at $z_0$ but also in some neighborhood of $z_0$.
*   **Analyticity in Domain $D$:** The function is analytic at every point in $D$.
*   **Singular Point (Singularity):** A point $z = z_0$ where $f(z)$ ceases to be analytic.
*   **Implication:** Analyticity $\implies$ Differentiability $\implies$ Continuity.

---

## 5. Cauchy-Riemann (C-R) Equations
The Cauchy-Riemann equations provide a necessary condition for a function to be analytic.

### Cartesian Form
For a function $f(z) = u(x, y) + iv(x, y)$, the C-R equations are:
$$u_x = v_y \quad \text{and} \quad v_x = -u_y$$
Where $u_x = \frac{\partial u}{\partial x}$, etc. If these partial derivatives are continuous and satisfy these equations in a domain $D$, then $f(z)$ is analytic in $D$.

### Polar Form
When $z \neq 0$, using $z = re^{i\theta}$, the C-R equations are:
$$u_r = \frac{1}{r}v_\theta \quad \text{and} \quad v_r = -\frac{1}{r}u_\theta$$

### Calculating the Derivative using C-R
If $f'(z)$ exists, it can be expressed using partial derivatives:
*   **Cartesian:** $f'(z) = u_x + iv_x = v_y - iu_y$
*   **Polar:** $f'(z) = e^{-i\theta}(u_r + iv_r) = \frac{1}{r}e^{-i\theta}(v_\theta - iu_\theta)$

---

## 6. Common Analytic Functions
1.  **Polynomials:** $f(z) = c_0 + c_1z + \dots + c_nz^n$ are analytic everywhere in the complex plane.
2.  **Rational Functions:** $f(z) = \frac{g(z)}{h(z)}$ (where $g, h$ are polynomials) are analytic except at points where $h(z) = 0$.
3.  **Partial Fractions:** Functions of the form $f(z) = \frac{c}{(z - z_0)^m}$ are analytic except at the singular point $z_0$.