import numpy as np
A = np.arange(-10, 13, 2).reshape(4, -1)
B = np.eye(3, 4) - 2
C = A @ B
print(C)
#C行列の2行2列までを取得する
D = C[:2, :2]
print(D)
#D行列を転置する
print(D.T)
#転置したD行列に逆行列が存在するか行列式の値を確認する
print(np.linalg.det(D.T)) #行列式の値が0でなければ逆行列が存在する
#転置したD行列の逆行列を求める
print(np.linalg.inv(D.T))