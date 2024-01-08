# Problema Móbile (OBI 2015) do NepsAcademy
# Link: https://neps.academy/br/exercise/50

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b != c:
    print('N')
else:
    if b + c != d:
        print('N')
    else:
        if a != b + c + d:
            print('N')
        else:
            print('S')
