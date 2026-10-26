Seleccionar charlas con puntaje
Se organiza un evento con \(n\) charlas. Cada charla \(i\) tiene:
- Una hora de inicio \(s_i\).
- Una hora de finalización \(f_i\).
- Un puntaje \(p_i\) que representa su valor.
Una persona puede asistir a varias charlas, pero no puede asistir a dos que se superpongan.

El objetivo es maximizar la suma de los puntajes de las charlas seleccionadas.

Consigna de práctica
1. Proponer un algoritmo Greedy para seleccionar las charlas.
2. Explicar cuál es su criterio de selección.
3. Indicar y justificar su complejidad.
4. Determinar si siempre obtiene la solución óptima. Si no, dar un contraejemplo.



el objetivo es maximizar la cantidad de puntos de las charlas elegidas, por lo tanto la idea es elegir dentro de las charlas posibles, osea las que inicien posterior al horario de finalizacion de una actual, la que mayor puntaje permita sumar en ese momento.
claramente no seria optimo ya que podria haber charlas mas cortas y que den menos puntos indivdualmente pero que sumandolas den mas puntos que una charla larga que de muchos puntos pero acapare muchas horas disponibles


func greedy(charlas):

    ordeno las charlas de mayor a menor puntaje
    puntaje_acumulado = 0
    charlas_elegidas[]

    recorro inicio,fin,puntaje in charlas:
        superposicion = falso
        recorro inicio_e,fin_elegida,puntaje_elegida in charlas_elegidas:
            si (inicio <= fin_elegida y fin >= inicio_elegida):
                superposicion = verdadero
        si (no hay superposicion):
            puntaje_acumulado += puntaje
            charlas_elegidas.append(inicio,fin,puntaje)

    return puntaje_acumulado

O(n^2) -> ordenar es O(n log n), pero cada charla se compara contra todas las elegidas, y en el peor caso eso es n por n.