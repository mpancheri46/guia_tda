# Ejercicio 1 — Reducciones: Subset Sum → Mochila

**Tema:** NP-completitud  
**Dificultad:** Media

## Enunciado

Sabemos que **Subset Sum es NP-completo**.

### Subset Sum

Dado un conjunto de números enteros positivos y un objetivo `T`, determinar si existe un subconjunto cuya suma sea exactamente `T`.

### Mochila (versión de decisión)

Dados `n` objetos, cada uno con:

- Peso `p_i`.
- Beneficio `b_i`.

Y dos parámetros:

- Capacidad máxima `C`.
- Beneficio mínimo requerido `B`.

Determinar si existe un subconjunto de objetos `S` que cumpla simultáneamente:

**Restricción de peso:**

`Σ(i ∈ S) p_i ≤ C`

**Restricción de beneficio:**

`Σ(i ∈ S) b_i ≥ B`

## Consigna

Demostrar que **Mochila es NP-completo** utilizando Subset Sum.

La demostración debe incluir:

1. **Pertenencia a NP:** demostrar que una solución candidata de Mochila puede verificarse en tiempo polinomial.
2. **Dirección:** indicar qué reducción polinomial debemos construir.
3. **Construcción:** transformar una instancia de Subset Sum en una instancia de Mochila.
4. **Ida:** demostrar que si Subset Sum responde SÍ, Mochila también responde SÍ.
5. **Vuelta:** demostrar que si Mochila responde SÍ, Subset Sum también responde SÍ.
6. **Complejidad:** justificar que la transformación se realiza en tiempo polinomial.
7. **Conclusión:** justificar por qué Mochila es NP-completo.


Como tengo que demostrar que mochila es NP-completo sabiendo que Subset sum es np completo.

Me alcanza con demostrar que Subset sum es como maximo tan dificil como mochila. O que mochila como minimo va a ser tan dificil como subset sum.

Subset sum <= Mochila

En la mochila tenemos objetos con un peso y beneficios. REspetando que su sumatoria tiene que ser menor al peso maximo y mayor al beneficio minimo pedido.

 mientras que en subset sum tenemos un conjunto de números enteros positivos y un objetivo `T`, determinar si existe un subconjunto cuya suma sea exactamente `T`.

 para resolver subset sum con la mochila, podemos tomar a los productos seleccionados como el subconnjunto seleccionado y le asignamos al beneficio y al peso el mismo valor, que seria nuestro numero entero positivo del subconjuntos (nuestros). Una vez que seleccionamos eso, realizamos la sumatoria de los productos tomados y tenemos que como las dos condiciones de peso y de beneficio son iguales, entonces nuestra suma de productos tieene que ser igual em ambos casos, basicamente seria nuestra T del problema de subset sum.

 Como le asignamos el mismo valor al peso y al beneficio a los objetos de la mochila que nuestro numero entero positivo, si subset sum encuentra un subconjunto que sea exactamente T, entonces mochila tambien encontrara un subconjunto de objetos que cumpla simultaneamente con las condiciones del peso maximo y el beneficio minimo.

 si mochila me da justamente esa igualdad, entonces me confirma que existe un subconjunto que al sumarlo me de ese numero T buscado.

 La transformacion se realiza en tiempo polinomial ya que tenemos n objetos en la mochila, y los recorre entonces en el peor caso vamos a tener O(n).

 como subset sum es np completo, y pudimos demostrar la ida y la vuelta, podemos demostrar que el problrma de la mochila tambien es np completo.

 que subset sum sea np completo nos garantiza que la mochila va a ser np hard, pero no necesariamente np completo, por eso se debe verificar la solucion brindada por el problema y si es capaz de respondernos que SI para afirmar que es np completo.

 Mochila pertenece a NP porque, dado un subconjunto de objetos como solución candidata, podemos verificar en tiempo polinomial que la suma de sus pesos no supera la capacidad máxima C y que la suma de sus beneficios alcanza al menos B.