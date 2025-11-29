# Homework Assignment 2 Solutions
## Research Methods: Numerical Methods
### Due November 30, 2025

---

## Exercise 5.1: Householder QR vs Gram-Schmidt

**Problem:** Use Householder reflections to obtain a QR factorization of the matrix A from Example 5.2 and compare with the Gram-Schmidt approach.

**Solution:**

**Matrix A:**
\[
A = \begin{bmatrix}
1 & 1 & 1 \\
0 & 1 & 1 \\
0 & 1 & 0
\end{bmatrix}
\]

**Householder QR Factorization:**

**Step 1:** First column vector: 
\[
\vec{a}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
\]
\[
\|\vec{a}_1\|_2 = 1
\]
\[
\vec{v}_1 = \vec{a}_1 - \|\vec{a}_1\|_2 \vec{e}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} - \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}
\]

Since $\vec{v}_1$ is zero, we skip this step as the first column is already in the desired form.

**Step 2:** Work with submatrix 
\[
A_2 = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}
\]
from rows 2-3, columns 2-3

\[
\vec{a}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
\]
\[
\|\vec{a}_2\|_2 = \sqrt{2}
\]
\[
\vec{v}_2 = \vec{a}_2 - \|\vec{a}_2\|_2 \vec{e}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \begin{bmatrix} \sqrt{2} \\ 0 \end{bmatrix} = \begin{bmatrix} 1-\sqrt{2} \\ 1 \end{bmatrix}
\]

After computation, the Householder transformation yields:

**Q matrix:**
\[
Q = \begin{bmatrix}
1 & 0 & 0 \\
0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
0 & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{bmatrix}
\]

**R matrix:**
\[
R = \begin{bmatrix}
1 & 1 & 1 \\
0 & \sqrt{2} & \frac{1}{\sqrt{2}} \\
0 & 0 & \frac{1}{\sqrt{2}}
\end{bmatrix}
\]

**Comparison:** The Householder QR factorization gives exactly the same Q and R matrices as the Gram-Schmidt method from Example 5.2. However, Householder transformations are numerically more stable, especially for ill-conditioned matrices.

---

## Exercise 6.10: Symmetric Positive Definite Matrices

**Problem:** Suppose A, B ∈ ℝⁿˣⁿ are symmetric and positive definite.

### (a) Define √A and show that (√A)² = A

**Solution:**
Since A is symmetric positive definite, it has an eigenvalue decomposition 
\[
A = Q\Lambda Q^T
\]
where 
\[
\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_n)
\]
with $\lambda_i > 0$.

Define 
\[
\sqrt{A} = Q\sqrt{\Lambda}Q^T
\]
where 
\[
\sqrt{\Lambda} = \text{diag}(\sqrt{\lambda_1}, \ldots, \sqrt{\lambda_n})
\]

Then:
\[
(\sqrt{A})^2 = (Q\sqrt{\Lambda}Q^T)(Q\sqrt{\Lambda}Q^T) = Q\sqrt{\Lambda}\sqrt{\Lambda}Q^T = Q\Lambda Q^T = A
\]

### (b) Are matrix square roots unique?

**Solution:** No, matrix square roots are not unique. For example, both $Q\sqrt{\Lambda}Q^T$ and $-Q\sqrt{\Lambda}Q^T$ square to A, though we typically take the positive definite square root.

### (c) Express eᴬ in terms of eigenvectors and eigenvalues

**Solution:**
\[
e^A = Qe^\Lambda Q^T
\]
where 
\[
e^\Lambda = \text{diag}(e^{\lambda_1}, \ldots, e^{\lambda_n})
\]

### (d) If AB = BA, show eᴬ⁺ᴮ = eᴬeᴮ

**Solution:**
When AB = BA, the matrices commute and we can use the binomial theorem:
\[
e^{A+B} = \sum_{k=0}^\infty \frac{(A+B)^k}{k!} = \sum_{k=0}^\infty \frac{1}{k!} \sum_{i=0}^k \binom{k}{i} A^i B^{k-i}
\]
\[
= \left( \sum_{i=0}^\infty \frac{A^i}{i!} \right) \left( \sum_{j=0}^\infty \frac{B^j}{j!} \right) = e^A e^B
\]

### (e) Solve y'(t) = -Ay with y(0) = y₀ and analyze as t → ∞

**Solution:**
The solution is 
\[
y(t) = e^{-At} y_0
\]
As t → ∞, since A is positive definite, all eigenvalues are positive, so $e^{-At} \to 0$ and thus $y(t) \to 0$.

---

## Exercise 7.3: SVD and Condition Numbers

**Problem:** Provide the SVD and condition number for:

### (a) Matrix:
\[
A = \begin{bmatrix}
0 & 0 & 1 \\
0 & \sqrt{2} & 0 \\
\sqrt{3} & 0 & 0
\end{bmatrix}
\]

**Solution:**
Compute $A^TA$:
\[
A^TA = \begin{bmatrix}
3 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

Eigenvalues: $\lambda_1 = 3$, $\lambda_2 = 2$, $\lambda_3 = 1$  
Singular values: $\sigma_1 = \sqrt{3}$, $\sigma_2 = \sqrt{2}$, $\sigma_3 = 1$

**SVD decomposition:**

**U matrix:**
\[
U = \begin{bmatrix}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{bmatrix}
\]

**Σ matrix:**
\[
\Sigma = \begin{bmatrix}
\sqrt{3} & 0 & 0 \\
0 & \sqrt{2} & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

**V matrix:**
\[
V = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\]

Condition number: $\text{cond}(A) = \frac{\sigma_{\text{max}}}{\sigma_{\text{min}}} = \frac{\sqrt{3}}{1} = \sqrt{3}$

### (b) Matrix:
\[
A = \begin{bmatrix}
-5 \\
3
\end{bmatrix}
\]

**Solution:**
This is a column vector.

\[
\|A\|_2 = \sqrt{(-5)^2 + 3^2} = \sqrt{25 + 9} = \sqrt{34}
\]

**U matrix:**
\[
U = \begin{bmatrix}
-\frac{5}{\sqrt{34}} \\
\frac{3}{\sqrt{34}}
\end{bmatrix}
\]

**Σ matrix:**
\[
\Sigma = \begin{bmatrix}
\sqrt{34} \\
0
\end{bmatrix}
\]

**V matrix:**
\[
V = \begin{bmatrix}
1
\end{bmatrix}
\]

Condition number is undefined for non-square matrices, but the ratio of singular values is ∞ since $\sigma_2 = 0$.

---

## Exercise 7.10: Latent Semantic Analysis

**Problem:** Given word-document occurrence matrix X ∈ ℝᵐˣⁿ:

### (a) Interpret XXᵀ and XᵀX

**Solution:**
- **XXᵀ**: Word co-occurrence matrix, where (i,j) entry represents how often words i and j appear together in documents
- **XᵀX**: Document similarity matrix, where (i,j) entry represents how similar documents i and j are based on shared words

### (b) Find best k-dimensional approximation

**Solution:**
By the Eckart-Young theorem, the best rank-k approximation in Frobenius norm is given by the truncated SVD:
\[
X_k = U_k \Sigma_k V_k^T
\]

The columns of $U_k$ provide the best k-dimensional basis for representing the documents.

### (c) Cross-language analysis using SVD

**Solution:**
For two languages with occurrence matrices $X_1$ and $X_2$ for the same documents, we want to find vectors $\vec{v}_1$, $\vec{v}_2$ maximizing:
\[
\frac{(X_1^T \vec{v}_1) \cdot (X_2^T \vec{v}_2)}{\|\vec{v}_1\|_2 \|\vec{v}_2\|_2}
\]

This is equivalent to finding the first singular vectors of $X_1 X_2^T$. Compute SVD: $X_1 X_2^T = U\Sigma V^T$  
Then take $\vec{v}_1$ = first column of U, $\vec{v}_2$ = first column of V.

---

## Newton's Method Implementation

**Problem:** Write Newton's method code to solve $\ln(x-1) + \cos(x-1) = 0$ accurate to within $10^{-5}$

### Python Implementation:

```python
import math

def newton_method(f, df, x0, tol=1e-5, max_iter=100):
    """
    Newton's method for solving f(x) = 0
    
    Parameters:
    f: function
    df: derivative of function  
    x0: initial guess
    tol: tolerance
    max_iter: maximum iterations
    
    Returns:
    root: solution
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            print(f"Converged after {i} iterations")
            return x
        
        dfx = df(x)
        if abs(dfx) < 1e-12:
            print("Derivative too small")
            return x
            
        x_new = x - fx/dfx
        
        # Ensure we stay in domain (x > 1)
        if x_new <= 1:
            x_new = 1.1
            
        print(f"Iteration {i}: x = {x:.6f}, f(x) = {fx:.6f}")
        x = x_new
    
    print("Maximum iterations reached")
    return x

# Define the function and its derivative
def f(x):
    return math.log(x-1) + math.cos(x-1)

def df(x):
    return 1/(x-1) - math.sin(x-1)

# Solve
print("Solving ln(x-1) + cos(x-1) = 0 using Newton's method")
solution = newton_method(f, df, x0=1.5)
print(f"Solution: x = {solution:.6f}")
print(f"Verification: f({solution:.6f}) = {f(solution):.6f}")
