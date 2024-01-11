# Exercício "Par ou Ímpar" do Neps Academy
# Link: "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/par-ou-impar"

b = int(input())
c = int(input())

soma = b + c
if float(soma//2) == float(soma/2):
    print('Bino')
else:
    print('Cino')
