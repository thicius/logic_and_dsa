# Exercício "https://neps.academy/br/exercise/324" do Neps Academy

n = int(input())
k = 0

for i in range(n):
    li = input()
    if int(li.split()[0]) > int(li.split()[1]):
        k += int(li.split()[1])

print(k)
