# Problema "Andando no Tempo" do NepsAcademy
# Link: https://neps.academy/br/exercise/111

line = input().split()

a = int(line[0])
b = int(line[1])
c = int(line[2])

if a == b or a == c or b == c:
    print('S')
elif max(a - b, b - a) == c or a + b == c:
    print('S')
else:
    print('N')
