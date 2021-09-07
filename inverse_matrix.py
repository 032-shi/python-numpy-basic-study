import numpy as np
A = np.array([[4, -2], [1, 0]])
print("A行列の表示")
print(A)
print("A行列の行列式の計算")
print(np.linalg.det(A))
print("A行列の行列式の値が0か判定")
print(np.linalg.det(A) == 0.0)
print("A行列の逆行列の表示")
print(np.linalg.inv(A))
print("A行列とA行列の逆行列の行列積の表示")
print(A @ np.linalg.inv(A)) #元の行列と逆行列の行列積は単位行列となる