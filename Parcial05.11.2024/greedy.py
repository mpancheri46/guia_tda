
#jaja xd

def descifrar(palabras, diccionario):
    clave = {}
    pendientes = palabras.copy()
    traducidas = 0

    while pendientes and traducidas < 15:
        mejor = None
        mayor_cantidad = 0

        for palabra in pendientes:
            for candidata in diccionario:
                if es_compatible(palabra, candidata, clave):
                    nueva_clave = extender(clave, palabra, candidata)

                    cantidad = contar_compatibles(
                        pendientes, diccionario, nueva_clave
                    )

                    if cantidad > mayor_cantidad:
                        mayor_cantidad = cantidad
                        mejor = nueva_clave

        if mejor is None:
            return None

        clave = mejor
        traducidas = contar_traducidas(palabras, diccionario, clave)
        pendientes = quitar_traducidas(pendientes, clave)

    if traducidas >= 15:
        return clave

    return None