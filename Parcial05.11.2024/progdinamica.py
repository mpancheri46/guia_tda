def mochila(litros, kilos, elementos, elemento_actual, guia_elegida):

    if elemento_actual == len(elementos):
        if guia_elegida:
            return 0
        return -float("inf")

    elemento = elementos[elemento_actual]

    no_elegir = mochila(litros, kilos, elementos, elemento_actual + 1, guia_elegida)

    elegir = elemento.beneficio + mochila(litros - elemento.volumen,kilos - elemento.peso,elementos,elemento_actual + 1,guia_elegida)

    return max(no_elegir, elegir)