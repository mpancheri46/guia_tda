
def soga(n):

    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n+1):
        for j in range(1, i):

            ##chequea si despues del primer corte conviene seguir cortando o ahi esta  bien
            producto = max(j * (i-j), j * dp[i-j])
            ##compara el producto maximo
            dp[i] = max(dp[i], producto)

    return dp[n]