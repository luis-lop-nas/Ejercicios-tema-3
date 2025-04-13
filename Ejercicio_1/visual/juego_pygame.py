import pygame
from hanoi import JuegoHanoi
from colores import *

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
FPS = 60

NUM_PIEDRAS = 5
ALTURA_PIEDRA = 20
ANCHO_BASE = 200
ESPACIADO = 250
DELAY = 500  # milisegundos entre movimientos

class VisualizadorHanoi:
    def __init__(self, num_piedras):
        pygame.init()
        self.ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption("Puzzle de la Pirámide de Piedras Preciosas")
        self.reloj = pygame.time.Clock()
        self.juego = JuegoHanoi(num_piedras)
        self.movimientos = self.juego.obtener_movimientos()
        self.pilas = self.juego.obtener_pilas()

    def dibujar_pilas(self):
        self.ventana.fill(BLANCO)
        posiciones_x = [ESPACIADO * i + 100 for i in range(3)]

        for i, pila in enumerate(self.pilas):
            x_base = posiciones_x[i]
            pygame.draw.rect(self.ventana, GRIS, (x_base + ANCHO_BASE // 2 - 5, 100, 10, 400))  # soporte

            for j, piedra in enumerate(reversed(pila.items)):
                ancho_piedra = piedra * (ANCHO_BASE // NUM_PIEDRAS)
                x = x_base + ANCHO_BASE // 2 - ancho_piedra // 2
                y = ALTO_VENTANA - (j + 1) * ALTURA_PIEDRA - 50
                pygame.draw.rect(self.ventana, AZUL, (x, y, ancho_piedra, ALTURA_PIEDRA))

        pygame.display.flip()

    def animar_movimientos(self):
        for origen, destino in self.movimientos:
            self.dibujar_pilas()
            pygame.time.delay(DELAY)
            destino.push(origen.pop())
            self.dibujar_pilas()
            pygame.time.delay(DELAY)

    def ejecutar(self):
        self.dibujar_pilas()
        pygame.time.delay(1000)
        self.animar_movimientos()

        ejecutando = True
        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        ejecutando = False

            self.reloj.tick(FPS)

        pygame.quit()


if __name__ == "__main__":
    visualizador = VisualizadorHanoi(NUM_PIEDRAS)
    visualizador.ejecutar()