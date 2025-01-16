import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

def show(dir,dataset,len,dim):
    file_directory = f"../fig/{dataset}_fig/{dir}/{dim}/0"
    if(len==18):
        n_rows,n_cols=3,6
    else:
        n_rows,n_cols=2,4
    files = [f for f in os.listdir(file_directory) if f.endswith('.eps')]
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 8))
    # 遍历 EPS 文件并显示在子图中
    for i, file in enumerate(files):
        row = i // n_cols
        col = i % n_cols
        img = imread(os.path.join(file_directory, file))
        axes[row, col].imshow(img)
        axes[row, col].axis('off')  # 隐藏坐标轴

    # 如果有空白的子图格子，可以将其坐标轴关闭
    for j in range(i + 1, n_rows * n_cols):
        row = j // n_cols
        col = j % n_cols
        axes[row, col].axis('off')

    plt.tight_layout()
    plt.show()
    plt.clf()

def show_fig(dataset,type,dim,len):
    file_directory = f"../fig/{dataset}_fig/{type}/{dim}"
    if(len==24):
        n_rows,n_cols=4,6
    else:
        n_rows,n_cols=2,4
    files = [f for f in os.listdir(file_directory) if f.endswith('.eps')]
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 8))
    # 遍历 EPS 文件并显示在子图中
    for i, file in enumerate(files):
        row = i // n_cols
        col = i % n_cols
        img = imread(os.path.join(file_directory, file))
        axes[row, col].imshow(img)
        axes[row, col].axis('off')  # 隐藏坐标轴

    # 如果有空白的子图格子，可以将其坐标轴关闭
    for j in range(i + 1, n_rows * n_cols):
        row = j // n_cols
        col = j % n_cols
        axes[row, col].axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    dataset = "P4"
    type = "DAYS"
    dim_list = [2,10]
    for dim in dim_list:
        show_fig(dataset,type,dim,7)