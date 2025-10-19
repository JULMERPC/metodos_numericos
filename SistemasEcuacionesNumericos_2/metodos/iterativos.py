"""
Métodos iterativos para resolver Ax = b:
 - Jacobi
 - Gauss-Seidel
"""

import numpy as np

def jacobi(A, b, x0=None, tol=1e-6, max_iter=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
    D = np.diag(A)
    R = A - np.diagflat(D)
    for it in range(1, max_iter + 1):
        if np.any(D == 0):
            raise ZeroDivisionError("La diagonal contiene ceros, no se puede usar Jacobi.")
        x_new = (b - np.dot(R, x)) / D
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new, it, True
        x = x_new
    return x, max_iter, False

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
    for it in range(1, max_iter + 1):
        x_new = x.copy()
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            if A[i, i] == 0:
                raise ZeroDivisionError("Cero en la diagonal.")
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new, it, True
        x = x_new
    return x, max_iter, False
