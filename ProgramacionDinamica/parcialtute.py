def costo(i, j, CF, CV, S, D):

    total = CF[i]

    for mes in range(i, j + 1):
        total += CV[i] * D[mes]

        for k in range(i, mes):
            total += S[k] * D[mes]

    return total

def producir_meses(n):

    dp = [float('inf')] * (n + 2)

    dp[n + 1] = 0
    
    for i in range(n,0,-1):
        for j in range(i, n+1):
            costo_actual = costo(i,j)
            dp[i] = min(dp[i], costo_actual + dp[j+1])

    return dp[1]
