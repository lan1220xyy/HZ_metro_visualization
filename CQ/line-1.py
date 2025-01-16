import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

def getdata(file,x,node_index,week_index=0):
    y = np.zeros((len(node_index), len(x)))  # y 轴数据
    datafrom = pd.read_csv(f'../data/PEMSD7/data{file+1}.csv').drop(columns="time").to_numpy()
    for i, index in enumerate(x):
        for j, value in enumerate(node_index):
            y[j, i] = datafrom[index * 12 + week_index * 12 * 24, value]
    return y

def drawLine(x,node_index,sub=5):
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    fig, axs = plt.subplots(1, 5, figsize=(15, 5))
    for i in range(sub):
        y = getdata(i,x,node_index)
        print(y)
        for j in range(y.shape[0]):
            axs[i].plot(x, y[j, :], color=colors[j], label=f'line{j + 1}', linestyle='--')
            axs[i].set_ylim(0,80)
    # 调整子图之间的间距
    plt.tight_layout()

    # 显示所有子图
    plt.show()


# 示例数据
num_node = 6
x = [14, 15, 16, 17, 18]         # x 轴数据
node_index = [random.randint(0,227) for _ in range(num_node)]
print(node_index)

drawLine(x,node_index)