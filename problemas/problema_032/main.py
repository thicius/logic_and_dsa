# Exercício "Vestibular" do NepsAcademy
# https://neps.academy/br/course/programacao-basica-(codcad)/lesson/vestibular

questões = int(input())
prova = input().split()[0]
aluno = input().split()[0]

n = 0

for i in range(0, questões):
    if prova[i] == aluno[i]:
        n += 1

print(n)
