
Un conjunto dominante (Dominating Set) de un grafo no dirigido \(G=(V,E)\) es un subconjunto \(D\) de vértices tal que cada vértice del grafo:
- Pertenece a \(D\), o
- Es adyacente a algún vértice de \(D\).
Dado un grafo \(G\) y un número \(k\), queremos determinar si existe un conjunto dominante de tamaño como máximo \(k\).

Vertex cover: Existe un conjunto de como máximo \(k\) vértices que cubra todas las aristas del grafo

Consigna original: demostrar que Dominating Set es NP-completo.

El parcial recomienda utilizar Vertex Cover como problema de partida.

Lo que tenés que demostrar:
1. Dominating Set pertenece a NP.
2. Vertex Cover \(\le_p\) Dominating Set.
3. La transformación es polinomial.
4. La equivalencia se cumple en ambos sentidos.


*OBJETIVO:* ¿Qué dificultad quiero demostrar?

    que dominating set es np completo. y que 
    vertex cover es como maximo tan dificil como dominating set. o que dominatig set es como minimo tan dificil como vertex cover


*DIRECCIÓN:* Si quiero demostrar que B es NP-hard, reducir un problema A ya NP-completo hacia B:

quiero demostrar que Dominating set es NP-completo, osea que tengo que reducir vertex cover hacia dominating set

A ≤p B

*CONSTRUCCIÓN:* ¿Cómo transformo una instancia de A en una de B?

dominating: subconjunto de vertices tal que cada vertice pertenece a ese subconjunto o es adyacente a algun vertice de ese subconjunto

podriamos resolver vertex cover utilizando el subconjunto D de vertices como nuestro conjunto de vertices de vertex cover. EL Tamaño maximo K de nuestro subconjunto en dominating set seria el maximo de K vertices que cubra todas las aristas del grafo.

si tengo un dominating set de tamaño maximo k, cualquier vertice se reemplaza Xuv seleccionado por uno de los dos extremos originales sin aumentar el tamaño del conjunto y asi se puede obtener un conjunto vertex cover.


*COMPLEJIDAD:* ¿La transformación es polinomial?

la transofrmacion es polinomial porqe seria reconstruir el grafo a partir del subconjunto que nos da dominating set

*PERTENENCIA A NP:* ¿Puedo verificar una solución candidata de B en tiempo polinomial?

es np poorque podes verificar una solucion sumando la cantidad de vertices y que te de el resultado K

*CONCLUSIÓN:* Si B pertenece a NP y es NP-hard, entonces es NP-completo.

Como puedo demostrar que es np, entonces puedo afirmar que dominating set es NP completo ya que una instancia de vertex cover soluciona 

*REGLA:* Una reducción, demostrada en los dos sentidos.