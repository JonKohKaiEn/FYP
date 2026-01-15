# 2 - Complex Numbers

## 1. Definitions and Basic Concepts
Complex numbers extend the real number system to allow for solutions to equations like $x^2 + 1 = 0$.

### 1.1 The Complex Number $z$
A complex number $z$ is defined as:
$$z = x + iy$$
where $i = \sqrt{-1}$.
*   **$x = \text{Re}(z)$**: The real part of $z$.
*   **$y = \text{Im}(z)$**: The imaginary part of $z$.

### 1.2 The Argand Diagram (Complex Plane)
Geometrically, a complex number is represented as a point or a vector in a 2D plane where the horizontal axis is the **real axis** and the vertical axis is the **imaginary axis**.
*   **Modulus ($r$ or $|z|$)**: The distance from the origin to the point $(x, y)$.
    $$r = |z| = \sqrt{x^2 + y^2}$$
*   **Argument ($\theta$ or $\arg(z)$)**: The angle the vector makes with the positive real axis.
    $$\theta = \arg(z) = \arctan\left(\frac{y}{x}\right) \text{ radians}$$
*   **Principal Value ($\text{Arg}(z)$)**: The unique value of the argument such that $-\pi < \text{Arg}(z) \le \pi$. The general argument is $\arg(z) = \text{Arg}(z) + 2n\pi$ for $n = 0, \pm 1, \pm 2, \dots$.

### 1.3 Complex Conjugate
The complex conjugate of $z = x + iy$ is denoted by $\bar{z}$ and is defined as:
$$\bar{z} = x - iy$$
In the Argand diagram, $\bar{z}$ is the reflection of $z$ across the real axis.

---

## 2. Euler's Formula and Polar Form
Euler's formula provides a fundamental link between trigonometric functions and complex exponential functions.

### 2.1 Euler's Formula
$$e^{i\theta} = \cos\theta + i\sin\theta$$
From this, we can derive expressions for sine and cosine:
$$\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \quad \sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$$

### 2.2 Polar Form
Using the modulus $r$ and argument $\theta$, a complex number can be written in polar form:
$$z = r(\cos\theta + i\sin\theta) = re^{i\theta} = r\angle\theta$$

---

## 3. Algebraic Rules
Operations on complex numbers can be performed in either rectangular or polar form.

### 3.1 Rectangular Form Operations
Given $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$:
*   **Addition/Subtraction**: $z_1 \pm z_2 = (x_1 \pm x_2) + i(y_1 \pm y_2)$
*   **Multiplication**: $z_1z_2 = (x_1x_2 - y_1y_2) + i(x_1y_2 + x_2y_1)$
*   **Division**: $\frac{z_1}{z_2} = \frac{x_1x_2 + y_1y_2}{x_2^2 + y_2^2} + i\frac{x_2y_1 - x_1y_2}{x_2^2 + y_2^2}$

### 3.2 Polar Form Operations
Multiplication and division are significantly simpler in polar form:
*   **Multiplication**: $z_1z_2 = r_1r_2\angle(\theta_1 + \theta_2)$
*   **Division**: $\frac{z_1}{z_2} = \frac{r_1}{r_2}\angle(\theta_1 - \theta_2)$

### 3.3 Properties of the Conjugate
*   $\text{Re}(z) = \frac{1}{2}(z + \bar{z})$
*   $\text{Im}(z) = \frac{1}{2i}(z - \bar{z})$
*   $z\bar{z} = |z|^2$
*   $\overline{z_1 \pm z_2} = \bar{z}_1 \pm \bar{z}_2$
*   $\overline{z_1 z_2} = \bar{z}_1 \bar{z}_2$

---

## 4. De Moivre's Formula
De Moivre's formula is used for raising complex numbers to an integer power $n$.
$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$
This formula is highly useful for deriving trigonometric identities, such as expressing $\cos(n\theta)$ or $\sin(n\theta)$ in terms of powers of $\cos\theta$ and $\sin\theta$.

---

## 5. Roots of Complex Numbers
To find the $n$-th roots of a complex number $z = r\angle\theta$, we solve $w^n = z$.

### 5.1 Root Formula
The $n$ distinct roots $w_k$ are given by:
$$w_k = \sqrt[n]{z} = \sqrt[n]{r} \angle \left( \frac{\theta + 2k\pi}{n} \right), \quad k = 0, 1, \dots, (n-1)$$

### 5.2 Geometric Interpretation
Geometrically, the $n$ roots of a complex number lie on a circle of radius $\sqrt[n]{r}$ and form the vertices of a **regular polygon** with $n$ sides. For example, the three cube roots of a number form an equilateral triangle.

---

## 6. Complex Functions

### 6.1 Exponential Function
The complex exponential function $e^z$ is defined by the power series:
$$e^z = \sum_{n=0}^{\infty} \frac{1}{n!}z^n = e^x(\cos y + i\sin y)$$
Notable values include $e^{i\pi} = -1$ and $e^{i2\pi} = 1$.

### 6.2 Complex Logarithm
The natural logarithm $\ln z$ is the inverse of the exponential function ($e^w = z$):
$$\ln z = \ln r + i(\theta + 2n\pi)$$
Because the argument $\theta$ is multi-valued, the complex logarithm is also **infinitely many-valued**.

### 6.3 General Power
The general power of a complex number $z^c$ is defined using the complex logarithm:
$$z^c = e^{c \ln z}, \quad z \neq 0$$
Since $\ln z$ is multi-valued, $z^c$ is generally multi-valued as well. The **principal value** is obtained by using the principal value of the argument ($\text{Arg}(z)$).