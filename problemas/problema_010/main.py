# Problema Lâmpada do Neps Academy
# Link: https://neps.academy/br/exercise/52

n = int(input())
l = input().split()
p2 = 0

for i in range(n):
    oi = int(l[i])
    if oi == 2:
        p2 += 1

if n % 2 == 0:
    r1 = 0
else:
    r1 = 1

if p2 % 2 == 0:
    r2 = 0
else:
    r2 = 1

print(r1)
print(r2)
