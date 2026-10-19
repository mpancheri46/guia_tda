

n reinas (filas, col, tablero, n, soluciones)

    SI estoy en n
    soluciones = tablero

    recorro el tablero para la columna reina

    si mi fila actual es igual a la fila de la reina 
        devuelvo false (poda)

    si mi col actual es igual a la col de la reina 
        devuelvo false (poda)

    si misma_diagonal
        devuelvo false (poda)

    si es posicion valida = true

        agrego al tablero la reina en la fila actual y mi columna 

        vuelvo a llamar a la funcion con fila actual + 1

        si no entro a la funcion. lo borro haciendo un 
        pop del tablero

