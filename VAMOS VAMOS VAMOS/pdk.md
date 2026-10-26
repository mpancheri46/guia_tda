Dado un número entero \(K\), se quiere obtener la mínima cantidad de operaciones para llegar desde 0 hasta K, utilizando solamente estas operaciones:
- Aumentar el valor actual en 1.
- Duplicar el valor actual.
Consigna: implementar un algoritmo de programación dinámica que obtenga la menor cantidad de operaciones necesarias y cuáles son esas operaciones.

Desarrollar la ecuación de recurrencia e indicar y justificar la complejidad del algoritmo.


*OBJETIVO:* ¿Qué quiero calcular u optimizar?

la menor cantidad de operaciones necesiarias desde 0 hasta K y cuales son esas operaciones

*ESTADO:* ¿Qué representa dp(...)?

dp(i) representa el caso optimo de operaciones para llegar a ese numero i

*CASO BASE:* ¿Cuándo ya conozco la respuesta?

 cuando la dp(0) vale 0 

*DECISIONES:* ¿Qué alternativas tengo?

en el numero parado actualmente tengo que decidir entre aumentar su valor en 1 o duplicar el valor de ese numero actual


*TRANSICIÓN:* ¿Cómo cambia el estado?

sumas 1 si venis desde i -1
duplicas si venis desde i/2

*RECURRENCIA:* ¿Cómo combino las alternativas con min, max u otra operación?

la recurrencia seria min cant de operaciones necesarias.

    si i % 2 == 0
        dp(i) = 1 + min(dp(i-1), dp(i/2))
    sino:
        dp(i) = 1 + dp(i-1)


def pd():

    dp = {}

    dp(0) = 0

    desde 1 hasta k + 1
        si i % 2 == 0
            dp(i) = 1 + min(dp(i-1), dp(i/2))
        sino:
            dp(i) = 1 + dp(i-1)
    
    lista_operaciones= []
    i = k

    while(i > 0):

    lista_operaciones.append(i)

    si i % 2 != 0
        i -= 1
    sino
        si la dp(i/2) < dp(i-1)
            i = i / 2
        sino
            i = i - 1
    
    lista_operaciones.append(0)
    lista_operaciones.reverse

    return dp[k], lista_operaciones

    





