# Problema Conversão de Inteiro para Binário
# Link: https://neps.academy/br/exercise/195

import math

n = int(input())

if n == 0:
    maior = 0
else:
    maior = int(math.log(n, 2))

retorno = ''
for i in range(maior+1):
    if n >= 2**(maior - i):
        n = n - 2**(maior - i)
        retorno += '1'
    else:
        retorno += '0'

print(retorno)
