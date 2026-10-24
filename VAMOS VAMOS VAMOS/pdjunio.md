El INVAP debe transportar una carga extremadamente peligrosa desde Ezeiza hasta Bariloche.

El traslado se hará por tierra y en etapas, ya que no se pueden hacer más de 400 km por día y no se puede viajar de noche.

Se conocen las diferentes alternativas de rutas y lugares donde parar. También se conoce el costo del seguro para cada camino posible.

Por ejemplo, para la primera etapa hay tres caminos posibles:
- Ezeiza → General Villegas: $57.
- Ezeiza → Bolívar: $82.
- Ezeiza → Azul: $39.
Los costos de seguro tienen en cuenta los riesgos de las distintas rutas.

Consigna: Realizar un algoritmo mediante programación dinámica que resuelva el problema calculando el menor costo de seguro. Indicar el orden de complejidad del algoritmo.



las soluciones para este trabajo son similares al de la mochila: tomar o no tomar ese camino para llegar a bariloche. en este caso deberiamos buscar el minimo del costo entre las opciones disponibles hasta llegar a bariloche


def menor_costo(rutas, origen, destino, ciudades):

    dp = {}

    
    for ciudad in ciudades:
        dp[ciudad] = numeros infinitos

    dp[origen] = 0

    hubo_cambios = True

    while hubo_cambios:

        hubo_cambios = False

        for ciudad_actual in ciudades:

            for ciudad_destino, costo in rutas[ciudad_actual]:

                nuevo_costo = dp[ciudad_actual] + costo

                if nuevo_costo < dp[ciudad_destino]:

                    dp[ciudad_destino] = nuevo_costo
                    hubo_cambios = True

    return dp[destino]


La complejidad de es de O(V)