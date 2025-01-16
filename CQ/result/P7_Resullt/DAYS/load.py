import torch
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def matrix_list(num):
    matrix_list = []
    for i in range(1, 6):

        # 加载模型参数
        state_dict = torch.load(f'./{num}dim/{i}/best_model.pth')
        node_embeddings = state_dict["node_embeddings"].cpu().numpy()
        print(node_embeddings.shape)
        A = np.dot(node_embeddings, node_embeddings.T)
        matrix_list.append(A)
    return matrix_list
