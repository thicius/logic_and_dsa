# Exercícios "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/aprovado-ou-reprovado"

a, b = map(float, input().split())

media_ = (float(a) + float(b))/2
media = float(media_)

if media >= 7:
    print('Aprovado')
elif media >= 4:
    print('Recuperacao')
else:
    print('Reprovado')
