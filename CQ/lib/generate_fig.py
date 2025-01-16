import random

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd


os.environ['KMP_DUPLICATE_LIB_OK']='True'


#todo:  1.写接口loaddata:  读取24个小时的数据 即24个矩阵   228*228  取6*6即可
#       2.把邻接矩阵存下来，加快画图速度
#       3.写接口savefig:  传入矩阵 生成热力图  保存在目录fig中
#       4.写接口画折线图
#       5.写执行文件

def savefig(dataset,matrix,rows,cols,folder,index,max,min,dim,type):
    num=17 if type=="HOURS" else 6
    cbar = True if index == num else False
    ax = sns.heatmap(matrix,cmap='coolwarm',vmin=min,vmax=max, cbar=cbar,square=True)

    ax.set_xticklabels(rows,fontsize=20,fontfamily='serif')  #设置自定义标签
    ax.xaxis.tick_top()     #X轴上移
    ax.set_yticklabels(cols,fontsize=20,fontfamily='serif')

    if type == "HOURS":
        plt.title(f"{index}:00",y=-0.15,fontsize=24,fontfamily='serif')
    else:
        dic = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5:'Saturday', 6:'Sunday'}
        plt.title(f"{dic[index]}",y=-0.15,fontsize=24,fontfamily='serif')

    des = os.path.abspath(os.path.join(os.getcwd(),'../'))
    plt.savefig(f"{des}/fig/{dataset}_fig/{type}/{dim}/{folder}/{index}.eps", dpi=300)
    plt.clf()
    plt.close()

def generate_col_row(size=5):
    if size > 80:
        raise ValueError("Size cannot be greater than the range (80) to ensure unique values.")
    cols = sorted(random.sample(range(80), size))  # 从范围内生成不重复随机数并排序
    rows = cols
    return cols, rows

def get_from_csv(dataset,rows,cols,path,dim,len):
    m_list = []
    v_min = 100
    v_max = -100
    index = list(range(len))
    for i in index:
        df = pd.read_csv(f'../matrix/{dataset}_matrix/{path}/{dim}/matrix_{i}.csv',header=None)
        matrix = df.to_numpy()
        sub_matrix = matrix[np.ix_(rows,cols)]
        print(sub_matrix)
        v_max = sub_matrix.max() if sub_matrix.max() > v_max else v_max
        v_min = sub_matrix.min() if sub_matrix.min() < v_min else v_min
        m_list.append(sub_matrix)
    return m_list,v_max,v_min

def myFig(dataset,dim,path,len,times=1):
    for i in range(times):
        # cols,rows = generate_col_row()           #[9,19,37,42,63]  [3,4,5,58,69]
        cols = rows = [6,37,46,50]
        list,max,min = get_from_csv(dataset,rows, cols, path, dim, len)
        for j,matrix in enumerate(list):
            savefig(dataset,matrix,rows,cols,i,j,max,min,dim,path)


def get_adj_matrix_csv(rows,cols,dataset,type,dim):
    m_list = []
    v_min = 100
    v_max = -100
    len = 7 if type=="DAYS" else 24
    index = list(range(len))
    for i in index:
        df = pd.read_csv(f'../matrix/{dataset}_matrix/{type}/{dim}/matrix_{i}.csv',header=None)
        matrix = df.to_numpy()
        sub_matrix = matrix[np.ix_(rows,cols)]
        print(sub_matrix)
        v_max = sub_matrix.max() if sub_matrix.max() > v_max else v_max
        v_min = sub_matrix.min() if sub_matrix.min() < v_min else v_min
        m_list.append(sub_matrix)
    return m_list,v_max,v_min

def save_fig(matrix,rows,cols,index,max,min,dim,type,dataset):
    num=23 if type=="DAYS" else 6
    cbar = True if index == num else False
    ax = sns.heatmap(matrix,cmap='coolwarm',vmin=min,vmax=max, cbar=cbar)

    ax.set_xticklabels(rows)  #设置自定义标签
    ax.xaxis.tick_top()     #X轴上移
    ax.set_yticklabels(cols)

    if type == "days":
        plt.title(f"{index}:00",y=-0.08)
    else:
        dic = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5:'Saturday',6:'Sunday'}
        plt.title(f"{dic[index]}",y=-0.08)

    des = os.path.abspath(os.path.join(os.getcwd(),'../'))
    plt.savefig(f"{des}/fig/{dataset}_fig/{type}/{dim}/{index}.eps", dpi=300)
    plt.clf()

def generate_my_fig(dataset,type,cols,rows,dim,times):
    for i in range(times):
        list,max,min = get_adj_matrix_csv(rows, cols, dataset, type,dim )
        print(len(list))
        for j,matrix in enumerate(list):
            save_fig(matrix,rows,cols,j,max,min,dim,type,dataset)

if __name__ == '__main__':
    dataset = "P4"
    dim_list = [2,10]
    type = "DAYS"
    times = 1
    cols, rows = generate_col_row()
    for dim in dim_list:
        generate_my_fig(dataset,type,cols,rows,dim,times)
    # generate_my_fig("P4","DAYS",10,1)