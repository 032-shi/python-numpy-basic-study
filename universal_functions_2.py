import numpy as np
A = np.array([0, np.pi, np.pi/2, -np.pi/4]).reshape(2, -1)
print(A)
print("行列の各値の三角関数のsinの値を取得")
print(np.sin(A)) #sin(0)が0、sin(pi/2)が1であることを確認する。
print("行列の各値の三角関数のcosの値を取得")
print(np.cos(A)) #cos(0)が1、cos(pi/2)が0であることを確認する。