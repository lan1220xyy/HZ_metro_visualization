import os
import matplotlib.pyplot as plt
import load
from matplotlib.gridspec import GridSpec
import numpy as np
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#preparation
num = 10

rows = [7,8,11,12,15,16]  # 自定义 x 轴刻度位置
cols = rows  # 自定义 y 轴刻度位置
matrix_list = load.matrix_list(num)

# 创建图形和网格布局
fig = plt.figure(figsize=(15, 5))
gs = GridSpec(1, 6, width_ratios=[1, 1, 1, 1, 1, 0.05])  # 额外的列用于颜色条
title = ['Monday','Tuesday','Wendsday','Thirsday','Friday']
# 创建热力图
for i, matrix in enumerate(matrix_list):

    ax = fig.add_subplot(gs[0, i])
    cax = ax.imshow(matrix[np.ix_(rows,cols)], aspect='equal', cmap='coolwarm')
    ax.set_title(f'{title[i]}')
    # 设置自定义的刻度
    x_ticks = np.arange(len(rows))  # x轴刻度位置
    plt.xticks(x_ticks, rows)  # 应用自定义刻度

    y_ticks = np.arange(len(cols))  # y轴刻度位置
    plt.yticks(y_ticks,cols)  # 应用自定义刻度

# 获取最后一个热力图的位置，以对齐颜色条
pos = ax.get_position()
cbar_ax = fig.add_axes([pos.x1 + 0.01, pos.y0, 0.01, pos.height])  # 手动设置颜色条位置

# 添加颜色条并设置标签
cbar = fig.colorbar(cax, cax=cbar_ax)
# 显示图形
plt.show()
plt.savefig("../../fig/week/",dpi=300)

#eps格式

#todo: 1.切分数据 2.写脚本 3.做图 4.插入overleaf