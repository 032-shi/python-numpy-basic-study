import numpy as np
import matplotlib.pyplot as plt
data1 = np.random.randint(-100, 100, 300)
data2 = np.random.randint(-100, 100, 300)
#以下、散布図はGooglecolab上で確認
plt.scatter(data1, data2) #散布図を表示