# Problema "Desafio do Maior Número" do NepsAcademy
# Link: https://neps.academy/br/exercise/323

sequence = input().split()

numbers = []
for string in sequence:
    numbers += [int(string)]

print(max(numbers))
