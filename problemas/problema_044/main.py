# Problema "Primo" do NepsAcademy:
# Link do problema : https://neps.academy/br/course/programacao-basica-(codcad)/lesson/primo

n = int(input())
c = 0

for i in range(1, n+1):
    if n % i == 0:
        c += 1

if c == 2:
    print("S")
else:
    print('N')
