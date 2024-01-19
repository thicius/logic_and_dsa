# Problema Contar Bits do Neps Academy
# Link: https://neps.academy/br/exercise/311

import math

k = 0


def operacao(x):
    global k
    if x == 1:
        k += 1
        print(k)
    elif x == 0:
        print(k)
    else:
        menor_potencia_de_dois = int(math.log(x, 2))
        k += 1
        return operacao(x - 2**menor_potencia_de_dois)


n = int(input())
operacao(n)
