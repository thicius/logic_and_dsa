# Exercício "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/todos-os-divisores"

x = int(input())
t = ''

for i in range(1, x+1):
    if x % i == 0:
        t += str(i) + ' '

print(t)
