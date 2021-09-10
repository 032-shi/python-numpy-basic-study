import numpy as np
A = np.array([0, 1, 2, 4]).reshape(2, -1) #reshapeの引数に−1を指定することで他の次元値から推測された値が自動的に決定される。
print(A)
print("行列内の要素の平方根を取得")
print(np.sqrt(A))
print("行列内の指数関数を取得")
print(np.exp(A))