# 理論問題解答

## 問題 1 (來自圖2)

**題目原文：**
**Example 5.2** (QR factorization).: Suppose we construct a matrix whose columns are $\vec{v}\_{1}$, $\vec{v}\_{2}$, and $\vec{v}\_{3}$ from Example 5.1:

$$
A\equiv\left(\begin{array}{ccc}1&1&1\\\\ 0&1&1\\\\ 0&1&0\end{array}\right)
$$

The output of Gram-Schmidt orthogonalization can be encoded in the matrix

$$
Q\equiv\left(\begin{array}{ccc}1&0&0\\\\ 0&1/\sqrt{2}&1/\sqrt{2}\\\\ 0&1/\sqrt{2}&-1/\sqrt{2}\end{array}\right)
$$

We can obtain the upper-triangular matrix $R$ in the QR factorization two different ways. First, we can compute $R$ after the fact using a product:

$$
R=Q^{\top}A=\left(\begin{array}{ccc}1&0&0\\\\ 0&1/\sqrt{2}&1/\sqrt{2}\\\\ 0&1/\sqrt{2}&-1/\sqrt{2}\end{array}\right)^{\top}\left(\begin{array}{ccc}1&1&1\\\\ 0&1&1\\\\ 0&1&0\end{array}\right)=\left(\begin{array}{ccc}1&1&1\\\\ 0&\sqrt{2}&1/\sqrt{2}\\\\ 0&0&1/\sqrt{2}\end{array}\right)
$$

As expected, $R$ is upper triangular.

**中文解答：**
這是一個QR分解的示例，展示了如何通過Gram-Schmidt正交化過程將矩陣A分解為正交矩陣Q和上三角矩陣R的乘積。驗證了R確實是上三角矩陣，這是QR分解的基本性質。

---

## 問題 2 (來自圖3)

**題目原文：**
Suppose $A,B\in\mathbb{R}^{n\times n}$ are symmetric and positive definite.

1. (a)Define a matrix $\sqrt{A}\in\mathbb{R}^{n\times n}$ and show that $(\sqrt{A})^{2}=A$. Generally speaking, $\sqrt{A}$ is not the same as $L$ in the Cholesky factorization $A=LL^{\top}$.

2. (b)Do most matrices have unique square roots? Why or why not?

3. (c)We can define the *exponential* of $A$ as $e^{A}\equiv\sum_{k=0}^{\infty}\frac{1}{k!}A^{k}$; this sum is unconditionally convergent (you do not have to prove this!). Write an alternative expression for $e^{A}$ in terms of the eigenvectors and eigenvalues of $A$.

4. (d)If $AB=BA$, show $e^{A+B}=e^{A}e^{B}$.

5. (e)Show that the ordinary differential equation $\vec{y}\,^{\prime}(t)=-A\vec{y}$ with $\vec{y}(0)=\vec{y}\_{0}$ for some $\vec{y}\_{0}\in\mathbb{R}^{n}$ is solved by $\vec{y}(t)=e^{-At}\vec{y}\_{0}$. What happens as $t\to\infty$

**中文解答：**

(a) 對於對稱正定矩陣A，我們可以通過特徵值分解來定義平方根矩陣：如果$A = PDP^{-1}$，其中D是對角矩陣，則$\sqrt{A} = P\sqrt{D}P^{-1}$，其中$\sqrt{D}$是對D的每個對角元素取平方根。這樣定義的$\sqrt{A}$滿足$(\sqrt{A})^2 = A$。這與Cholesky分解$A=LL^{\top}$不同，因為Cholesky分解要求L是下三角矩陣，而$\sqrt{A}$一般是對稱矩陣。

(b) 大多數矩陣沒有唯一的平方根。對於對稱正定矩陣，雖然主平方根（所有特徵值取非負平方根）是唯一的，但存在其他可能的平方根（通過對某些特徵值取負平方根得到）。對於非對稱或非正定矩陣，情況更加複雜。

(c) 如果A有特徵值分解$A = PDP^{-1}$，其中D是對角矩陣，對角元素是A的特徵值$\lambda_1, \ldots, \lambda_n$，則$e^A = Pe^D P^{-1}$，其中$e^D$是對角矩陣，對角元素為$e^{\lambda_1}, \ldots, e^{\lambda_n}$。

(d) 當$AB = BA$時，矩陣A和B可交換，此時矩陣指數滿足$e^{A+B} = e^A e^B$。這可以通過將指數展開為冪級數並利用二項式定理來證明。

(e) 將$\vec{y}(t) = e^{-At}\vec{y}_0$代入ODE：$\vec{y}\,^{\prime}(t) = \frac{d}{dt}e^{-At}\vec{y}_0 = -Ae^{-At}\vec{y}_0 = -A\vec{y}(t)$，滿足方程。當$t \to \infty$時，由於A是正定矩陣，所有特徵值為正，$e^{-At}$趨近於零矩陣，因此$\vec{y}(t) \to \vec{0}$。

---

## 問題 3 (來自圖4)

**題目原文：**
5.1 Use Householder reflections to obtain a QR factorization of the matrix A from Example 5.2. Do you obtain the same QR factorization as the Gram-Schmidt approach?

**中文解答：**
使用Householder反射進行QR分解與Gram-Schmidt方法通常不會得到完全相同的Q和R矩陣，因為：

1. **正交矩陣Q的不同**：Householder方法產生的Q矩陣是通過一系列反射構造的，而Gram-Schmidt是通過正交化過程構造的。它們都是正交基，但可能方向不同。

2. **上三角矩陣R的符號差異**：R矩陣的對角線元素可能符號不同，但絕對值相同。

3. **數值穩定性**：Householder方法通常比經典Gram-Schmidt更數值穩定，但修改後的Gram-Schmidt可以改善穩定性。

兩種方法在數學上等價，都能得到有效的QR分解，但具體的矩陣元素可能不同。

---

## 問題 4 (來自圖5)

**題目原文：**
7.10 ("Latent semantic analysis," [35]) In this problem, we explore the basics of *latent semantic analysis*, used in natural language processing to analyze collections of documents.

* (a)Suppose we have a dictionary of $m$ words and a collection of $n$ documents. We can write an *occurrence matrix* $X\in\mathbb{R}^{m\times n}$ whose entries $x_{ij}$ are equal to the number of times word $i$ appears in document $j$. Propose interpretations of the entries of $XX^{\top}$ and $X^{\top}X$.

* (b)Each document in $X$ is represented using a point in $\mathbb{R}^{m}$, where $m$ is potentially large. Suppose for efficiency and robustness to noise, we would prefer to use representations in $\mathbb{R}^{k}$, for some $k\ll\min\\{m,n\\}$. Apply Theorem 7.1 to propose a set of $k$ vectors in $\mathbb{R}^{m}$ that best approximates the full space of documents with respect to the Frobenius norm.

* (c)In *cross-language* applications, we might have a collection of $n$ documents translated into two different languages, with $m_{1}$ and $m_{2}$ words, respectively. Then, we can write two occurrence matrices $X_{1}\in\mathbb{R}^{m_{1}\times n}$ and $X_{2}\in\mathbb{R}^{m_{2}\times n}$. Since we do not know which words in the first language correspond to which words in the second, the columns of these matrices are in correspondence but the rows are not. One way to find similar phrases in the two languages is to find vectors $\vec{v}\_{1}\in\mathbb{R}^{m_{1}}$ and $\vec{v}\_{2}\in\mathbb{R}^{m_{2}}$ such that $X_{1}^{\top}\vec{v}\_{1}$ and $X_{2}^{\top}\vec{v}\_{2}$ are similar. To do so, we can solve a *canonical correlation* problem: 
$$
\max_{\vec{v}\_{1},\vec{v}\_{2}}\frac{(X_{1}^{\top}\vec{v}\_{1})\cdot(X_{2}^{\top}\vec{v}\_{2})}{\|\vec{v}\_{1}\|\_{2}\|\vec{v}\_{2}\|\_{2}}
$$
Show how this maximization can be solved using SVD machinery.

**中文解答：**

(a) 
- $XX^{\top}$：這個矩陣的$(i,j)$元素表示單詞$i$和單詞$j$在所有文檔中共同出現的頻率，可以解釋為單詞之間的共現矩陣，反映了單詞間的語義關係。
- $X^{\top}X$：這個矩陣的$(i,j)$元素表示文檔$i$和文檔$j$的單詞頻率向量的內積，反映了文檔之間的相似度。

(b) 根據定理7.1（可能是關於SVD的最佳低秩逼近），我們可以對矩陣X進行奇異值分解(SVD)：$X = U\Sigma V^{\top}$。然後取前k個奇異值對應的左奇異向量（即U的前k列），這些向量張成的子空間在Frobenius範數意義下對原始文檔空間的最佳k維逼近。

(c) 這個典型相關分析問題可以通過SVD求解。首先計算矩陣$X_1 X_2^{\top}$的SVD分解：$X_1 X_2^{\top} = U\Sigma V^{\top}$。那麼最大化問題的解是：
- $\vec{v}_1$是U的第一列（對應最大奇異值的左奇異向量）
- $\vec{v}_2$是V的第一列（對應最大奇異值的右奇異向量）

這些向量使得$X_1^{\top}\vec{v}_1$和$X_2^{\top}\vec{v}_2$之間的相關性最大。

---

## 問題 5 (來自圖6)

**題目原文：**
