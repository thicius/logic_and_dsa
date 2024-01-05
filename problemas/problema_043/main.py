# Problema Senha 2018 do NepsAcademy
# Link do Problema: https://neps.academy/br/exercise/153

n = 0


def f(n):
    a = int(input())
    if a == 2018:
        print(n)
    else:
        f(n+1)


f(0)
