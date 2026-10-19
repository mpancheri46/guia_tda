def menor_costo(rutas, orden, origen, destino):
    
    dp = {}

    for ciudad in orden:
        dp[ciudad] = float('inf')

    dp[origen] = 0

    for ciudad in orden:
        for vecino, costo in rutas[ciudad]:
            dp[vecino] = min(dp[vecino], dp[ciudad] + costo)

    return dp[destino]