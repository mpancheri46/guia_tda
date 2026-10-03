#L LISTA DE POSITIVOS ENTEROS [1,2,3,4]
#un entero n
# encontrar un subconjunto de esa lista que al sumarlo te de n
#si no existe, devolver la mas cercana sin pasarse

def suma_n (L, n, camino, suma_actual, pos_actual, mejor_suma, mejor_camino):

    if(suma_actual > n):
        return mejor_suma, mejor_camino

    if(suma_actual > mejor_suma):
        mejor_suma = suma_actual
        mejor_camino = camino.copy()


    if pos_actual == len(L):
        return mejor_suma, mejor_camino

    camino.append(L[pos_actual])
    suma_actual += L[pos_actual]

    mejor_suma, mejor_camino = suma_n(L, n, camino, suma_actual, pos_actual + 1, mejor_suma, mejor_camino)

    camino.pop()
    suma_actual -= L[pos_actual]

    mejor_suma, mejor_camino = suma_n(L, n, camino, suma_actual, pos_actual + 1, mejor_suma, mejor_camino)

    return mejor_suma, mejor_camino
    
    