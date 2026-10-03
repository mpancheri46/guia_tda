#Se cuenta con un arreglo de enteros ordenado de manera ascendente, que contiene
#exactamente un número duplicado (es decir, todos los demás elementos son distintos, sin
#duplicados). Implementar una función que encuentre dicho número utilizando división y
#conquista. Indicar y justificar la complejidad del algoritmo, utilizando el Teorema Maestro.

# vector = [1,2,3,3,4,5,6]

def num_duplicado(vector, inicio, fin):

    ##caso base
    if(inicio == fin):
        return 0

    medio = (inicio + fin) // 2

    if(vector[medio] == vector[medio + 1]):
        return vector[medio]

    izq = num_duplicado(vector, inicio, medio)
    der = num_duplicado(vector, medio + 1, fin)

# complejidad O(n)    




    