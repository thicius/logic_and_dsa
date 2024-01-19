# Problema Substituir o Maior em Matriz 3x3
# Link: https://neps.academy/br/exercise/202

m = []

for i in range(9):
    m += [int(input())]

ma = max(m)
for i in range(9):
    if m[i] == ma:
        m[i] = -1

linha1 = ''
linha2 = ''
linha3 = ''

for i in range(3):
    linha1 += str(m[i]) + ' '

for i in range(3, 6):
    linha2 += str(m[i]) + ' '

for i in range(6, 9):
    linha3 += str(m[i]) + ' '

print(linha1)
print(linha2)
print(linha3)
