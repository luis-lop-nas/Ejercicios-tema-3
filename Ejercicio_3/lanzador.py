from nave import Nave
from gestor_naves import GestorNaves

def ejecutar():
    naves = [
        Nave("Cometa Veloz", 120, 5, 20),
        Nave("Titán del Cosmos", 300, 10, 50),
        Nave("GX-500", 150, 4, 8),
        Nave("GX-900", 180, 6, 12),
        Nave("Andrómeda", 95, 3, 4),
        Nave("Estrella Fénix", 220, 7, 30),
        Nave("Nebulosa Gris", 110, 4, 6),
        Nave("Cruzero Galáctico", 310, 15, 70),
        Nave("Viento Solar", 130, 5, 10),
        Nave("Orion", 200, 6, 15)
    ]

    respuesta = input("¿Quieres modificar la lista de naves? (si/no): ").strip().lower()
    if respuesta == "si":
        while True:
            accion = input("¿Qué quieres hacer? (añadir / borrar / modificar / salir): ").strip().lower()
            if accion == "salir":
                break

            if accion == "añadir":
                nombre = input("Nombre de la nueva nave: ")
                longitud = float(input("Longitud de la nave: "))
                tripulantes = int(input("Cantidad de tripulantes: "))
                pasajeros = int(input("Cantidad de pasajeros: "))
                naves.append(Nave(nombre, longitud, tripulantes, pasajeros))

            elif accion == "borrar":
                nombre = input("Nombre de la nave a borrar: ")
                naves = [n for n in naves if n.nombre != nombre]

            elif accion == "modificar":
                nombre = input("Nombre de la nave a modificar: ")
                for nave in naves:
                    if nave.nombre == nombre:
                        campo = input("¿Qué quieres modificar? (nombre / longitud / tripulantes / pasajeros): ").strip().lower()
                        if campo == "nombre":
                            nave.nombre = input("Nuevo nombre: ")
                        elif campo == "longitud":
                            nave.longitud = float(input("Nueva longitud: "))
                        elif campo == "tripulantes":
                            nave.tripulantes = int(input("Nuevo número de tripulantes: "))
                        elif campo == "pasajeros":
                            nave.pasajeros = int(input("Nuevo número de pasajeros: "))
                        break
                else:
                    print("Nave no encontrada.")

    print("=== Ordenadas por nombre (ascendente) ===")
    for nave in GestorNaves.ordenar_por_nombre(naves):
        nave.mostrar_info()

    print("=== Ordenadas por longitud (descendente) ===")
    for nave in GestorNaves.ordenar_por_longitud_desc(naves):
        nave.mostrar_info()

    print("=== Info de 'Cometa Veloz' y 'Titán del Cosmos' ===")
    for nave in GestorNaves.buscar_por_nombre(naves, ["Cometa Veloz", "Titán del Cosmos"]):
        nave.mostrar_info()

    print("=== Top 5 naves con más pasajeros ===")
    for nave in GestorNaves.top_pasajeros(naves):
        nave.mostrar_info()

    print("=== Nave con mayor cantidad de tripulantes ===")
    GestorNaves.nave_mayor_tripulacion(naves).mostrar_info()

    print("=== Naves cuyo nombre comienza con 'GX' ===")
    for nave in GestorNaves.nombres_empiezan_con(naves, "GX"):
        nave.mostrar_info()

    print("=== Naves con 6 o más pasajeros ===")
    for nave in GestorNaves.naves_con_pasajeros_minimos(naves, 6):
        nave.mostrar_info()

    print("=== Nave más pequeña ===")
    GestorNaves.nave_mas_pequena(naves).mostrar_info()

    print("=== Nave más grande ===")
    GestorNaves.nave_mas_grande(naves).mostrar_info()
