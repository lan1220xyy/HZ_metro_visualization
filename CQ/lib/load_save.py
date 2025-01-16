import torch
import numpy as np
import csv
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
def loaddata(dim,len,type="HOURS"):
    matrix_list = []
    for i in range(len):
        state_dict = torch.load(f'../result/datapth/{type}/data{i}/{dim}/best_model.pth')
        node_embeddings = state_dict["node_embeddings"].cpu().numpy()
        print(node_embeddings.shape)
        A = np.dot(node_embeddings, node_embeddings.T)
        matrix_list.append(A)
    return matrix_list

def save_as_csv(matrix_list):
    for idx,matrix in enumerate(matrix_list):
        print(matrix)
        filename = f'../result/days/10dim/matrix_{idx}.csv'
        with open(filename,mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(matrix)

def loaddatabyweekdays(dim,len,type="week"):
    matrix_list = []
    for i in range(1,len):
        state_dict = torch.load(f'../result/datapth/{type}/{dim}dim/{i}/best_model.pth')
        node_embeddings = state_dict["node_embeddings"].cpu().numpy()
        print(node_embeddings.shape)
        A = np.dot(node_embeddings, node_embeddings.T)
        matrix_list.append(A)
    return matrix_list

def save_as_csv_1(matrix_list,path,dim):
    for idx,matrix in enumerate(matrix_list):
        print(matrix)
        filename = f'../result/{path}/{dim}dim/matrix_{idx}.csv'
        with open(filename,mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(matrix)

def compute_adj_matrix(dim,len,dataset,type):
    matrix_list = []
    for i in range(len):
        state_dict = torch.load(f'../{dataset}_Result/{type}/{dim}/data{i}/best_model.pth')
        node_embeddings = state_dict["node_embeddings"].cpu().numpy()
        print(node_embeddings.shape)
        A = np.dot(node_embeddings, node_embeddings.T)
        matrix_list.append(A)
    return matrix_list

def save_adj_matrix(matrix_list,dataset,dim,type):
    for idx,matrix in enumerate(matrix_list):
        print(matrix)
        filename = f'../matrix/{dataset}_matrix/{type}/{dim}/matrix_{idx}.csv'
        with open(filename,mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(matrix)

# m = loaddatabyweekdays(10,6)
# save_as_csv_1(m,"week",10)
if __name__ == '__main__':
    dim = 10
    len = 7
    dataset = "HZ"
    type = "DAYS"
    list = compute_adj_matrix(dim,len,dataset,type)
    print(list[1].shape)
    save_adj_matrix(list,dataset, dim, type)
