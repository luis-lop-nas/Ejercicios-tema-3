def es_matriz_cuadrada(matriz):
    return all(len(fila) == len(matriz) for fila in matriz)