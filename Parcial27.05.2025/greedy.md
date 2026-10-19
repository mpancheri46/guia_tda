Para cada región i:
    excedente[i] = max(0, Gi - Di)
    deficit[i] = max(0, Di - Gi)

Ordenar las regiones con déficit según el criterio greedy.

Para cada región i con déficit:
    Mientras deficit[i] > 0:
        Buscar una región j con excedente y
        capacidad disponible para enviar a i.

        Si no existe:
            Marcar que no se pudo cubrir la demanda.
            Pasar a la siguiente región.

        cantidad = min(excedente[j],deficit[i],capacidad_disponible[j][i])

        Registrar el transporte de j hacia i.

        excedente[j] -= cantidad
        deficit[i] -= cantidad
        capacidad_disponible[j][i] -= cantidad

Devolver los transportes realizados.

No se garantiza econtrar la mejor distribucion ya que se basa en decisiones locales que pueden bloquear a otras alternativas.