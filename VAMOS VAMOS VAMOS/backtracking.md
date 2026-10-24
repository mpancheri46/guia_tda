Realizar un algoritmo que resuelva el problema de las 8 reinas mediante backtracking.

Recordemos que el problema consiste en ubicar 8 reinas en un tablero de ajedrez de manera que no haya dos reinas en la misma fila, columna o diagonal.

Indicar las estructuras de datos utilizadas para representar el problema y la solución.

n_reinas(filas, col, tablero, n, soluciones)

    si estoy en n:
        soluciones = tablero
    
    recorro el tablero para la columna reina:
        
        si mi fila actual es igual a la fila
            devuelvo false (poda)
        
        si mi col actual igual a la columna reina:
            devuelvo false (poda)

        si misma_diagonal (con abs)
            devuelvo false (poda)
    
        si posicion_valida = true

            agrego al tablero la reina en la fila actual con la columna reina

            n_reinas(fila + 1, col, tablero, n, soluciones)

            tablero.pop