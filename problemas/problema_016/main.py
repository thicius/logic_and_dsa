# Exercício "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/gangorra"

# Lendo a entrada do exercício
P1, C1, P2, C2 = map(int, input().split())

# Seu código vai aqui
if P1*C1 == P2*C2:
    print(0)
elif P1*C1 > P2*C2:
    print(-1)
else:
    print(+1)
