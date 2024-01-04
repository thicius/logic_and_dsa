# Problema Campo Minado do NepsAcademy
# link do problema: "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/campo-minado"

n = int(input())
l = []
d = []

for i in range(n):
    l += [int(input())]

for i in range(n):
    d.append(l[i])

for i in range(n):
    if i != 0:
        d[i] += (l[i-1])
    if i != n-1:
        d[i] += l[i+1]

for i in range(n):
    print(d[i])
