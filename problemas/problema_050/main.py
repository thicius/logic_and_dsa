# Problema, Múltiplos de 2, 3 e 4 do NepsAcademy
# Link: https://neps.academy/br/exercise/155

n = int(input())

l = []
for i in range(n):
    l += [int(input())]

s2 = 0
s3 = 0
s4 = 0
for member in l:
    if member % 2 == 0:
        s2 += 1
    if member % 3 == 0:
        s3 += 1
    if member % 4 == 0:
        s4 += 1

print(s2)
print(s3)
print(s4)
