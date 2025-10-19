import numpy as np
from metodos.gauss import gauss_eliminacion
from metodos.gauss_jordan import gauss_jordan
from metodos.lu import descomposicion_LU

def menu():
    print("\n--- SISTEMAS DE ECUACIONES LINEALES ---")
    print("1. Método de Eliminación de Gauss")
    print("2. Método de Gauss-Jordan")
    print("3. Descomposición LU")
    print("4. Salir")
    return input("Seleccione una opción: ")

def ingresar_datos():
    n = int(input("Ingrese el número de ecuaciones: "))
    A = np.zeros((n, n))
    b = np.zeros(n)

    print("\nIngrese los coeficientes del sistema Ax = b:")
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"A[{i+1},{j+1}]: "))
        b[i] = float(input(f"b[{i+1}]: "))
    return A, b

def main():
    while True:
        opcion = menu()
        if opcion == "4":
            print("Saliendo del programa...")
            break

        A, b = ingresar_datos()

        if opcion == "1":
            print("\n--- MÉTODO DE ELIMINACIÓN DE GAUSS ---")
            x = gauss_eliminacion(A.copy(), b.copy())
        elif opcion == "2":
            print("\n--- MÉTODO DE GAUSS-JORDAN ---")
            x = gauss_jordan(A.copy(), b.copy())
        elif opcion == "3":
            print("\n--- DESCOMPOSICIÓN LU ---")
            x = descomposicion_LU(A.copy(), b.copy())
        else:
            print("Opción inválida.")
            continue

        print("\nSolución del sistema:")
        print(x)

if __name__ == "__main__":
    main()
