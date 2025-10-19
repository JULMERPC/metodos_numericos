"""
Método de Cholesky
A = L * L^T
Solo funciona si A es simétrica y definida positiva.
"""

import numpy as np

def is_symmetric(A, tol=1e-10):
    return np.allclose(A, A.T, atol=tol)

def cholesky_decomposition(A):
    A = np.array(A, dtype=float)
    n = A.shape[0]
    if not is_symmetric(A):
        raise ValueError("La matriz A no es simétrica.")
    L = np.zeros_like(A)
    for i in range(n):
        for j in range(i + 1):
            suma = np.dot(L[i, :j], L[j, :j])
            if i == j:
                val = A[i, i] - suma
                if val <= 0:
                    raise ValueError("La matriz no es definida positiva.")
                L[i, j] = np.sqrt(val)
            else:
                L[i, j] = (A[i, j] - suma) / L[j, j]
    return L

def forward_substitution(L, b):
    n = len(b)
    y = np.zeros_like(b)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y

def backward_substitution(U, y):
    n = len(y)
    x = np.zeros_like(y)
    for i in reversed(range(n)):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

def cholesky_solve(A, b):
    L = cholesky_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(L.T, y)
    return x
