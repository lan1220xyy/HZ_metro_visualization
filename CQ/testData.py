import pickle
import os
import numpy as np

# 替换 'your_file.pkl' 为你的文件路径
with open('./mydata/HZMetro/test.pkl', 'rb') as file:
    data = pickle.load(file)

# 打印加载的数据
x = data["x"]
y = data["y"]
x_t = data["xtime"]
y_t = data["ytime"]

print(type(data))
print(data.keys())
print(x.shape)
print(x_t.shape)

data_path = os.path.join('./mydata/PEMSD4/pems04.npz')
data1 = np.load(data_path)['data'][:,:,0]
print(data1.shape)
#其中PEMS04是2018年1月1日开始采集的连续59天的307的探测器获得的流量数据，每5分钟采集一次，所以原始流量数据data.npz读取后shape为(307, 16992, 3)，其中3维特征为flow, occupy, speed，原始邻接矩阵数据是一个distance.csv文件，它包含是from,to,distance的格式，方便起见，本文距离（对应图上的边权）只要节点相连都取1。相似的是，PEMS08是2016年7月1日开始采集的连续62天170个节点的流量数据，其数据shape为(170, 17856, 3)。

for i in range(5):
    print(data1[i])
