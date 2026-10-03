
def esta_ordenado(vector, inicio, fin):

    # caso base
    if(inicio == fin):
        return True

    medio = (inicio + fin) // 2

    izq_ord = esta_ordenado(vector, inicio, medio)
    der_ord = esta_ordenado(vector, medio + 1, fin)

    if (izq_ord and der_ord):
        if(vector[medio] <= vector[medio + 1]):
            return True

    return False

# complejidad = O(n)