# Exercício Potencia Simples do Neps Academy
# Link: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/potencias-simples

x, y = map(float, input().split())

n = round(x**y, 4)
m = "{:.4f}".format(n)
print(m)
