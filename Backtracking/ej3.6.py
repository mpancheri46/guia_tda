##coloreo de grafos, que no se repita el color en los nodos adyacentes

def coloreo_grafo(grafo, color_por_vertice, cantidad_colores, vertice_actual, cant_vertices):

    if vertice_actual == cant_vertices:
        return True

    adyacentes = grafo[vertice_actual]

    for color_candidato in range(cantidad_colores):

        valido = True

        for vecino in adyacentes:
            if color_por_vertice[vecino] == color_candidato:
                valido = False

        if valido:
            color_por_vertice[vertice_actual] = color_candidato
    
            if coloreo_grafo(grafo, color_por_vertice, cantidad_colores, vertice_actual + 1, cant_vertices):
                return True
            
            color_por_vertice[vertice_actual] = -1

    return False
    
    

