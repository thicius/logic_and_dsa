# Exercício "https://neps.academy/br/exercise/47" do NepsAcademy

n = int(input())
l = input().split()
s = 0

for i in range(n-2):
    ni = int(l[i])
    nj = int(l[i+1])
    nk = int(l[i+2])
    if ni == 1 and nj == 0 and nk == 0:
        s += 1

print(s)
