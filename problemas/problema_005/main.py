# Problema Lançamento de Dados do Neps Academy
# Link: https://neps.academy/br/exercise/188

import string
n = int(input())
l = []

for i in range(12):
    l += [0]

faces = []

for i in range(n):
    faces += [int(input())]

maximos = []

for numero in faces:
    l[numero - 1] += 1


for i in range(12):
    if l[i] == max(l):
        maximos += [i+1]

s = ''
for valores in maximos:
    s += str(valores) + ' '

print(s)
