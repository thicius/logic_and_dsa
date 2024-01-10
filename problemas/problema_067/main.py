# Problema "Álbum da Copa" do NepsAcademy
# Link do problema: https://neps.academy/br/exercise/163

n = int(input())
m = int(input())

l = []
for i in range(m):
    l += [int(input())]

k = 0
for i in range(1, n+1):
    if i not in l:
        k += 1

print(k)
