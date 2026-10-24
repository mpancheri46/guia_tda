Tenemos el problema del delivery. Es similar al problema de la mochila, pero además del peso \(W_i\) de cada elemento, debemos considerar su volumen \(V_i\) y su costo \(C_i\).

La mochila tiene una capacidad máxima de \(C\) kilos y \(T\) litros.

Además, por una restricción del seguro, el costo total de los productos transportados no puede superar los \(M\) pesos.

Desarrollar un algoritmo de programación dinámica que resuelva el problema.

delivery(N,W,V,C,cap_mochila,T,M):

   dp[0][w][v][m] = 0

    para i = 1 hasta n productos
      para w de cada producto:
        para v de cada producto:
          para m hasta el valor maximo:
            si W[i] <= w y V[i] <= v y C[i] <= m:
                dp[i][w][v][m] = max( dp[i-1][w][v][m], 1 + dp[i-1][w-W[i]][v-V[i]][m-C[i]] )  

    devolver dp[N][cap_mochila][T][M]