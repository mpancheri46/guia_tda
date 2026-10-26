Demostrar que Set Cover es NP-completo
Sabemos que Vertex Cover es NP-completo.

Vertex Cover: dado un grafo no dirigido \(G=(V,E)\) y un entero \(k\), determinar si existe un conjunto de como máximo \(k\) vértices que cubra todas las aristas.

Set Cover: dado un universo \(U\), una familia de subconjuntos \(S_1,S_2,\ldots,S_n\) de \(U\) y un entero \(k\), determinar si podemos elegir como máximo \(k\) subconjuntos cuya unión cubra todo \(U\).

Consigna

Demostrar que Set Cover es NP-completo utilizando Vertex Cover.

Tu demostración debe incluir:
1. Pertenencia de Set Cover a NP.
2. Dirección de la reducción.
3. Construcción de la instancia de Set Cover.
4. Demostración de ida y vuelta.
5. Complejidad de la transformación.
6. Conclusión.


como me piden demostrar que set cover en  NP completo

tengo que demostrar que vertex cover como maximo es tan dificil como set cover, o que set cover es como minimo tan dificil como vertex cover.

en set cover, mi universo U serian todas las aristas de vertex cover. La familia de subconjuntos cuya union cubra todo el U serian mis vertices seleccionados para cubrir todas las aristas, osea por cada vertice se crea un subconjunto y ester subconjunto contiene todas las aristas que tienen al vertice Vi como uno de sus extremos. Y el entero K que seria el maximo de subconjuntos, representaria el maximo K vertices en vertex cover.

Una vez que se demostró que se puede resolver una instancia de set covver con vertex cover. 

Podemos demostrar que si tenemos 5 subconjuntos y la union cubre todo U, podemos afirmar que 5 vertices cubren todas las aristas, utilizando 5 como nuestro K de ambos problemas.

lo mismo hacia el otro lado, si tengo 5 vertices que cubren todas las aristas, puedo resolver 5 subconjuntos que cubran todo el U.

como vertex cover es np completo, de primeras por resolver una instancia del problema con set cover, puedo decir que este ultimo es np hard. para demostrar que es np completo, solo faltaria chequear que sea np.

se puede chequear verificando una posible solucion en la que uniendo los k subconjuntos obtenidos podamos cubrir todo el universo U.

con esta veritifacion, podemos demostrar que set cover es np-completo.


la complejidad seria de O(v+e)