# 1 - Linear Algebra

## 1. Systems of Linear Equations and Matrices
This section introduces the fundamental methods for solving linear systems and representing them using matrix notation.

*   **General Form of Linear Systems:** A system of $m$ linear equations in $n$ unknowns is represented as:
    $$\begin{cases} a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2 \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m \end{cases}$$
    There are three possible outcomes for any system: a unique solution, infinitely many solutions, or no solution.
*   **Matrix Notation:** Systems are recorded using a **coefficient matrix** and an **augmented matrix**. For example:
    $$\begin{bmatrix} 1 & -2 & 1 & | & 0 \\ 1 & 0 & -1 & | & 2 \\ 0 & 1 & -4 & | & 4 \end{bmatrix}$$
*   **Elementary Row Operations (EROs):** These operations transform a system into an equivalent one without changing the solution set:
    1. Interchanging two rows ($R_i \leftrightarrow R_j$).
    2. Multiplying a row by a non-zero constant ($R_j \leftarrow \alpha R_j$).
    3. Adding a multiple of one row to another ($R_j \leftarrow R_j + \beta R_i$).
*   **Gaussian Elimination:** A systematic algorithm that uses EROs to convert a matrix into **Row Echelon (RE) form**, followed by **back substitution** to find variables.
*   **Gauss-Jordan Elimination:** Extends Gaussian elimination by transforming the matrix into **Reduced Row Echelon (RRE) form**, where each pivot is 1 and is the only non-zero entry in its column.
*   **Consistency and Rank:** A system is consistent if it has at least one solution.
    *   **Unique solution:** $rank(A|b) = rank(A) = n$ (number of variables).
    *   **Many solutions:** $rank(A|b) = rank(A) < n$.
    *   **No solution:** $rank(A|b) > rank(A)$ (occurs when a row of zeros in $A$ corresponds to a non-zero value in $b$).

## 2. Matrix Algebra
This section covers the arithmetic of matrices and their algebraic properties.

*   **Operations:**
    *   **Addition:** $A + B$ involves adding corresponding entries $a_{ij} + b_{ij}$.
    *   **Scalar Multiplication:** $cA$ multiplies every entry by the scalar $c$.
    *   **Matrix Multiplication:** The $ij$-term of $AB$ is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$: $(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$.
*   **Properties:** Matrix multiplication is **not commutative** ($AB \neq BA$ in general). It is associative and distributive.
*   **Transpose:** The transpose $A^T$ is formed by swapping rows and columns. A matrix is **symmetric** if $A^T = A$.
*   **Inverse of a Matrix:** A square matrix $A$ is invertible (non-singular) if there exists $A^{-1}$ such that $AA^{-1} = I = A^{-1}A$.
    *   For a $2 \times 2$ matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, $A^{-1} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$, provided $ad-bc \neq 0$.
    *   For $n \times n$ matrices, the inverse is found by row-reducing $[A | I]$ to $[I | A^{-1}]$.

## 3. Determinants and LU Factorization
Determinants provide a scalar value that characterizes square matrices, while LU factorization offers an efficient way to solve systems.

*   **Determinants:**
    *   Calculated via **cofactor expansion** along any row or column.
    *   The determinant of a triangular matrix is the product of its diagonal entries.
    *   **Properties:** $\det(AB) = \det(A)\det(B)$; $\det(A^T) = \det(A)$; $A$ is invertible if and only if $\det(A) \neq 0$.
*   **Elementary Matrices:** Matrices obtained by performing a single ERO on the identity matrix. Every ERO can be represented as multiplication by an elementary matrix ($B = EA$).
*   **LU Factorization:** Decomposing a matrix $A$ into a lower triangular matrix $L$ and an upper triangular matrix $U$ ($A = LU$).
    *   Used to solve $Ax = b$ by solving $Ly = b$ (forward substitution) and then $Ux = y$ (back substitution).
    *   If row interchanges are required, it becomes **PLU Factorization**, where $P$ is a permutation matrix.

## 4. Vector Spaces, Span, and Linear Independence
This section moves from algebraic systems to the geometric and structural properties of vectors in $\mathbb{R}^n$.

*   **Linear Combination:** A vector $\mathbf{v}$ is a linear combination of $\{ \mathbf{v}_1, \dots, \mathbf{v}_k \}$ if $\mathbf{v} = c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k$.
*   **Span:** The set of all possible linear combinations of a set of vectors. Geometrically, the span of two non-parallel vectors in $\mathbb{R}^3$ is a plane through the origin.
*   **Linear Independence (LI):** A set of vectors is LI if the only solution to $c_1\mathbf{v}_1 + \dots + c_m\mathbf{v}_m = \mathbf{0}$ is the trivial solution $c_1 = \dots = c_m = 0$. If non-trivial solutions exist, the set is **Linearly Dependent (LD)**.
*   **Orthogonality:** Two vectors $\mathbf{u}, \mathbf{v}$ are orthogonal if their dot product is zero ($\mathbf{u}^T\mathbf{v} = 0$).

## 5. Subspaces, Basis, and Dimension
These concepts define the "skeleton" and size of vector spaces.

*   **Subspace:** A subset $S$ of $\mathbb{R}^n$ that contains the zero vector and is closed under addition and scalar multiplication.
*   **Matrix Spaces:**
    *   **Null Space $N(A)$:** Solutions to $Ax = 0$.
    *   **Column Space $col(A)$:** Span of the columns of $A$.
    *   **Row Space $row(A)$:** Span of the rows of $A$.
*   **Basis:** A set of vectors that is both Linearly Independent and spans the space.
*   **Dimension:** The number of vectors in a basis for a space.
    *   **Rank:** $dim(col(A))$ or $dim(row(A))$.
    *   **Nullity:** $dim(N(A))$.
*   **Rank Theorem:** For an $m \times n$ matrix, $rank(A) + nullity(A) = n$.

## 6. Eigenvalues and Eigenvectors
This section explores the characteristic scaling behavior of linear transformations.

*   **Definitions:** A scalar $\lambda$ is an **eigenvalue** and non-zero vector $\mathbf{v}$ is an **eigenvector** of $A$ if:
    $$A\mathbf{v} = \lambda\mathbf{v}$$
*   **Characteristic Equation:** Eigenvalues are found by solving $\det(\lambda I - A) = 0$.
*   **Diagonalization:** A matrix $A$ is diagonalizable if it can be written as $A = PDP^{-1}$, where $D$ is a diagonal matrix of eigenvalues and $P$ is a matrix whose columns are the corresponding LI eigenvectors.
*   **Applications:**
    *   **Differential Equations:** Solving coupled systems $\dot{\mathbf{x}}(t) = A\mathbf{x}(t)$ using eigenvalues to decouple the equations.
    *   **Dynamical Systems:** Analyzing long-term behavior ($k \to \infty$) of systems $\mathbf{x}_{k+1} = A\mathbf{x}_k$ using $A^\infty = PD^\infty P^{-1}$. If eigenvalues $|\lambda| < 1$, those components vanish over time.