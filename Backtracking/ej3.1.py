
def numeros_dado(n, s, dado_actual, tirada, suma_actual, soluciones):

    if(dado_actual == n):
        if(suma_actual == s):
            soluciones.append(tirada.copy())
        return

    for valor in range(1,7):
        tirada.append(valor)

        numeros_dado(n, s, dado_actual + 1, tirada, suma_actual + valor, soluciones)
        tirada.pop()

    
    

