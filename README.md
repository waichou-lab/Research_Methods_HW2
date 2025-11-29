問題 5.1
題目原文：

text
5.1 Use Householder reflections to obtain a QR factorization of the matrix A from Example 5.2. Do you obtain the same QR factorization as the Gram-Schmidt approach?
回答：

Householder QR 分解與 Gram-Schmidt QR 分解通常不會得到相同的結果。

理由：

Householder 反射使用正交變換，數值穩定性更好

Gram-Schmidt 通過逐步正交化構造 $Q$ 矩陣

兩者得到的 $Q$ 矩陣不同，但都滿足 $A = QR$

$R$ 矩陣的對角元符號可能不同，但可通過調整統一

結論： ❌ 不會得到相同的 QR 分解

