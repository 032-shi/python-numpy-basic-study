import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 500) #第一引数：0からスタート、第二：2piまで、第三：500個の要素
plt.plot(x, np.sin(x)) #第一引数：x軸、第二：y軸を指定
plt.plot(x, np.cos(x))
plt.show() #グラフを表示

#以下のヒストグラムは、Googlecolab上で確認する
data = np.random.randint(0, 30, 100) #0から30までの整数を100個作成
plt.hist(data, bins = 50) #第二引数でグラフの太さを指定する