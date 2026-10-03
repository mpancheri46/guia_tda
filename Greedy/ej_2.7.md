OPT(0) = 0

para i desde 1 hasta n:
    buscar p(i) = ultima charla anterior compatible con i

    tomar = score(i) + OPT(p(i))
    no_tomar = OPT(i - 1)

    OPT(i) = max(tomar, no_tomar)

devolver OPT(n)

no busco una charla “mejor” de forma individual, sino que para cada charla compara cuanto obtiene si la elije contra cuanto tiene si no.