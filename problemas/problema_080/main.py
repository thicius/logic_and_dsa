# Critérios de Divisibilidade do NepsAcademy
# Link: https://neps.academy/br/exercise/266

n = str(input())

if n[-1] in '02468':
    print('S')
else:
    print('N')

soma = 0
for s in n:
    soma += int(s)

if soma % 3 == 0:
    print('S')
else:
    print('N')

if n[-1] in '05':
    print('S')
else:
    print('N')
