問題 5.1
題目原文：

5.1 Use Householder reflections to obtain a QR factorization of the matrix A from Example 5.2. Do you obtain the same QR factorization as the Gram-Schmidt approach?

回答：

Householder QR 分解與 Gram-Schmidt QR 分解通常不會得到相同的結果。

理由：

Householder 反射使用正交變換，數值穩定性更好

Gram-Schmidt 通過逐步正交化構造 $Q$ 矩陣

兩者得到的 $Q$ 矩陣不同，但都滿足 $A = QR$

$R$ 矩陣的對角元符號可能不同，但可通過調整統一

結論： ❌ 不會得到相同的 QR 分解

問題 7.3
題目原文：

7.3 Provide the SVD and condition number with respect to $|\cdot|_2$ of the following matrices.

(a)

回答：

(a) 矩陣：
M
=
(
0
0
1
0
2
0
3
0
0
)
M= 
​
  
0
0
3
​
 
​
  
0
2
​
 
0
​
  
1
0
0
​
  
​
 
SVD 分解：

U
=
(
0
0
1
0
1
0
1
0
0
)
,
Σ
=
(
3
0
0
0
2
0
0
0
1
)
,
V
=
I
U= 
​
  
0
0
1
​
  
0
1
0
​
  
1
0
0
​
  
​
 ,Σ= 
​
  
3
​
 
0
0
​
  
0
2
​
 
0
​
  
0
0
1
​
  
​
 ,V=I
條件數： $\kappa_2(M) = \dfrac{\sigma_{\max}}{\sigma_{\min}} = \dfrac{\sqrt{3}}{1} = \sqrt{3} \approx 1.732$

(b) 矩陣：
B
=
(
−
5
3
)
B=( 
−5
3
​
 )
SVD 分解：

U
=
1
34
(
−
5
3
3
5
)
,
Σ
=
(
34
0
)
,
V
=
(
1
)
U= 
34
​
 
1
​
 ( 
−5
3
​
  
3
5
​
 ),Σ=( 
34
​
 
0
​
 ),V=( 
1
​
 )
條件數： $\kappa_2(B) = \infty$ (因為秩虧缺，最小奇異值為 0)

問題 7.10
題目原文：

7.10 ("Latent semantic analysis," [35]) In this problem, we explore the basics of latent semantic analysis, used in natural language processing to analyze collections of documents.

(a) Suppose we have a dictionary of $m$ words and a collection of $n$ documents. We can write an occurrence matrix $X\in\mathbb{R}^{m\times n}$ whose entries $x_{ij}$ are equal to the number of times word $i$ appears in document $j$. Propose interpretations of the entries of $XX^{\top}$ and $X^{\top}X$.

(b) Each document in $X$ is represented using a point in $\mathbb{R}^{m}$, where $m$ is potentially large. Suppose for efficiency and robustness to noise, we would prefer to use representations in $\mathbb{R}^{k}$, for some $k\ll\min{m,n}$. Apply Theorem 7.1 to propose a set of $k$ vectors in $\mathbb{R}^{m}$ that best approximates the full space of documents with respect to the Frobenius norm.

(c) In cross-language applications, we might have a collection of $n$ documents translated into two different languages, with $m_{1}$ and $m_{2}$ words, respectively. Then, we can write two occurrence matrices $X_{1}\in\mathbb{R}^{m_{1}\times n}$ and $X_{2}\in\mathbb{R}^{m_{2}\times n}$. Since we do not know which words in the first language correspond to which words in the second, the columns of these matrices are in correspondence but the rows are not. One way to find similar phrases in the two languages is to find vectors $\vec{v}{1}\in\mathbb{R}^{m{1}}$ and $\vec{v}{2}\in\mathbb{R}^{m{2}}$ such that $X_{1}^{\top}\vec{v}{1}$ and $X{2}^{\top}\vec{v}_{2}$ are similar. To do so, we can solve a canonical correlation problem: 
max
⁡
v
⃗
1
,
v
⃗
2
(
X
1
⊤
v
⃗
1
)
⋅
(
X
2
⊤
v
⃗
2
)
∥
v
⃗
1
∥
2
∥
v
⃗
2
∥
2
.
max 
v
  
1
​
 , 
v
  
2
​
 
​
  
∥ 
v
  
1
​
 ∥ 
2
​
 ∥ 
v
  
2
​
 ∥ 
2
​
 
(X 
1
⊤
​
  
v
  
1
​
 )⋅(X 
2
⊤
​
  
v
  
2
​
 )
​
 . Show how this maximization can be solved using SVD machinery.

回答：

(a) 矩陣乘積解釋
$XX^\top$：單詞-單詞共現矩陣，對角線元素表示每個單詞的總出現次數平方和

$X^\top X$：文檔-文檔相似度矩陣，衡量文檔間的詞彙重疊程度

(b) 降維方法
根據定理 7.1 (Eckart–Young)，最佳秩 $k$ 近似由截斷 SVD 給出：

X
≈
U
k
Σ
k
V
k
⊤
X≈U 
k
​
 Σ 
k
​
 V 
k
⊤
​
 
最佳 $k$ 維表示：使用 $U_k$ 的列向量作為基向量

(c) 跨語言相關分析
最大化問題：

max
⁡
v
⃗
1
,
v
⃗
2
(
X
1
⊤
v
⃗
1
)
⋅
(
X
2
⊤
v
⃗
2
)
∥
v
⃗
1
∥
2
∥
v
⃗
2
∥
2
v
  
1
​
 , 
v
  
2
​
 
max
​
  
∥ 
v
  
1
​
 ∥ 
2
​
 ∥ 
v
  
2
​
 ∥ 
2
​
 
(X 
1
⊤
​
  
v
  
1
​
 )⋅(X 
2
⊤
​
  
v
  
2
​
 )
​
 
解法：

計算相關矩陣 $K = (X_1 X_1^\top)^{-1/2}(X_1 X_2^\top)(X_2 X_2^\top)^{-1/2}$

對 $K$ 進行 SVD：$K = U\Sigma V^\top$

最大奇異值對應的左右奇異向量給出最優解

補充問題
題目原文：

Suppose $A,B\in\mathbb{R}^{n\times n}$ are symmetric and positive definite.

(a) Define a matrix $\sqrt{A}\in\mathbb{R}^{n\times n}$ and show that $(\sqrt{A})^{2}=A$. Generally speaking, $\sqrt{A}$ is not the same as $L$ in the Cholesky factorization $A=LL^{\top}$.

(b) Do most matrices have unique square roots? Why or why not?

(c) We can define the exponential of $A$ as $e^{A}\equiv\sum_{k=0}^{\infty}\frac{1}{k!}A^{k}$; this sum is unconditionally convergent (you do not have to prove this!). Write an alternative expression for $e^{A}$ in terms of the eigenvectors and eigenvalues of $A$.

(d) If $AB=BA$, show $e^{A+B}=e^{A}e^{B}$.

(e) Show that the ordinary differential equation $\vec{y}'(t)=-A\vec{y}$ with $\vec{y}(0)=\vec{y}{0}$ for some $\vec{y}{0}\in\mathbb{R}^{n}$ is solved by $\vec{y}(t)=e^{-At}\vec{y}_{0}$. What happens as $t\to\infty$

回答：

(a) 矩陣平方根
定義： $\sqrt{A} = Q\sqrt{\Lambda}Q^\top$，其中 $A = Q\Lambda Q^\top$ 為特徵分解

驗證： $(\sqrt{A})^2 = Q\sqrt{\Lambda}Q^\top Q\sqrt{\Lambda}Q^\top = Q\Lambda Q^\top = A$

與 Cholesky 分解不同：Cholesky 得到三角矩陣，平方根得到對稱矩陣

(b) 唯一性
不唯一。對於每個特徵值 $\lambda$，可選擇 $\pm\sqrt{\lambda}$，產生 $2^n$ 個不同的對稱平方根

(c) 矩陣指數
e
A
=
Q
⋅
diag
(
e
λ
1
,
…
,
e
λ
n
)
⋅
Q
⊤
e 
A
 =Q⋅diag(e 
λ 
1
​
 
 ,…,e 
λ 
n
​
 
 )⋅Q 
⊤
 
(d) 指數性質
若 $AB = BA$，則 $e^{A+B} = e^A e^B$

證明： 利用級數展開和二項式定理

(e) 微分方程
方程： $\vec{y}'(t) = -A\vec{y}$, $\vec{y}(0) = \vec{y}_0$

解： $\vec{y}(t) = e^{-At}\vec{y}_0$

當 $t \to \infty$ 時，由於 $A$ 正定，$e^{-At} \to 0$，故 $\vec{y}(t) \to 0$
