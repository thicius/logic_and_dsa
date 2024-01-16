# Problema "Fuga com Helicóptero" do NepsAcademy
# Link: https://neps.academy/br/exercise/5

# Recebendo a entrada

inp = input().split()
h = int(inp[0])
p = int(inp[1])
f = int(inp[2])
d = int(inp[3])

# Caso onde f está entre h e p

if p < f < h:
    if d == 1:
        print('S')
    else:
        print('N')

if h < f < p:
    if d == 1:
        print('N')
    else:
        print('S')

# Caso em que f é maior que ambos:

if f > p and f > h:
    if h > p:
        if d == 1:
            print('N')
        else:
            print('S')
    else:
        if d == -1:
            print('N')
        else:
            print('S')

# Caso em que f é menor que ambos

if f < p and f < h:
    if h < p:
        if d == 1:
            print('S')
        else:
            print('N')
    else:
        if d == -1:
            print('S')
        else:
            print('N')
