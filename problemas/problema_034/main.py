# Problema "Zerinho ou Um" do Neps Academy
# Link: https://neps.academy/br/exercise/88

n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

if a != b and a != c:
    print('A')
elif b != a and b != c:
    print('B')
elif c != a and c != b:
    print('C')
else:
    print('*')
