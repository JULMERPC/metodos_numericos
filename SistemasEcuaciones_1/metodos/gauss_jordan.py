import numpy as np 
"""Importa la librería NumPy para manejar operaciones matriciales y arreglos numéricos"""

def gauss_jordan(A, b):
    n = len(b)
    Ab = np.concatenate((A, b.reshape(-1,1)), axis=1)
    for i in range(n):
        Ab[i] = Ab[i] / Ab[i][i]
        for j in range(n):
            if i != j:
                Ab[j] = Ab[j] - Ab[j][i]*Ab[i]
    x = Ab[:, -1]
    return x
