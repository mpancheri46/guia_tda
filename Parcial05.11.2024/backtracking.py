def cuadrados_lagranje(n, camino, suma_actual, raiz_n_menos_suma_actual):

    #caso base

    if(n == suma_actual and len(camino) == 4):
        return camino

    if(len(camino) == 4 and suma_actual != n):
        return None

    #procesamiento

    for i in range(0, raiz_n_menos_suma_actual + 1):
        camino.append(i)
        suma_actual += i**2

        resultado = cuadrados_lagranje(n, camino, suma_actual, raiz_n_menos_suma_actual)

        if(resultado != None):
            return resultado

        camino.pop()
        suma_actual -= i**2

    return None

## complejidad O(n^2) porque se consideran raiz de n candidatos aprox y piden que sean 4 por numero osea que queda raiz de n elevado a la cuarta.

    