La mochila de Paolo Casanova
Paolo se va de viaje y tiene una mochila con dos limitaciones:
- Capacidad máxima de L litros.
- Peso máximo de C kilogramos.
Tiene una lista de \(n\) objetos. Para cada objeto \(i\), conoce:
- Su peso \(p_i\).
- Su volumen \(v_i\).
- Su beneficio \(b_i\).
Los objetos 1 y 2 son dos guías de observación de aves.

Debe llevar exactamente una de las dos guías, nunca ambas.

Su objetivo es maximizar el beneficio total de los objetos transportados.

Consigna original

Desarrollar un algoritmo de programación dinámica que encuentre la solución óptima.

*OBJETIVO:* ¿Qué quiero calcular u optimizar?

quiero maximizar el beneficio total de los objetos transportados


*ESTADO:* ¿Qué representa dp(...)?

dp() representa el beneficio actual de la mochila con los productos seleccionados hasta el momento

*CASO BASE:* ¿Cuándo ya conozco la respuesta?

cuando la dp(0) = 0

*DECISIONES:* ¿Qué alternativas tengo?

llevar o no el objeto en la mochila

*TRANSICIÓN:* ¿Cómo cambia el estado?

el estado cambia tomando o no el objeto

*RECURRENCIA:* ¿Cómo combino las alternativas con min, max u otra operación?

deberias hacer el max(no tomarlo, tomar el elemento + beneficio)

*IMPLEMENTACIÓN:* ¿En qué orden calculo los estados?

*COMPLEJIDAD:* Cantidad de estados × trabajo por estado.


Mochila(peso, volumen, beneficio, n, PESO_MAX, VOL_MAX):

    dp[c][l] = 0

    para i = 3 hasta n:
        para c = PESO_MAX hasta peso[i]:
            para l = VOL_MAX hasta volumen[i]:
                dp[c][l] = max(dp[c][l], beneficio[i] + dp[c - peso[i]][l - volumen[i]])

    mejor_beneficio = -infitnito

    para las guias pos 1 y 2:
        si peso[guia] <= PESO_MAX y volumen[guia] <= VOL_MAX:
            mejor_beneficio = max(mejor_beneficio, beneficio[guia] + dp[PESO_MAX - peso[guia]][VOL_MAX - volumen[guia]])

    devolver mejor_beneficio