import numpy as np
from metodos.unidimensional import optimizacion_unidimensional
from metodos.multidimensional import optimizacion_multidimensional
from metodos.restricciones import optimizacion_con_restricciones

def menu():
    print("\n=== MENÚ DE OPTIMIZACIÓN ===")
    print("1. Optimización Unidimensional")
    print("2. Optimización Multidimensional (sin restricciones)")
    print("3. Optimización con Restricciones")
    print("4. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Optimización Unidimensional ---")
        expr = input("Ingrese la función f(x): (ej. x**2 + 3*x + 2): ")
        a = float(input("Límite inferior a: "))
        b = float(input("Límite superior b: "))
        optimizacion_unidimensional(expr, a, b)

    elif opcion == "2":
        print("\n--- Optimización Multidimensional ---")
        expr = input("Ingrese la función f(x, y): (ej. x**2 + y**2 + x*y): ")
        x0 = list(map(float, input("Ingrese valores iniciales separados por coma (ej. 1,2): ").split(",")))
        optimizacion_multidimensional(expr, x0)

    elif opcion == "3":
        print("\n--- Optimización con Restricciones ---")
        expr = input("Ingrese la función f(x, y): (ej. x**2 + y**2): ")
        restr = input("Restricción g(x, y)=0 (ej. x + y - 1): ")
        x0 = list(map(float, input("Ingrese valores iniciales separados por coma (ej. 0.5,0.5): ").split(",")))
        optimizacion_con_restricciones(expr, restr, x0)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
