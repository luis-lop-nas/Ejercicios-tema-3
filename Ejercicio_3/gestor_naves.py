from nave import Nave

class GestorNaves:
    @staticmethod
    def ordenar_por_nombre(naves):
        return sorted(naves, key=lambda n: n.nombre)

    @staticmethod
    def ordenar_por_longitud_desc(naves):
        return sorted(naves, key=lambda n: n.longitud, reverse=True)

    @staticmethod
    def buscar_por_nombre(naves, nombres):
        return [n for n in naves if n.nombre in nombres]

    @staticmethod
    def top_pasajeros(naves, top=5):
        return sorted(naves, key=lambda n: n.pasajeros, reverse=True)[:top]

    @staticmethod
    def nave_mayor_tripulacion(naves):
        return max(naves, key=lambda n: n.tripulantes)

    @staticmethod
    def nombres_empiezan_con(naves, prefijo):
        return [n for n in naves if n.nombre.startswith(prefijo)]

    @staticmethod
    def naves_con_pasajeros_minimos(naves, minimo=6):
        return [n for n in naves if n.pasajeros >= minimo]

    @staticmethod
    def nave_mas_grande(naves):
        return max(naves, key=lambda n: n.longitud)

    @staticmethod
    def nave_mas_pequena(naves):
        return min(naves, key=lambda n: n.longitud)
