def mover_piedras(n, origen, destino, auxiliar):
    if n == 1:
        destino.push(origen.pop())
    else:
        mover_piedras(n - 1, origen, auxiliar, destino)
        destino.push(origen.pop())
        mover_piedras(n - 1, auxiliar, destino, origen)