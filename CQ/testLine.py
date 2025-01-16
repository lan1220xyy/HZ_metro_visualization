import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = [1, 2, 3, 4, 5]
y_values = [
    [1, 4, 9, 16, 25],
    [2, 3, 5, 7, 11],
    [3, 6, 9, 12, 15],
    [4, 8, 12, 16, 20],
    [5, 10, 15, 20, 25]
]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# 创建 1 行 5 列的子图
fig, axs = plt.subplots(1, 5, figsize=(15, 5))

# 绘制每个子图
for i in range(5):
    axs[i].plot(x, y_values[i], color=colors[i], linestyle='--', linewidth=2, label=f'Line {i + 1}')
    axs[i].set_title(f"Line Chart {i + 1}")
    axs[i].set_xlabel("X Axis")
    axs[i].set_ylabel("Y Axis")
    axs[i].legend()
    axs[i].grid(True)

# 调整子图之间的间距
plt.tight_layout()

# 显示所有子图
plt.show()
