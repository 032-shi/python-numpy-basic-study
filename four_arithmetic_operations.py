import numpy as np
a = np.array([[1, 3], [-2, 4]])
b = np.array([[2, -1], [3, 0]])
c = np.array([[-2, -5], [1, 3]])
d = np.array([[3, 0], [6, 2]])
e = np.array([[3, 5], [4, -1]])
f = np.array([[-2, 1], [0, -3]])

print("足し算")
print(a + b)
print("引き算")
print(a - b)
print("行列積")
print(c @ d) #13行と同じ計算
print(c.dot(d)) #12行と同じ計算
print("アダマール積") #要素同志(同じ場所の値)の掛け算
print(e * f)

