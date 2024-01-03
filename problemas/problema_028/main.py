# Problema do Quadrado Mágico (OBI 2007)
# Link do Problema pelo Neps Academy: "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/quadrado-magico"

n = int(input())
k = []

for i in range(n):
    l = input().split()
    k += [l]

s = 0
for i in range(len(k)):
    s += int(k[0][i])

for coluns in k:
    ss = 0
    for lines in range(len(k)):
        ss += int(coluns[lines])
    if ss != s:
        s = -1
    else:
        ss = 0


for lines in range(len(k)):
    ss = 0
    for coluns in k:
        ss += int(coluns[lines])
    if ss != s:
        s = -1
    else:
        ss = 0


for i in range(len(k)):
    ss += int(k[i][i])
if ss != s:
    s = -1

ss = 0
for i in range(len(k)):
    ss += int(k[i][len(k)-i-1])
if ss != s:
    s = -1

print(s)
