# Problema "Impedido!" do NepsAcademy
# Link do Problema: https://neps.academy/br/exercise/46

line1 = input().split()
l = int(line1[0])
r = int(line1[1])
d = int(line1[2])

if r > 50 and l < r and r > d:
    print('S')
else:
    print('N')
