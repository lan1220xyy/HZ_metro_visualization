import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D


def getdata(file,x,node_index,week_index=2):
    y = np.zeros((len(node_index), len(x)))  # y 轴数据
    datafrom = pd.read_csv(f'../../data/HZ_metro/data{file}.csv',header=None).to_numpy()
    # datafrom = pd.read_csv(f'../../data/PEMSD7/data{file+1}.csv').drop(columns="time").to_numpy()
    for i, index in enumerate(x):
        for j, value in enumerate(node_index):
            y[j, i] = datafrom[(index-6) * 4 + 2 + week_index * 73, value]
    return y

# def drawLine(x,node_index,day=7):
#     colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
#     weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
#     fig, axs = plt.subplots(1, day, figsize=(15, 5))
#     for i in range(day):
#         y = getdata(i,x,node_index)
#         print(y)
#         for j in range(y.shape[0]):
#             axs[i].plot(x, y[j, :], color=colors[j], label=f'station{node_index[j]}', linestyle='--')
#             axs[i].set_ylim(0,900)
#
#         # 设置子图标题为周几
#         axs[i].set_title(
#             weekdays[i],
#             fontdict={'fontsize': 14, 'color': 'red', 'weight': 'bold'},  # 设置字体大小、颜色和粗细
#             pad=20  # 标题和子图之间的距离，默认是 6，增加为 20
#         )
#
#         if i ==day-1:
#             axs[i].legend(loc='upper right')  # 控制图例的位置
#     # 调整子图之间的间距
#     plt.tight_layout()
#
#     # 显示所有子图
#     plt.show()

def drawLine(x, node_index, day=7):
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    position=[750,750,750,750,600,700,700]

    # 确保 day 不超过一周的天数
    assert day <= 7, "The number of days should not exceed 7."

    for i in range(day):
        y = getdata(i, x, node_index)  # 获取数据
        print(y)

        # 创建单独的图
        plt.figure(figsize=(2.5, 5.5))  # 设置每张图的大小
        for j in range(y.shape[0]):
            plt.plot(x, y[j, :], color=colors[j], label=f'station{node_index[j]}', linestyle='--')

        # 设置 y 轴范围
        plt.ylim(0, 900)

        # 在图形内部添加标题
        plt.text(
            x[2], position[i],  # 调整位置，x[0] 表示最左侧，950 表示接近顶部（y 值靠近 1000）
            weekdays[i],
            fontsize=20,
            color='red',
            weight='bold',
            fontfamily='Times New Roman',
            ha='center',  # 水平对齐方式为左对齐
            va='top'    # 垂直对齐方式为顶部对齐
        )

        # 显示完整的 x 轴刻度
        plt.xticks(x)
        plt.yticks([])

        # # 可选：隐藏 Y 轴线条
        # ax = plt.gca()
        # ax.spines['left'].set_visible(False)  # 隐藏左边框
        # ax.spines['right'].set_visible(False)  # 隐藏右边框
        #
        # # 创建并添加左边虚线（从 x[0] 到 x[0] 的位置）
        # left_line = Line2D([x[0], x[0]], [0, 900], color=ax.spines['top'].get_edgecolor(), linestyle='--', dashes=(4, 2))  # 设置虚线间隔
        # ax.add_line(left_line)
        #
        # # 创建并添加右边虚线（从 x[-1] 到 x[-1] 的位置）
        # right_line = Line2D([x[-1], x[-1]], [0, 900], color=ax.spines['top'].get_edgecolor(), linestyle='--',dashes=(4, 2))  # 设置虚线间隔
        # ax.add_line(right_line)

        if(i==4):
            # 添加图例
            plt.legend(loc='upper right')

        plt.show()
        plt.savefig(f"../fig/HZ_fig/FLOW/{weekdays[i]}.eps", dpi=300)
        plt.clf()
        plt.close()


if __name__ == '__main__':
    # 示例数据
    num_node = 5
    x = [8, 9, 10, 11, 12]  # x 轴数据
    # node_index = [random.randint(0,79) for _ in range(num_node)]
    node_index = [6, 37, 46, 50]
    print(node_index)

    drawLine(x, node_index)