
def londres_california(l, c, m):

    n = len(l)

    dp_londres = [0] * n
    dp_california = [0] * n

    dp_londres[0] = l[0]
    dp_california[0] = c[0]

    for i in range(1, n):

        dp_londres[i] = min(dp_londres[i-1] + l[i], dp_california[i-1] + m + l[i])

        dp_california[i] = min(dp_california[i-1] + c[i], dp_londres[i-1] + m + c[i])

        
    dp = min(dp_california[n-1], dp_londres[n-1])

##esta parte de la restructuracion me cuesta una banda, por ahora necesito chat para entender como sacarlo

    