
**Objetivo:** determinar cuánta energía transportar entre las 9 regiones para satisfacer todas las demandas mediante Ford-Fulkerson.

### 1. Construcción del grafo

Creamos un grafo dirigido con 9 vértices, uno por región, una fuente S y un sumidero T.

Agregamos las siguientes aristas:

- **S -> i:** capacidad Gi, que representa la energía generada por la región.
- **i -> T:** capacidad Di, que representa su demanda.
- **i -> j:** capacidad CAPij, que representa el máximo de energía que puede enviarse entre regiones.

Las regiones están conectadas entre sí mediante aristas dirigidas.

### 2. Aplicación de Ford-Fulkerson

1. Inicializamos todos los flujos en cero.
2. Buscamos un camino aumentante desde S hasta T en la red residual.
3. Calculamos el cuello de botella, que es la menor capacidad residual del camino.
4. Aumentamos el flujo del camino en esa cantidad.
5. Actualizamos las capacidades residuales, incluyendo las aristas inversas.
6. Repetimos hasta que no existan más caminos aumentantes.

Cuando el algoritmo termina, obtenemos el flujo máximo.

### 3. Verificación de las demandas

Sumamos las demandas de todas las regiones.

- Si el flujo máximo es igual a la demanda total, podemos satisfacer todas las regiones.
- Si el flujo máximo es menor, no existe una distribución que permita cubrir todas las demandas.

### 4. Obtener la solución

Una vez finalizado el algoritmo, consultamos el flujo de cada arista entre regiones.

El flujo de la arista i → j indica cuántos MWh debemos transportar desde la región i hacia la región j.



