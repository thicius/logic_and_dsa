# Exercício Fibonacci do NepsAcademy
# Link: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/fibonacci

n = int(input())


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(n))
