

def encontrar_cero (vector, inicio, fin):

    #caso base
    if(inicio == fin):
        if(vector[inicio] == 0):
            return inicio
        return -1

    medio = (inicio + fin) // 2

    if(vector[medio] == 0):
        return encontrar_cero(vector, inicio, medio)
    else:
        return encontrar_cero(vector, medio + 1, fin)