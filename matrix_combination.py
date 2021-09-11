import numpy as np
A = np.array([0, 1, -1, 2, 4, -3, 5, -2, 7]).reshape(3, -1)
B = np.array([-2, 0, 1, 5, -1, 2, -6, 3, 4]).reshape(3, -1)
print(A)
print(B)
print("垂直方向に結合")
print(np.vstack((A, B)))
print("水平方向に結合")
print(np.hstack((A, B)))
