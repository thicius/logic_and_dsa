# Exercícios Primo do NepsAcademy
# Link: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/primo

s = input().split()
f = ''


def titulo(s):
    r = s[0].upper()
    for letter in s[1:]:
        r += letter.lower()
    return r


for word in s:
    f += titulo(word) + ' '

print(f)
