import numpy as np
a = np.array([2, 3, 4])
print(a)
B = np.array([[1.2, 3.5, 5.1], [-0.3, 1.1, -4.5]])
print(B)
print("\n[2, 3, 4]の情報")
c = a.shape #形状の取得
print(c)
d = a.ndim #次元の取得
print(d)
e = a.dtype #データ型の取得
print(e)
f = a.size #要素数の取得
print(f)
print("\n[[1.2, 3.5, 5.1], [-0.3, 1.1, -4.5]]の情報")
g = B.shape #形状の取得
print(g)
h = B.ndim #次元の取得
print(h)
i = B.dtype #データ型の取得
print(i)
j = B.size #要素数の取得
print(j)