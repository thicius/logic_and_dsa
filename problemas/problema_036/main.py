# Problema "Medalhas" da OBI de 2016
# Link do problema no NepsAcademy: https://neps.academy/br/exercise/2

l = [0, 0, 0]

l[0] = int(input())
l[1] = int(input())
l[2] = int(input())


for i in range(3):
    if l[i] == min(l):
        min = i+1
    elif l[i] == max(l):
        max = i+1
    else:
        mid = i+1

print(min)
print(mid)
print(max)
