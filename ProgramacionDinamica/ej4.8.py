
def monedas(monedas, monto):

    dp = [float("inf")] * (monto + 1)
    
    dp[0] = 0

    for m in range(1, monto + 1):
        for moneda in monedas:
            if moneda <= m:
                dp[m] = min(dp[m], dp[m - moneda] + 1)
    
    return dp[monto]

    