
def teclado(n,k):

    vecinos = [[8],[2, 4],[1, 3, 5],[2, 6],[1, 5, 7],[2, 4, 6, 8],[3, 5, 9],[4, 8],[0, 5, 7, 9],[6, 8]]

    dp = [[0] * 10 for i in range(n + 1)]

    for tecla in range(10):
        dp[1][tecla] = 1

    for longitud in range(2, n + 1):
        for tecla in range(10):
            for vecino in vecinos[tecla]:
                dp[longitud][tecla] += dp[longitud -1][vecino]

    return dp[n][k]


