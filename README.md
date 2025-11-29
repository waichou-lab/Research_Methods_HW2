# 數值方法作業 2 解答 #  
___________________________________  
## 問題 5.1：Householder QR 分解與 Gram-Schmidt 比較  
![image](image/fg1.jpg)  
## Gram-Schmidt 方法結果  
從教科書示例 5.2 可得： 
![image](image/fg2.jpg)  
## Householder 方法推導  
第一步：處理第一列  
第一列向量：
$\vec{a}_1 = (1, 0, 0)^T$  
範數：
$|\vec{a}_1| = 1$  
選擇
$\sigma = -1$（為數值穩定性)  
反射向量：
$\vec{v} = \vec{a}_1 - \sigma \vec{e}_1 = (2, 0, 0)^T$  
Householder 矩陣：  
![image](image/fg3.jpg)  
應用變換：  
![image](image/fg4.jpg)  
第二步：處理第二列  
考慮子矩陣（第二行和第二列以下）：
$\vec{a}_2 = (1, 1)^T$
範數：
$|\vec{a}_2| = \sqrt{2}$  
選擇
$\sigma = -\sqrt{2}$  
反射向量：
$\vec{v} = \vec{a}_2 - \sigma \vec{e}_1 = (1+\sqrt{2}, 1)^T$  
2×2 反射矩陣：  
![image](image/fg5.jpg)  
擴展為 3×3 矩陣：  
