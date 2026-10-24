Marco, el cadete de la empresa, está en problemas. Le pidieron que compre un paquete de software para resolver el problema del Ciclo Hamiltoniano de manera eficiente.

Como siempre está distraído, compró uno que resuelve el problema del viajante (TSP).

El vendedor le dijo que si puede resolver TSP, también puede resolver fácilmente el Ciclo Hamiltoniano.

Determinar si el vendedor tiene razón o hay que echar a Marco.

1. Ciclo Hamiltoniano
Dado un grafo \(G=(V,E)\):

¿Existe un ciclo que visite todos los vértices exactamente una vez y regrese al vértice inicial?

Por ejemplo, si tenemos cuatro vértices A, B, C y D, un ciclo válido podría ser:

A → B → C → D → A

Siempre que todas esas aristas existan en el grafo original.

2. TSP — Problema del viajante
Dado un conjunto de ciudades, las distancias o costos entre ellas y un valor \(K\):

¿Existe un recorrido que visite todas las ciudades exactamente una vez, regrese al origen y tenga un costo total menor o igual a \(K\)?

A diferencia del Ciclo Hamiltoniano, acá nos importa también el costo total del recorrido.


ciclo hamiltoneano es como maximo tan dificil como TSP

Ciclo hamiltoneano <= TSP

TSP como MINIMO va a ser tan dificil como Ciclo Hamiltoneano

tengo que demostrar que con tsp se puede resolver el ciclo hamiltoneano.

La ciudades en este caso van a ser mis vertices mientras que las aristas van a ser las rutas del recorrido que conectan a los vertices para realizar el viaje para pasar por las ciudades exactamente una vez y regresar al origen. Nuestro costo K del tsp tiene que ser = a la cantidad de vertices que tengamos en el ciclo hamiltoneano.

entonces hasta ahora con TSP para ciclo hamiltoneano tenemos:

Ciudades = vertices
Rutas = aristas
K = cantidad de vertices 

Le asignamos costo 1 a las aristas oroginales del hamiltoneano, y 2 a las agregadas del tsp. SI TSP responde con SI con k = v entonces no voy usar las aristas agregadas del costo 2 ya que el ciclo existe en elgrafo original.

Si existe ciclo hamiltoneano, usa v aritas y cuesta v, por lo tanto TSP tambien va a responder que si.

El vendedor tiene razon.

O(V^2)

