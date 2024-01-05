# Problema Fita Colorida da OBI 2015, nível Júnior
# Link do Problema: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/fita-colorida

# criando a lista que terá a posição dos zeros:

n = int(input())
l = input().split()

t = []
for i in range(n):
    if l[i] == '0':
        t += [i]

# criando uma função módulo:


def m(x):
    if x >= 0:
        return x
    else:
        return x*(-1)


# atribuindo à cada posição da fita, a mínima distância à uma cor de tom "0":
f = l
min = n

for i in range(n):
    for j in t:
        if m(i-int(j)) < min:
            min = m(i - int(j))
    if min < 10:
        f[i] = min
        min = n
    else:
        f[i] = 9
        min = n

# criando a string que será a saída:

p = ''
for letter in f:
    p += str(letter) + ' '

print(p)
