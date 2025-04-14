import pygame
from hanoi import JuegoHanoi
from visual.colores import BLANCO, GRIS, color_piedra
import os

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
        self.sonido_valido = pygame.mixer.Sound("sonidos/movimiento_valido.wav")
        self.sonido_invalido = pygame.mixer.Sound("sonidos/movimiento_invalido.wav")
        self.sonido_victoria = pygame.mixer.Sound("sonidos/victoria.wav")
        self.ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption("Puzzle de la Pirámide de Piedras Preciosas")
        self.reloj = pygame.time.Clock()
        self.juego = JuegoHanoi(num_piedras)
        self.juego.resolver()
        self.movimientos = self.juego.obtener_movimientos()
        self.pilas = self.juego.obtener_pilas()
        self.num_piedras = num_piedras

    def reconocer_ruta_record(self):
        self.archivo_record = "record_hanoi.txt"
        if not os.path.exists(self.archivo_record):
            with open(self.archivo_record, "w") as f:
                pass

    def cargar_record(self, num_piedras):
        with open(self.archivo_record, "r") as f:
            for linea in f:
                partes = linea.strip().split(":")
                if len(partes) == 2 and partes[0] == str(num_piedras):
                    return int(partes[1])
        return None

    def guardar_record(self, num_piedras, movimientos):
        lineas = []
        actualizado = False
        if os.path.exists(self.archivo_record):
            with open(self.archivo_record, "r") as f:
                lineas = f.readlines()

        with open(self.archivo_record, "w") as f:
            for linea in lineas:
                partes = linea.strip().split(":")
                if len(partes) == 2 and partes[0] == str(num_piedras):
                    if movimientos < int(partes[1]):
                        f.write(f"{num_piedras}:{movimientos}\n")
                    else:
                        f.write(linea)
                    actualizado = True
                else:
                    f.write(linea)
            if not actualizado:
                f.write(f"{num_piedras}:{movimientos}\n")

    def dibujar_pilas(self, seleccionada=None):
        self.ventana.fill(BLANCO)
        posiciones_x = [ESPACIADO * i + 100 for i in range(3)]

        for i, pila in enumerate(self.pilas):
            x_base = posiciones_x[i]
            if seleccionada == i:
                pygame.draw.rect(self.ventana, (255, 0, 0), (x_base, 90, ANCHO_BASE, 420), 3)
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

        mensaje_error = ""
        tiempo_error = 0

        while True:
            entrada = input("¿Cuántas piedras quieres usar? (mínimo 3, máximo 10)? Pulsa ENTER para usar 5: ").strip()
            if entrada == "":
                cantidad = 5
                break
            try:
                cantidad = int(entrada)
                if 3 <= cantidad <= 10:
                    break
                else:
                    print("Por favor, elige un número entre 3 y 10.")
            except ValueError:
                print("Entrada no válida. Introduce un número.")

        self.num_piedras = cantidad
        self.reconocer_ruta_record()
        mejor_puntaje = self.cargar_record(self.num_piedras)
        self.juego = JuegoHanoi(self.num_piedras)
        self.juego.resolver()
        self.pilas = self.juego.obtener_pilas()

        seleccionada = None
        movimientos_realizados = 0
        victoria = False
        ejecutando = True

        while ejecutando:
            self.ventana.fill(BLANCO)
            self.dibujar_pilas(seleccionada)

            font = pygame.font.SysFont(None, 24)
            msg = f"Movimientos: {movimientos_realizados}"
            if mejor_puntaje is not None:
                msg += f" | Récord: {mejor_puntaje}"
            if seleccionada is not None:
                msg += " | Selecciona pila de destino"
            texto = font.render(msg, True, (0, 0, 0))
            self.ventana.blit(texto, (10, 10))

            if mensaje_error:
                error_text = font.render(mensaje_error, True, (255, 0, 0))
                self.ventana.blit(error_text, (10, 35))
                if pygame.time.get_ticks() - tiempo_error > 2000:
                    mensaje_error = ""

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        ejecutando = False
                    elif evento.key == pygame.K_r and victoria:
                        self.__init__(self.num_piedras)
                        self.ejecutar()
                        return
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
                            self.sonido_invalido.play()  # movimiento inválido
                            mensaje_error = "Movimiento inválido"
                            tiempo_error = pygame.time.get_ticks()
                        elif destino.is_empty() or origen.peek() < destino.peek():
                            destino.push(origen.pop())
                            self.sonido_valido.play()  # movimiento válido
                            movimientos_realizados += 1
                        seleccionada = None

                        if len(self.destino) == self.num_piedras:
                            self.dibujar_pilas()
                            self.sonido_victoria.play()  # puzzle resuelto
                            if mejor_puntaje is None or movimientos_realizados < mejor_puntaje:
                                self.guardar_record(self.num_piedras, movimientos_realizados)
                                mejor_puntaje = movimientos_realizados
                            texto = font.render(f"¡Puzzle resuelto en {movimientos_realizados} movimientos!", True, (0, 100, 0))
                            self.ventana.blit(texto, (10, 40))
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            victoria = True
                            ejecutando = False

            self.reloj.tick(FPS)

        if victoria:
            texto2 = font.render("Pulsa R para reiniciar o ESC para salir", True, (0, 0, 0))
            self.ventana.blit(texto2, (10, 65))

        pygame.quit()