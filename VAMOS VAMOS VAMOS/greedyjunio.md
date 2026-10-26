El INVAP debe transportar una carga extremadamente peligrosa desde Ezeiza hasta Bariloche.

El traslado se hará por tierra y en etapas, ya que no se pueden hacer más de 400 km por día y no se puede viajar de noche.

Se conocen las diferentes alternativas de rutas y lugares donde parar. También se conoce el costo del seguro para cada camino posible.

Por ejemplo, para la primera etapa hay tres caminos posibles:
- Ezeiza → General Villegas: $57.
- Ezeiza → Bolívar: $82.
- Ezeiza → Azul: $39.
Los costos de seguro tienen en cuenta los riesgos de las distintas rutas.

Consigna: Realizar un algoritmo mediante programación dinámica que resuelva el problema calculando el menor costo de seguro. Indicar el orden de complejidad del algoritmo

AHORA CON GREEDY


func menor_costo(rutas, origen, destino):

    costo_acumulado = 0
    ciudad_actual = origen
    ciudades_visitadas = vacío

    mientras ciudad_actual != destino:

        mejor_costo = infinito
        proxima_ciudad = ninguna

        recorro las rutas posibles desde ciudad_actual:
            si la ciudad no fue visitada:
                si costo_ruta < mejor_costo:
                    mejor_costo = costo_ruta
                    proxima_ciudad = ciudad

        costo_acumulado += mejor_costo
        agregar ciudad_actual a ciudades_visitadas
        ciudad_actual = proxima_ciudad

    devolver costo_acumulado

no garantiza el optimo ya que al tomar la mejor decision local descarta muchas alternativas que podrian ser mas economicas. esto se puede ver con un ejemplo

- Ezeiza → General Villegas: $57.
- Ezeiza → Bolívar: $82.
- Ezeiza → Azul: $39.

Ahi elegiria azul
pero quizas de azul solo hay una ruta que vale 1000
mientras que las otras opciones tenias otras rutas mucho mas economicas que nunca alcanzaban ese costo.
Por eso mismo el algoritmo no garantiza una solucion optima.
