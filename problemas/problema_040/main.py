# Problema "Soma dos Elementos" do NepsAcademy
# Link: https://neps.academy/br/exercise/159

n = int(input())
l = input().split()

s = 0
for number in l:
    s += int(number)

print(s)
