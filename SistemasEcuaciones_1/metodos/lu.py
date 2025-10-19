import numpy as np

def descomposicion_LU(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i+1, n):
            L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]

    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][k]*y[k] for k in range(i))
    
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i][k]*x[k] for k in range(i+1, n))) / U[i][i]
    
    return x
