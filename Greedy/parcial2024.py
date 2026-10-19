def mafias_ordenadas(mafias):

    mafias.sort(key=lambda mafia: mafia[1])
    seleccionadas = []
    ultimo_fin = float('-inf')

    for inicio, fin in mafias:
        if inicio > ultimo_fin:
            seleccionadas.append((inicio, fin))
            ultimo_fin = fin

    return seleccionadas