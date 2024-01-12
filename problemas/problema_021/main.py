# Exercício Prêmio do Milhão do NepsAcademy
# Link: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/premio-do-milhao

n = int(input())
l = 1
s = 0

for i in range(n):
    ki = input()
    s += int(ki)
    if s < 10**6:
        i += 1
        l += 1
print(l)
