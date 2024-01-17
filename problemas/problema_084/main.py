# Problema Critérios de Divisibilidade III
# Link: https://neps.academy/br/exercise/272

n = str(input())
l = (len(n) // 2)

if len(n) % 2 == 0:
    s = 0
    for i in range(l):
        s += int(n[2*i])
        s -= int(n[2*i + 1])
else:
    s = int(n[-1])
    for i in range(l):
        s += int(n[2*i])
        s -= int(n[2*i + 1])

if s % 11 == 0:
    print('S')
else:
    print('N')
