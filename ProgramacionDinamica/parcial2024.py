def llegar_a_k(k):

    dp = [0] * (k + 1)

    dp[0] = 0

    for i in range(1,k+1):
        if(i % 2 == 0):
            dp[i] = 1 + min(dp[i-1], dp[i//2])
        else: 
            dp[i] = 1 + dp[i-1]

    camino = []
    i = k

    while(i > 0):
        camino.append(i)
        if(i % 2 != 0):
            i-=1
        else:
            if(dp[i//2] < dp[i-1]):
                i = i//2
            else:
                i = i-1

    camino.append(0)
    camino.reverse()

    return dp[k], camino

