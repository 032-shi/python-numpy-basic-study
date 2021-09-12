import numpy as np
#以下、AとB行列の行列積を計算する
A = np.arange(-10, 13, 2).reshape(4, -1) #-10から13未満の2間隔の等差数列
B = np.eye(3, 4) - 2 #3行4列の単位行列の各要素から−2した行列
#まず、A及びBの行列の形状を確認する
print(A.shape, B.shape) #行列積が成り立つには、第一の行列の列と第二の行列の行が一致しなければならない
print(A @ B)