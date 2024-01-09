# Problema Jogo de Par ou Impar do NepsAcademy
# Link: https://neps.academy/br/exercise/51

player = int(input())
first = int(input())
second = int(input())

result = first + second

if (result + player) % 2 == 0:
    print('0')
else:
    print('1')
