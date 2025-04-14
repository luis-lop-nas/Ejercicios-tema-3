import pygame
from hanoi import JuegoHanoi
from visual.colores import BLANCO, GRIS, color_piedra

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
        self.juego.resolver()
        self.movimientos = self.juego.obtener_movimientos()
        self.pilas = self.juego.obtener_pilas()
        self.num_piedras = num_piedras

    def dibujar_pilas(self):
        self.ventana.fill(BLANCO)
        posiciones_x = [ESPACIADO * i + 100 for i in range(3)]

        for i, pila in enumerate(self.pilas):
            x_base = posiciones_x[i]
            pygame.draw.rect(self.ventana, GRIS, (x_base + ANCHO_BASE // 2 - 5, 100, 10, 400))  # soporte

            for j, piedra in enumerate(reversed(pila.items)):
                ancho_piedra = piedra * (ANCHO_BASE // self.num_piedras)
                x = x_base + ANCHO_BASE // 2 - ancho_piedra // 2
                y = ALTO_VENTANA - (j + 1) * ALTURA_PIEDRA - 50
                color = color_piedra(piedra)
                pygame.draw.rect(self.ventana, color, (x, y, ancho_piedra, ALTURA_PIEDRA))

        pygame.display.flip()

    def ejecutar(self):
        print("🔷 Puzzle de la Pirámide de Piedras Preciosas 🔷")
        print("En una antigua cámara secreta egipcia, deberás trasladar todas las piedras de una columna a otra.")
        print("Reglas del juego:")
        print("- Solo puedes mover una piedra a la vez.")
        print("- No puedes colocar una piedra más grande sobre una más pequeña.")
        print("- Usa la lógica para completar el puzzle con el menor número de movimientos posibles.")
        input("Pulsa ENTER para comenzar la visualización del puzzle...\n")

        seleccionada = None
        movimientos_realizados = 0
        ejecutando = True

        while ejecutando:
            self.ventana.fill(BLANCO)
            self.dibujar_pilas()

            font = pygame.font.SysFont(None, 24)
            msg = f"Movimientos: {movimientos_realizados}"
            if seleccionada is not None:
                msg += " | Selecciona pila de destino"
            texto = font.render(msg, True, (0, 0, 0))
            self.ventana.blit(texto, (10, 10))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    ejecutando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    pila_index = x // ESPACIADO
                    if pila_index > 2:
                        pila_index = 2

                    if seleccionada is None:
                        if not self.pilas[pila_index].is_empty():
                            seleccionada = pila_index
                    else:
                        origen = self.pilas[seleccionada]
                        destino = self.pilas[pila_index]
                        if origen.is_empty():
                            pass  # movimiento inválido
                        elif destino.is_empty() or origen.peek() < destino.peek():
                            destino.push(origen.pop())
                            movimientos_realizados += 1
                        seleccionada = None

                        if len(self.destino) == self.num_piedras:
                            self.dibujar_pilas()
                            texto = font.render(f"¡Puzzle resuelto en {movimientos_realizados} movimientos!", True, (0, 100, 0))
                            self.ventana.blit(texto, (10, 40))
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            ejecutando = False

            self.reloj.tick(FPS)

        pygame.quit()