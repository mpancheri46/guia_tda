Se está estudiando la posibilidad de implementar un bus turístico temático que recorra todos los estadios de fútbol de la ciudad de Buenos Aires (Defensores de Belgrano, River Plate, Excursionistas, Atlanta, Comunicaciones, Argentinos Juniors, Lamadrid, All Boys, Ferrocarril Oeste, Vélez Sarsfield, Huracán, Barracas Central, San Lorenzo, Riestra, Deportivo Español, Nueva Chicago y Sacachispas).

El ómnibus partirá del Obelisco, recorrerá todos los estadios y volverá al Obelisco.

Se conocen las distancias entre cada par de estadios y entre cada estadio y el Obelisco.

Considerando que se desea poder realizar varias vueltas en el día con un único autobús, se pide desarrollar un algoritmo que determine un orden de visitas a los estadios que insuma el menor tiempo posible.

Indicar la complejidad del algoritmo generado y si el resultado obtenido es óptimo o no.

como es un algoritmo greedy se tiene que tomar la mejor decision local posible, lo importante es determinar si es optimo o no en base a la decision local que tenemos. como tenemos la distancia entre cada par de estadios, lo importante es tomar la decision en base al estadio que tengamos mas cerca para poder determinar a donde ir sin que lo hayamos visitado ya previamente.

en pseudocodigo

funcion recorrido(origen)

    lista_estadios[]
    estadios_recorridos
    posicion colectivo = origen

    mientras que haya estadios
        mejor_distancia
        for estadios in lista estadios
            si el estadio actual no fue visitado
                si la distancia_actual < mejor distancia
                    estadio actual es el proximo a visitar
                    
        agregar el estadio actual a recorridos
        distancia acumulada += distancia_actual
        estadio actual = visitado
        posicion colectivo = estadio actual
    
    distancia acumulada += distancia al obeliso 

    devolver distancia acumulada 

Determino que este algoritmo no es optimo ya que al tomar decisiones locales por cada estadio, no me asegura que sea la mejor solucion ya que podria quedar muy lejos del obelisco a la hora de tener que regresar y sumar kilometros innecesariamente.

la complejidad del algoritmo es O(n^2)

