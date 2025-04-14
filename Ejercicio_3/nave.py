class Nave:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def mostrar_info(self):
        print(f"Nombre     : {self.nombre}")
        print(f"Longitud   : {self.longitud} metros")
        print(f"Tripulantes: {self.tripulantes}")
        print(f"Pasajeros  : {self.pasajeros}")
        print("-" * 30)
