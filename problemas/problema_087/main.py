# Problema Frequência na Aula, Neps Academy
# Link: https://neps.academy/br/exercise/252

n = int(input())

l = []
for i in range(n):
    l += [int(input())]

sl = sorted(l)

k = 0
for i in range(1, n):
    if sl[i] == sl[i-1]:
        k += 1

print(n - k)
