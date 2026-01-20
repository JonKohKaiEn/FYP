# Complex Numbers

## Fundamentals of Complex Numbers

### Definition and Geometric Representation
A complex number $z$ is defined as $z = x + iy$, where $x$ is the real part ($\text{Re}(z)$), $y$ is the imaginary part ($\text{Im}(z)$), and $i = \sqrt{-1}$. Geometrically, it is represented as a point $(x, y)$ or a vector in the complex plane, also known as the Argand diagram. The horizontal axis represents the real components, while the vertical axis represents the imaginary components.

### Modulus and Argument
The modulus $r = |z|$ represents the magnitude or length of the vector and is calculated as $r = \sqrt{x^2 + y^2}$. The argument $\theta = \arg(z)$ is the angle the vector makes with the positive real axis, calculated as $\theta = \arctan(y/x)$ in radians. The principal value $\text{Arg}(z)$ is restricted to the range $-\pi < \text{Arg}(z) \le \pi$, and the general argument is $\arg(z) = \text{Arg}(z) + 2n\pi$ for $n = 0, \pm 1, \pm 2, \dots$.

### Complex Conjugate
The complex conjugate of $z = x + iy$ is denoted as $\bar{z} = x - iy$. Geometrically, it is a reflection of $z$ across the real axis. Key properties include:
*   $\text{Re}(z) = \frac{1}{2}(z + \bar{z})$
*   $\text{Im}(z) = \frac{1}{2i}(z - \bar{z})$
*   $z\bar{z} = x^2 + y^2 = |z|^2$
*   $\overline{z_1 \pm z_2} = \bar{z}_1 \pm \bar{z}_2$
*   $\overline{z_1 z_2} = \bar{z}_1 \bar{z}_2$

## Euler's Formula and Algebraic Operations

### Euler's Formula and Polar Form
Euler's formula states that $e^{i\theta} = \cos\theta + i\sin\theta$. This allows complex numbers to be written in polar form as $z = re^{i\theta}$ or $z = r\angle\theta$. From this formula, trigonometric functions can be expressed as:
*   $\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$
*   $\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$

### Arithmetic Operations
Complex arithmetic can be performed in different forms:
*   **Addition and Subtraction:** Most convenient in rectangular form: $z_1 \pm z_2 = (x_1 \pm x_2) + i(y_1 \pm y_2)$.
*   **Multiplication:** In rectangular form, $z_1 z_2 = (x_1 x_2 - y_1 y_2) + i(x_1 y_2 + x_2 y_1)$. In polar form, magnitudes are multiplied and angles are added: $z_1 z_2 = r_1 r_2 \angle(\theta_1 + \theta_2)$.
*   **Division:** In rectangular form, it involves multiplying the numerator and denominator by the conjugate of the denominator. In polar form, magnitudes are divided and angles are subtracted: $\frac{z_1}{z_2} = \frac{r_1}{r_2} \angle(\theta_1 - \theta_2)$.

## De Moivre's Formula and Roots

### De Moivre's Formula
De Moivre's formula states that for any integer $n$, $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$. In polar form, this is expressed as $z^n = r^n \angle(n\theta)$. This formula is a powerful tool for deriving trigonometric identities and calculating powers of complex numbers.

### Roots of Complex Numbers
The $n$-th roots of a complex number $z = r\angle\theta$ are given by $w_k = \sqrt[n]{r} \angle \left( \frac{\theta + 2k\pi}{n} \right)$ for $k = 0, 1, \dots, (n-1)$. Geometrically, the set of $n$ roots lies on the vertices of a regular polygon with $n$ sides, inscribed within a circle of radius $\sqrt[n]{r}$ centered at the origin.

## Complex Functions

### Exponential Function
The complex exponential function $e^z$ is defined by the power series $\sum_{n=0}^{\infty} \frac{1}{n!} z^n$. It can be expressed as $e^z = e^{x+iy} = e^x(\cos y + i\sin y)$. This function is periodic with a period of $2\pi i$.

### Complex Logarithm and General Power
The natural logarithm of a complex number is defined as the inverse of the exponential function: $\ln z = \ln r + i\theta$, where $z \neq 0$. Because the argument $\theta$ is multi-valued, the complex logarithm is also infinitely many-valued. The general power of a complex number $z^c$ is defined using the complex logarithm as $z^c = e^{c \ln z}$.