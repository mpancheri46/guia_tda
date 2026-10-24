GREEDY. Plantear un algoritmo Greedy que resuelva el problema anterior.

Problema: distribución de energía
El sistema energético argentino está dividido en 9 regiones.

Para cada región conocemos:
- La cantidad de energía que genera (\(G_i\)).
- La demanda de energía que necesita cubrir (\(D_i\)).
- La capacidad máxima de transporte entre cada par de regiones (\(CAP_{ij}\)).
- El costo de transportar energía entre regiones (\(C_{ij}\)).
Consigna: desarrollar un algoritmo Greedy que distribuya la energía entre las regiones para intentar cubrir sus demandas.


func greedy(regiones, generacion, demanda):

    for i in red:
        si regiones[i].generacion >= demanda:
            cubre su demanda
            excedente_enviar = regiones[i].generacion - regiones[i].demanda
            if(excdente_enviar <= cap maxima entre regiones):
                demanda_vecino = regiones[i+1].demanda
                excdente_enviar = demanda_vecino
                excedente_enviar a mayor demanda



pseudocodigo de chat:

    func greedy(regiones, generacion, demanda, CAP):

    para cada region i:
        demanda_pendiente[i] = max(0, demanda[i] - generacion[i])
        excedente[i] = max(0, generacion[i] - demanda[i])

    para cada region i:

        mientras excedente[i] > 0:

            buscar la region j con mayor demanda_pendiente
            entre las que tengan capacidad disponible desde i

            si no existe una region j:
                terminar este mientras

            energia_enviar = min(
                excedente[i],
                demanda_pendiente[j],
                CAP_disponible[i][j]
            )

            enviar energia_enviar de i a j

            excedente[i] -= energia_enviar
            demanda_pendiente[j] -= energia_enviar
            CAP_disponible[i][j] -= energia_enviar

    si todas las demandas_pendientes son 0:
        devolver distribucion de energia

    devolver "No se pudieron cubrir todas las demandas"