Demostrar que Set Cover es NP-completo, utilizando una reducción desde un problema que ya sabemos que es NP-completo

utilizaria una reduccion desde Vertex Cover 

Vertex Cover → Set Cover: universo = aristas del grafo; cada vértice corresponde al conjunto de aristas incidentes. Elegir vértices que cubren todas las aristas equivale a elegir conjuntos cuya unión cubre ese universo.

osea deberiamos demostrar que vertex cover es como maximo tan dificil como set cover

Vertex cover: Existe un conjunto de como máximo \(k\) vértices que cubra todas las aristas del grafo

Set cover: Podemos elegir como máximo \(k\) subconjuntos cuya unión cubra todo el universo


entonces la reduccion que podriamos ahcer es tratar a los vertices de vertex cover como los subconjuntos de set cover y el maximo k seria el mismo para ambos. mientras que vertex cover me pide un maximo K vertices, set cover me pide maximo K subconjuntos. Esos subconjuntos ahora son nuestros vertices de vertex cover que tenemos que maximizar.

Como vertex cover es NP completo ya que todos sus problemas con como maximo tan dificiles como set cover y podemos verificar una solucion candidata en tiempo polinomial

Entonces podemos demostrar que set cover es NP completo ya que si vertex cover tiene soluciones y son verificables, entonces set cover tambien las tiene ya que VC es como maximo tan dificil como lo es Set cover.