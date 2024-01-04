# Problema "Huaauhahhuahau" do Neps Academy
# Link da questão: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/huaauhahhuahau

t = input()
v = ''

for string in t:
    if string in 'aeiou':
        v += string

for i in range(len(v)):
    if v[i] != v[-1-i]:
        print('N')
        break
else:
    print('S')
