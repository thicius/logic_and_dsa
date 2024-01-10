# Problema Drone de Entrega, do NepsAcademy
# Link: https://neps.academy/br/exercise/14

a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())

k = [a1, a2, a3]
del (k[k.index(min(k))])

if min(a1, a2, a3) > min(b1, b2):
    print('N')
else:
    if min(k) > max(b1, b2):
        print('N')
    else:
        print('S')
