

def recorrer_estadios(distancias, obelisco):
    distancia_acumulada = 0
    visitados = [False] * len(distancias)
    visitados[obelisco] = True
    posicion_colectivo = obelisco

    i = 0

    while i < len(distancias) - 1:
        menor_distancia = float('inf')
        estadio_mas_cercano = -1

        for estadio in range(len(distancias)):
            if visitados[estadio] == False:
                if distancias[posicion_colectivo][estadio] < menor_distancia:
                    estadio_mas_cercano = estadio
                    menor_distancia = distancias[posicion_colectivo][estadio]

        distancia_acumulada += menor_distancia
        visitados[estadio_mas_cercano] = True
        posicion_colectivo = estadio_mas_cercano

        i += 1

    distancia_acumulada += distancias[posicion_colectivo][obelisco]

    return distancia_acumulada