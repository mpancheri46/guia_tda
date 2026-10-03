
def juan_vago(ganancias):

    dp = [0] * len(ganancias)

    dp[0] = ganancias[0]
    dp[1] = max(ganancias[0], ganancias[1])

    for i in range (2, len(ganancias)):
        dp[i] = max(dp[i-1], dp[i-2] + ganancias[i])

    dias_trabajados = []

    i= len(ganancias) - 1

    while i >= 0:

        if i == 0:
            dias_trabajados.append(0)
            break

        if dp[i] == dp[i - 1]:
            # no trabajo el dia i
            i -= 1

        else:
            # trabajo el dia i
            dias_trabajados.append(i)
            i -= 2

    dias_trabajados.reverse()