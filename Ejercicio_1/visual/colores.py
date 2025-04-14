BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)
AZUL = (0, 102, 204)
VERDE = (0, 153, 0)
ROJO = (204, 0, 0)
AMARILLO = (255, 204, 0)
MORADO = (153, 0, 204)
CELESTE = (0, 204, 204)

_PALETA = [AZUL, VERDE, ROJO, AMARILLO, MORADO, CELESTE]

def color_piedra(tamaño):
    return _PALETA[(tamaño - 1) % len(_PALETA)]