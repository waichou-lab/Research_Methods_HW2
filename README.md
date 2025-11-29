問題 5.1  
題目原文：  
5.1 Use Householder reflections to obtain a QR factorization of the matrix A from Example 5.2. Do you obtain the same QR factorization as the Gram-Schmidt approach?  

回答：  

Householder QR 分解與 Gram-Schmidt QR 分解通常不會得到相同的結果。  

理由：  

Householder 反射使用正交變換，數值穩定性更好  

Gram-Schmidt 通過逐步正交化構造 Q 矩陣  

兩者得到的 Q 矩陣不同，但都滿足 A = QR  

R 矩陣的對角元符號可能不同，但可通過調整統一  

結論： 不會得到相同的 QR 分解  

問題 7.3
題目原文：
7.3 Provide the SVD and condition number with respect to ||·||₂ of the following matrices.

(a)
[[0, 0, 1],
[0, √2, 0],
[√3, 0, 0]]

(b)
[[-5],
[3]]

回答：

(a) 矩陣：
M = [[0, 0, 1],
[0, √2, 0],
[√3, 0, 0]]

SVD 分解：
U = [[0, 0, 1],
[0, 1, 0],
[1, 0, 0]]

Σ = [[√3, 0, 0],
[0, √2, 0],
[0, 0, 1]]

V = I

條件數： κ₂(M) = σ_max/σ_min = √3/1 = √3 ≈ 1.732

(b) 矩陣：
B = [[-5],
[3]]

SVD 分解：
U = (1/√34) × [[-5, 3],
[3, 5]]

Σ = [[√34],
[0]]

V = [[1]]

條件數： κ₂(B) = ∞ (因為秩虧缺，最小奇異值為 0)
