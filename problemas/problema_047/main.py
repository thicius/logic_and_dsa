
# pegando os input's e colocando numa matriz 'k':

line1 = input().split()
n = int(line1[0])
m = int(line1[1])
k = []
for i in range(m):
    k += [input().split()]

# criação da lista que atribui a pontuação ao país:

l = []
for i in range(n):
    l += ['']

# entrando as medalhas de ouro:

for j in range(m):
    for i in range(n):
        if k[j][0] == str(i+1):
            l[i] += 'z'


# entregando as medalhas de prata:

for j in range(m):
    for i in range(n):
        if k[j][1] == str(i+1):
            l[i] += 'y'


# entregando as medalhas de bronze:

for j in range(m):
    for i in range(n):
        if k[j][2] == str(i+1):
            l[i] += 'x'


# atribuindo o número do time:

for i in range(n):
    if i < 90:
        l[i] += str(99-i)
    else:
        l[i] += '0' + str(99-i)

# a lista de "pontos" em ordem decrescente, o inverso do sorted(l):

isl = []
for i in range(n):
    isl += [sorted(l)[n-1-i]]


# criando a string que será a saída:

p = ''
for item in isl:
    p += str(l.index(item)+1) + ' '

print(p)
