# Problema Multiplicação e Divisão de Frações do NepsAcademy
# Link: https://neps.academy/br/exercise/2237

# Grande parte do código já foi dado, o exercício é escrever a codificação que dirá se o personagem morreu

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    # TODO: Implemente o operador de multiplicação.
    def __mul__(self, fracao):
        c = Fracao(1, 1)
        c.numerador = a.numerador * b.numerador
        c.denominador = a.denominador * b.denominador
        return c

    # TODO: Implemente o operador de divisão.
    def __truediv__(self, fracao):
        c = Fracao(1, 1)
        c.numerador = a.numerador * b.denominador
        c.denominador = a.denominador * b.numerador
        return c


if __name__ == "__main__":

    a_numerador, a_denominador = map(int, input().split())
    b_numerador, b_denominador = map(int, input().split())
    op = input()

    a = Fracao(a_numerador, a_denominador)
    b = Fracao(b_numerador, b_denominador)

    if op == "M":
        c = a * b
    else:
        c = a / b

    print(c.numerador, c.denominador)
