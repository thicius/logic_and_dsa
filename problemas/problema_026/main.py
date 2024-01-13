# Exercício Soma do Vetor do NepsAcademy
# Lunk: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/soma-do-vetor

n = input()
l = input().split()
s = 0

for number in l:
    s += int(number)

print(s)
