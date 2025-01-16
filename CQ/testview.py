import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
os.environ['KMP_DUPLICATE_LIB_OK']='True'

##测试一下sns的接口

matrix = np.random.random(size=(6,6))
print(matrix)

fig = plt.figure(figsize=(10,5))
title = 'Wensday'

sns.heatmap(matrix,cmap='coolwarm',)
plt.title(title)
plt.show()
