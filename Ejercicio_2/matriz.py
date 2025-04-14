class Matriz:
    def __init__(self, datos):
        self.datos = datos
        self.n = len(datos)

    def obtener_elemento(self, fila, col):
        return self.datos[fila][col]

    def dimension(self):
        return self.n

    def submatriz(self, fila_excluida, col_excluida):
        nueva = [
            [self.datos[i][j] for j in range(self.n) if j != col_excluida]
            for i in range(self.n) if i != fila_excluida
        ]
        return Matriz(nueva)

    def mostrar(self):
        for fila in self.datos:
            print(fila)