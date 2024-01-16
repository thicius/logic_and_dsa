# Problema, Quadrado Mágico 3x3 do NepsAcademy
# Link: https://neps.academy/br/exercise/198

l = []
for i in range(9):
    l += [int(input())]

k = 0
s = l[0] + l[1] + l[2]

# A soma das linhas

for i in (3, 6):
    if l[i] + l[i+1] + l[i+2] != s:
        k += 1

# A soma das colunas

for i in (0, 1, 2):
    if l[i] + l[i+3] + l[i+6] != s:
        k += 1

# A soma das diagonais

if l[0] + l[4] + l[8] != s:
    k += 1

if l[2] + l[4] + l[6] != s:
    k += 1

# Resultado

if k != 0:
    print('NAO')
else:
    print('SIM')
