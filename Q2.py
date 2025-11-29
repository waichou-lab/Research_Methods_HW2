import math

def f(x):
    """定義函數 f(x) = ln(x-1) + cos(x-1)"""
    return math.log(x-1) + math.cos(x-1)

def df(x):
    """定義導數 f'(x) = 1/(x-1) - sin(x-1)"""
    return 1/(x-1) - math.sin(x-1)

def newton_method(initial_guess, tolerance=1e-5, max_iterations=100):
    """
    牛頓法求解方程
    
    參數:
        initial_guess: 初始猜測值
        tolerance: 容許誤差
        max_iterations: 最大迭代次數
    
    返回:
        方程的近似解
    """
    x = initial_guess
    for i in range(max_iterations):
        fx = f(x)
        dfx = df(x)
        
        # 檢查導數是否接近零
        if abs(dfx) < 1e-10:
            print("導數接近零，迭代終止")
            break
            
        # 牛頓法迭代公式
        x_new = x - fx / dfx
        
        # 檢查收斂
        if abs(x_new - x) < tolerance:
            return x_new
            
        x = x_new
        
    return x

# 初始猜測 x0 = 1.4，因為 f(1.4) ≈ 0.005
root = newton_method(1.4)
print(f"根為: {root:.6f}")
print(f"f(root) = {f(root):.10f}")
