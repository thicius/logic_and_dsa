# Problema Critérios de Divisibilidade II do NepsAcademy
# Link: https://neps.academy/br/exercise/263

n = str(input())

if int(n[-2:]) % 4 == 0:
    print('S')
else:
    print('N')

soma = 0
for s in n:
    soma += int(s)

if soma % 9 == 0:
    print('S')
else:
    print('N')

if n[-2:] in ('0', '00', '25', '50', '75'):
    print('S')
else:
    print('N')
