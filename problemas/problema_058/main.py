# Problema Função Fatorial do NepsAcademy
# Link: https://neps.academy/br/exercise/174

def fatorial(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f


n = int(input())
print(fatorial(n))
