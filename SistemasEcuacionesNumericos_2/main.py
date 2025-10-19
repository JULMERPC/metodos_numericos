#!/usr/bin/env python3
"""
Aplicación simple para resolver sistemas lineales Ax = b
usando métodos numéricos:
 - Cholesky
 - Jacobi
 - Gauss-Seidel
"""

import numpy as np
from metodos.cholesky import cholesky_solve
from metodos.iterativos import jacobi, gauss_seidel

def leer_matriz_y_vector():
    """Permite ingresar una matriz cuadrada A y un vector b."""
    n = int(input("Ingrese el tamaño n de la matriz A (n x n): "))
    A = np.zeros((n, n), dtype=float)
    print("Ingrese las filas de A (separe los valores con espacios):")
    for i in range(n):
        while True:
            try:
                fila = list(map(float, input(f"Fila {i+1}: ").split()))
                if len(fila) != n:
                    print(f"Debe ingresar exactamente {n} valores.")
                    continue
                A[i] = fila
                break
            except ValueError:
                print("Error: ingrese solo números.")
    while True:
        try:
            b = list(map(float, input(f"Ingrese el vector b ({n} valores separados por espacio): ").split()))
            if len(b) != n:
                print(f"Debe ingresar exactamente {n} valores.")
                continue
            b = np.array(b, dtype=float)
            break
        except ValueError:
            print("Error: ingrese solo números.")
    return A, b

def menu():
    print("\n=== SISTEMAS DE ECUACIONES LINEALES ===")
    print("1) Método de Cholesky")
    print("2) Método de Jacobi")
    print("3) Método de Gauss-Seidel")
    print("4) Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        op = menu()
        if op == "1":
            print("\n--- Método de Cholesky ---")
            A, b = leer_matriz_y_vector()
            try:
                x = cholesky_solve(A, b)
                print("\nSolución encontrada:")
                print(x)
            except Exception as e:
                print("Error:", e)

        elif op == "2":
            print("\n--- Método de Jacobi ---")
            A, b = leer_matriz_y_vector()
            tol = float(input("Ingrese tolerancia (ejemplo: 1e-6): ") or 1e-6)
            max_iter = int(input("Ingrese el máximo de iteraciones (ejemplo: 1000): ") or 1000)
            x, it, conv = jacobi(A, b, tol=tol, max_iter=max_iter)
            print(f"\nConvergió: {conv} en {it} iteraciones.")
            print("Aproximación de x:")
            print(x)

        elif op == "3":
            print("\n--- Método de Gauss-Seidel ---")
            A, b = leer_matriz_y_vector()
            tol = float(input("Ingrese tolerancia (ejemplo: 1e-6): ") or 1e-6)
            max_iter = int(input("Ingrese el máximo de iteraciones (ejemplo: 1000): ") or 1000)
            x, it, conv = gauss_seidel(A, b, tol=tol, max_iter=max_iter)
            print(f"\nConvergió: {conv} en {it} iteraciones.")
            print("Aproximación de x:")
            print(x)

        elif op == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
