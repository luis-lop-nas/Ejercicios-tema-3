from polinomio import Polinomio
from operaciones import restar_polinomios, dividir_polinomios, eliminar_termino, existe_termino

def ejecutar():
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
