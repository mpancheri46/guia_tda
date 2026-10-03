##encontrar un camino en un grafo que visite todos los vertices exactamente una vez

def camino_hamiltoneano(grafo, camino, vertice_actual, cantidad_vertices):

    if(len(camino) == cantidad_vertices):
        return True


    for vecino in grafo[vertice_actual]:
        
        if vecino not in camino:
            camino.append(vecino)
            
            if(camino_hamiltoneano(grafo, camino, vecino, cantidad_vertices)):
                return True

            camino.pop()

    return False

        