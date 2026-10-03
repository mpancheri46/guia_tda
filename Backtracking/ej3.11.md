  S E N D
+ M O R E        una poda posible puede ser que y no puede coincidir en un digito que ya usa otra letra
---------        si S + M + C3 = M, entonces S + C3 = 10 -> c3 solo puede ser 0 1 enonces s = 9 y c3 =1 por lotanto M = 1
M O N E Y         

Letras iniciales distintas de 0
S y M son los primeros dígitos de SEND, MORE y MONEY -> no pueden valer 0.


Usar los acarreos
Cada columna puede generar un acarreo de 0 o 1. Ese acarreo restringe inmediatamente la columna siguiente.

dos letras con el mismo número


una letra que tendría que ser 10


una suma que obliga a usar un número que ya está ocupado

S no es 9


M no es 1


La principal ventaja del backtracking en este problema es que no espera a completar una asignacion de las ocho letras para verificarla. Las restricciones de dígitos distintos, los valores de las columnas y los acarreos permiten detectar inconsistencias durante la construcción de la solución y podar ramas completas del árbol de búsqueda. En particular, del análisis de la primera columna podemos deducir directamente S = 9, M = 1 y c3 = 1.