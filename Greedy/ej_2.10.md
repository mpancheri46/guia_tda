Algoritmo puestos_minimos(puertas, d):

    ordenar puertas de menor a mayor

    puestos = []
    i = 0

    mientras i < cantidad_de_puertas:

        primera_no_cubierta = puertas[i]

        mientras i < cantidad_de_puertas && puertas[i] - primera_no_cubierta <= d:
            i = i + 1

        puesto = puertas[i - 1]
        agregar puesto a puestos

        mientras i < cantidad_de_puertas && puertas[i] - puesto <= d:
            i = i + 1

    devolver puestos

    la complejidad es de nlogn