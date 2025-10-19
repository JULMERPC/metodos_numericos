import numpy as np

def gauss_eliminacion(A, b):
    n = len(b)
    for k in range(n-1):
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x
