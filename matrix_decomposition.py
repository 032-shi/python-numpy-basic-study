import numpy as np
A = np.array([0, 1, -1, 2, 4, -3, 5, -2, 7]).reshape(3, -1)
B = np.array([-2, 0, 1, 5, -1, 2, -6, 3, 4]).reshape(3, -1)
print(A)
print(B)
print("垂直方向に結合")
C = np.vstack((A, B))
print(C)
print("水平方向に結合")
D = np.hstack((A, B))
print(D)
print("垂直方向に分解")
print(np.vsplit(C, 3)) #"C行列"を垂直方向に"3分割"する
print(np.vsplit(C, 3)[0]) #"[0]"を指定することで1つ目の分割した行列を取得する
print("水平方向に分解")
print(np.hsplit(D, 3)) #"D行列"を水平方向に"3分割"する