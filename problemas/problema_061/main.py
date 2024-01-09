# Problema "Pares ou com Último Algarismo Igual a 5" do NepsAcademy
# Link: https://neps.academy/br/exercise/177

a = int(input())
b = int(input())
c = int(input())

k = 0

for letter in [a, b, c]:
    if letter % 2 == 0 or letter % 10 == 5:
        k += 1

print(k)
