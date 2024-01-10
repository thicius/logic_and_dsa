# Problema "Maior Área" do NepsAcademy
# https://neps.academy/br/exercise/214

line1 = input().split()
line2 = input().split()

prod1 = int(line1[0])*int(line1[1])

prod2 = int(line2[0])*int(line2[1])

if prod1 > prod2:
    print('Primeiro')
elif prod1 < prod2:
    print('Segundo')
else:
    print('Empate')
