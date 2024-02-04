# Problema Tira-Teima, Neps Academy
# Link: https://neps.academy/br/exercise/220

a, b = map(int, input().split())

k = 0

if 0 <= a <= 432 and 0 <= b <= 468:
    k = 1

if k == 1:
    print('dentro')
else:
    print('fora')
