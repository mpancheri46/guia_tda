Permisos para controlar tramos de ruta
El mafioso Arnook recibe pedidos de distintas mafias para controlar determinados tramos de una ruta costera.

Cada mafia solicita un intervalo de kilómetros. Por ejemplo:
- Mafia 1: km 1 al 5.
- Mafia 2: km 3 al 8.
Restricción: no se pueden otorgar permisos a dos mafias cuyos tramos se superpongan.

Arnook cobra lo mismo por cada permiso, independientemente de la longitud del tramo.

Objetivo: maximizar la cantidad de permisos otorgados.

Consigna del parcial
1. Implementar un algoritmo Greedy que determine a qué mafias otorgar permisos.
2. Indicar y justificar su complejidad.
3. Justificar por qué el algoritmo es Greedy.
4. Determinar si siempre encuentra la solución óptima y justificar.

1. GREEDY*

*OBJETIVO:* ¿Qué quiero maximizar o minimizar? maximizar la cantidad de permisos otorgados para las mafias

*CRITERIO:* ¿Cuál es la mejor decisión local?

la mejor decision local va a ser elegir la que empiece mas cerca de la que termine actualmente

*VALIDACIÓN:* ¿La decisión respeta las restricciones?

la proxima banda tiene que al menos empezar donde termine la actual

*ACTUALIZACIÓN:* ¿Qué cambia después de elegir?

cambia nuestro fin actual y pasamos a otra banda

*REPETICIÓN:* ¿Cuándo termino?

terminas cuando te quedas sin posibilidad de asignar bandas

*OPTIMALIDAD:* ¿Garantiza el óptimo? Justificar o dar un contraejemplo.

no garantiza el optimo ya que podrian haber entrado mas bandas que requieran menos km y  asi dar muchos permisos

*COMPLEJIDAD:* Contar recorridos y ordenamientos.

def mafias(bandas_mafiosas):

    ruta_costera = []
    fin_anterior 

    for inicio,fin in banda_mafiosas
        if(inicio > fin_anterior):
            ruta_costera.append(inicio,fin)
            fin_anterior = fin
    
    return ruta_costera


version optima:

def mafias(bandas_mafiosas):

    ordenar las bandas_mafiosas segun su fin de km (tipo scheduler)
    ruta_costera = []
    fin_anterior 

    for inicio,fin in banda_mafiosas
        if(inicio > fin_anterior):
            ruta_costera.append(inicio,fin)
            fin_anterior = fin
    
    return ruta_costera

ahi si seria optimo porque agrega todas las posibles en el rango de la ruta costera

O(nlogn)








