def determinante_recursivo(matriz):
    if matriz.dimension() == 1:
        return matriz.obtener_elemento(0, 0)

    if matriz.dimension() == 2:
        return (
            matriz.obtener_elemento(0, 0) * matriz.obtener_elemento(1, 1)
            - matriz.obtener_elemento(0, 1) * matriz.obtener_elemento(1, 0)
        )

    det = 0
    for col in range(matriz.dimension()):
        signo = (-1) ** col
        sub = matriz.submatriz(0, col)
        det += signo * matriz.obtener_elemento(0, col) * determinante_recursivo(sub)
    return det


def determinante_iterativo(matriz):
    import copy
    datos = copy.deepcopy(matriz.datos)
    n = matriz.dimension()
    det = 1

    for i in range(n):
        if datos[i][i] == 0:
            for j in range(i + 1, n):
                if datos[j][i] != 0:
                    datos[i], datos[j] = datos[j], datos[i]
                    det *= -1
                    break
            else:
                return 0

        det *= datos[i][i]
        for j in range(i + 1, n):
            factor = datos[j][i] / datos[i][i]
            for k in range(i, n):
                datos[j][k] -= factor * datos[i][k]

    return round(det)