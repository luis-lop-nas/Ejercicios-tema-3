from pila import Pila
from utils import mostrar_pilas

class JuegoHanoi:
    def __init__(self, num_piedras=5):
        self.num_piedras = num_piedras
        self.origen = Pila()
        self.auxiliar = Pila()
        self.destino = Pila()
        self._cargar_piedras()

    def _cargar_piedras(self):
        for i in range(self.num_piedras, 0, -1):
            self.origen.push(i)

    def resolver(self):
        mostrar_pilas(self.origen, self.auxiliar, self.destino)
        self._mover_piedras(self.num_piedras, self.origen, self.destino, self.auxiliar)
        mostrar_pilas(self.origen, self.auxiliar, self.destino)
        print("Puzzle resuelto.")

    def _mover_piedras(self, n, origen, destino, auxiliar):
        if n == 1:
            destino.push(origen.pop())
        else:
            self._mover_piedras(n - 1, origen, auxiliar, destino)
            destino.push(origen.pop())
            self._mover_piedras(n - 1, auxiliar, destino, origen)