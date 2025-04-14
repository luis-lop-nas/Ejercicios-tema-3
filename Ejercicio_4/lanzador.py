from polinomio import Polinomio
from operaciones import restar_polinomios, eliminar_termino, existe_termino

def dividir_polinomios(dividendo, divisor):
    cociente = Polinomio()
    resto = Polinomio()
    for exp, coef in dividendo.terminos.items():
        resto.agregar_termino(coef, exp)

    exp_dvs = max(divisor.terminos)
    coef_dvs = divisor.terminos[exp_dvs]

    while resto.terminos and max(resto.terminos) >= exp_dvs:
        exp_div = max(resto.terminos)
        coef_div = resto.terminos[exp_div]

        nuevo_exp = exp_div - exp_dvs
        nuevo_coef = coef_div / coef_dvs
        cociente.agregar_termino(nuevo_coef, nuevo_exp)

        # Multiplicar divisor por el nuevo término y restar del resto
        temp = Polinomio()
        for exp, coef in divisor.terminos.items():
            temp.agregar_termino(nuevo_coef * coef, exp + nuevo_exp)
        for exp, coef in temp.terminos.items():
            resto.agregar_termino(-coef, exp)

        # Limpiar coeficientes cercanos a cero
        resto.terminos = {exp: coef for exp, coef in resto.terminos.items() if abs(coef) > 1e-10}

    return cociente, resto

def ejecutar():
    print("✨ Bienvenido al ejercicio 4: La Matemática de los Encantamientos ✨")
    print("Has abierto un grimorio arcano con secretos algebraicos milenarios...")
    while True:
        continuar = input("Pulsa ENTER para desbloquear los misterios del polinomio mágico.\n")
        if continuar == "":
            break

    # Crear polinomios de ejemplo
    p1 = Polinomio()
    p1.agregar_termino(3, 2)
    p1.agregar_termino(5, 1)
    p1.agregar_termino(-2, 0)

    p2 = Polinomio()
    p2.agregar_termino(1, 1)
    p2.agregar_termino(1, 0)

    print("Polinomio 1:")
    p1.mostrar()
    print("\nPolinomio 2:")
    p2.mostrar()

    print("\n¿Deseas cambiar los polinomios?")
    opcion = input("Escribe '1' para introducirlos manualmente, '2' para generarlos aleatoriamente, o pulsa ENTER para continuar con los actuales: ")

    if opcion == "1":
        def crear_polinomio_desde_input(nombre):
            p = Polinomio()
            print(f"\nIntroduce los términos para el {nombre}:")
            while True:
                try:
                    coef = float(input("Coeficiente (o ENTER para terminar): ") or "")
                    exp = int(input("Exponente: "))
                    p.agregar_termino(coef, exp)
                except ValueError:
                    break
            return p

        p1 = crear_polinomio_desde_input("Polinomio 1")
        p2 = crear_polinomio_desde_input("Polinomio 2")

    elif opcion == "2":
        import random
        def generar_polinomio_aleatorio(nombre):
            p = Polinomio()
            print(f"\nGenerando {nombre} aleatorio:")
            for _ in range(random.randint(2, 5)):
                coef = random.randint(-5, 5)
                exp = random.randint(0, 4)
                p.agregar_termino(coef, exp)
            return p

        p1 = generar_polinomio_aleatorio("Polinomio 1")
        p2 = generar_polinomio_aleatorio("Polinomio 2")

    print("\nPolinomio 1:")
    p1.mostrar()
    print("\nPolinomio 2:")
    p2.mostrar()

    print("\nResta (p1 - p2):")
    resultado_resta = restar_polinomios(p1, p2)
    resultado_resta.mostrar()

    print("\nDivisión (p1 / p2):")
    cociente, resto = dividir_polinomios(p1, p2)
    print("Cociente:")
    cociente.mostrar()
    print("Resto:")
    resto.mostrar()

    print("\nEliminando término de grado 1 en p1:")
    eliminar_termino(p1, 1)
    p1.mostrar()

    print("\n¿Existe término de grado 2 en p1?")
    print("Sí" if existe_termino(p1, 2) else "No")
