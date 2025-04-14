from matriz import Matriz
from determinante import determinante_recursivo, determinante_iterativo
import random

def ejecutar():
    while True:
        try:
            n = int(input("Introduce el tamaño de la matriz cuadrada (n x n): "))
            if n <= 0:
                print("El tamaño debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    datos = []
    modo = input("¿Quieres introducir la matriz manualmente (M) o generarla aleatoriamente (A)? [M/A]: ").strip().upper()
    if modo == 'A':
        datos = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
        print("\nMatriz generada aleatoriamente:")
    else:
        print(f"Introduce los {n}x{n} elementos de la matriz fila por fila (separados por espacios):")
        for i in range(n):
            while True:
                try:
                    fila = list(map(float, input(f"Fila {i + 1}: ").strip().split()))
                    if len(fila) != n:
                        print(f"La fila debe tener exactamente {n} elementos.")
                        continue
                    datos.append(fila)
                    break
                except ValueError:
                    print("Introduce solo números válidos separados por espacios.")

    matriz = Matriz(datos)
    print("\nMatriz introducida:")
    matriz.mostrar()

    det_recursivo = determinante_recursivo(matriz)
    print("\nDeterminante (método recursivo):", det_recursivo)

    det_iterativo = determinante_iterativo(matriz)
    print("Determinante (método iterativo):", det_iterativo)