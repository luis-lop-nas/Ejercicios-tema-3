from matriz import Matriz
from determinante import determinante_recursivo, determinante_iterativo

def ejecutar():
    datos = [
        [2, 5, 3],
        [1, -2, -1],
        [1, 3, 4]
    ]

    matriz = Matriz(datos)
    print("Matriz original:")
    matriz.mostrar()

    det_recursivo = determinante_recursivo(matriz)
    print("\nDeterminante (método recursivo):", det_recursivo)

    det_iterativo = determinante_iterativo(matriz)
    print("Determinante (método iterativo):", det_iterativo)