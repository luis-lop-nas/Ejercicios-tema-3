# pila.py
class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items[::-1])


# utils.py (opcional)
def mostrar_pilas(origen, auxiliar, destino):
    print("\nEstado actual de las pilas:")
    print(f"Origen  : {origen}")
    print(f"Auxiliar: {auxiliar}")
    print(f"Destino : {destino}\n")


# hanoi.py
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
        mostrar_pilas(self.origen, self.auxiliar, self.destino)
        self._mover_piedras(self.num_piedras, self.origen, self.destino, self.auxiliar)
        mostrar_pilas(self.origen, self.auxiliar, self.destino)
        print("Puzzle resuelto.")

    def _mover_piedras(self, n, origen, destino, auxiliar):
        if n == 1:
            destino.push(origen.pop())
            self.movimientos.append((origen, destino))
        else:
            self._mover_piedras(n - 1, origen, auxiliar, destino)
            destino.push(origen.pop())
            self.movimientos.append((origen, destino))
            self._mover_piedras(n - 1, auxiliar, destino, origen)

    def obtener_pilas(self):
        return self.origen, self.auxiliar, self.destino

    def obtener_movimientos(self):
        return self.movimientos


# main.py
from hanoi import JuegoHanoi

if __name__ == "__main__":
    juego = JuegoHanoi(num_piedras=5)  # Cambia a 74 si quieres el reto completo
    juego.resolver()
