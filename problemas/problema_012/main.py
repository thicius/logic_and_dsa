# Exercício "Contagem de Algarismos" do NepsAcademy
# Link: "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/contagem-de-algarismos"

n = int(input())
d = {}

for numeral in '0123456789':
    d[numeral] = 0

for i in range(n):
    ni = str(input())
    for numeral in ni:
        d[numeral] += 1

for key in d:
    print(key, '-', d[key])
