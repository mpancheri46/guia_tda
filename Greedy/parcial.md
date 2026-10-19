


greedy (destino):

    precio_guardado = inf
    ciudad_actual = ezeiza


    MIENTRAS QUE la ciudad actual sea distinta del destino:
        precio_guardado = infinito
        para las rutas posibles en rutas desde la ciudad actual
            si (precio_actual en la ruta posible es menor al precio guardado y es dia y distancia <= 400 km y ciudad no visitada) entonces:
                precio guardado pasa a valer el precio actual
                mejor destino = ruta posible
        
        ciudad_actual = mejor_destino