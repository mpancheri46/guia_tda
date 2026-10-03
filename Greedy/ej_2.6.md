Algoritmo organizar_charlas(charlas):

    ordenar charlas por hora de finalización creciente

    seleccionadas = []
    fin_ultima = -infinito

    para cada charla en charlas:
        si inicio(charla) >= fin_ultima:
            agregar charla a seleccionadas
            fin_ultima = fin(charla)

    devolver seleccionadas

    complejidad nlogn porque ordena logn y hace un recorrido lineal n

    