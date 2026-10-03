#ubicar n reinas
#tablero nxn de forma q ninguna pueda atacar a otroa. LAs reinas se atacan en fila, columna y diagonal

#que ejericio de mierdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

def n_reinas(n, fila_actual, tablero, soluciones):

    # CASO BASE
    if fila_actual == n:
        soluciones.append(tablero.copy())
        return

    # PROCESAMIENTO
    for columna in range(n):

        posicion_valida = True

        for fila_reina, columna_reina in tablero:

            # misma columna
            if columna == columna_reina:
                posicion_valida = False

            # misma diagonal
            if abs(fila_actual - fila_reina) == abs(columna - columna_reina):
                posicion_valida = False

    
        if posicion_valida:

            tablero.append((fila_actual, columna))

            # LLAMADO RECURSIVO
            n_reinas(n,fila_actual + 1,tablero,soluciones)

            # BACKTRACKING
            tablero.pop()