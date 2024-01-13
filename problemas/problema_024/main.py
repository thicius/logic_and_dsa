# Exercício Raízes do NepsAcademy
# Link: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/raizes

n = int(input())
k = input().split()

for i in range(n):
    ni = float(k[i])
    ri = (float(ni))**(0.5)
    print("{:.4f}".format(ri))
