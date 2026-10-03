

def posicion_pico(vector, inicio, fin):

    # caso base
    if(inicio == fin):
        return inicio

    medio = (inicio + fin) // 2

    if(vector[medio] > vector[medio - 1] and vector[medio] < vector[medio + 1]):
        return posicion_pico(vector, medio + 1, fin)
    elif(vector[medio] < vector[medio - 1] and vector[medio] > vector[medio + 1]):
        return posicion_pico(vector, inicio, medio)
    else:
        return medio

    