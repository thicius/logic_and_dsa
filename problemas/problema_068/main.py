# Problema "Tempo de Viagem em Segundos" do NepsAcademy
# Link: https://neps.academy/br/exercise/178

d1 = int(input())
h1 = int(input())
m1 = int(input())
d2 = int(input())
h2 = int(input())
m2 = int(input())

soma = 0
soma += max((d2 - d1)*86400, 0)
soma += max((h2 - h1)*3600, 0)
soma += max((m2 - m1)*60, 0)
print(soma)
