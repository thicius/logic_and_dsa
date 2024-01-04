# Exercício "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/ordenacao-simples"

n = int(input())

l = map(int, input().split())

l = sorted(l)

p = ''

for number in l:
    p += str(number) + ' '

print(p)
