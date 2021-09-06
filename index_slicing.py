import numpy as np
#"arangeメソッド"の第一引数で開始の数値(start<=n)、第二で最後の数値(n<end)、第三で間隔
a = np.arange(1, 13, 2)
print("aベクトル")
print(a)
B = np.array([[2, 4, 6], [-1, 5, -3], [0, -2, 3]])
print("B行列")
print(B)

print("aベクトルについて")
c = a[2:-1] #"2"でインデックス番号2を指定、"−1"でインデックス番号の最後から1つ前の番号を指定
print(c)
d = a[::-1] #"::"で逆順での取得になる
print(d)

print("B行列について")
e = B[0] #"0"を指定することで1行目を取得することができる
print(e)
f = B[2, 0] #3行1列目の値を取得
print(f)
g = B[1:, 1:] #","の左側で行の指定、右側で列の指定
print(g)