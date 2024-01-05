# Problema "Torres de Hanói" da (OBI 2003)
# Link do problema no NepsAcademy: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/torres-de-hanoi

k = 0

while True:
    n = int(input())
    if n == 0:
        print(' ')
        print('Teste', k)
        print(2**(m)-1)
        break
    else:
        if k == 0:
            k += 1
            m = n
        else:
            print('Teste', k)
            print(2**(m)-1)
            k += 1
            m = n
