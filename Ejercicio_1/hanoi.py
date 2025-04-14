from pila import Pila
from utils import mostrar_pilas

class JuegoHanoi:
    def __init__(self, num_piedras=5):
        self.num_piedras = num_piedras
        self.origen = Pila()
        self.auxiliar = Pila()
        self.destino = Pila()
        self.movimientos = []
        self._cargar_piedras()

    def _cargar_piedras(self):
        for i in range(self.num_piedras, 0, -1):
            self.origen.push(i)

    def resolver(self):
        self._mover_piedras(self.num_piedras, self.origen, self.destino, self.auxiliar)

    def _mover_piedras(self, n, origen, destino, auxiliar):
        if n == 1:
            self.movimientos.append((origen, destino))
            destino.push(origen.pop())
        else:
            self._mover_piedras(n - 1, origen, auxiliar, destino)
            self.movimientos.append((origen, destino))
            destino.push(origen.pop())
            self._mover_piedras(n - 1, auxiliar, destino, origen)

    def obtener_pilas(self):
        return self.origen, self.auxiliar, self.destino

    def obtener_movimientos(self):
        return self.movimientos