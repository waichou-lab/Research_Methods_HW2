# 數值方法作業 2 解答 #  
___________________________________  
## 問題 5.1：Householder QR 分解與 Gram-Schmidt 比較  
![image](image/fg1.png)  
## Gram-Schmidt 方法結果  
從教科書示例 5.2 可得： 
![image](image/fg2.png)  
## Householder 方法推導  
第一步：處理第一列  
第一列向量：$\vec{a}_1 = (1, 0, 0)^T$  

範數：$|\vec{a}_1| = 1$  

選擇 $\sigma = -1$（為數值穩定性）

反射向量：$\vec{v} = \vec{a}_1 - \sigma \vec{e}_1 = (2, 0, 0)^T$  

Householder 矩陣：  
