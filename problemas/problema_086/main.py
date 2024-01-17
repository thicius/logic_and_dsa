# Problema soma de frações do NepsAcademy
# Link: https://neps.academy/br/exercise/268

class Fracao:

    numerador: int
    denominador: int

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __mdc(self, numerador, denominador):
        if 1 in (numerador, denominador):
            return 1
        else:
            mi = min(numerador, denominador)
            ma = max(numerador, denominador)
            if mi == 0:
                return ma
            else:
                return self.__mdc(mi, ma-mi)

    def __add__(self, other):
        res_numerador = self.numerador * other.denominador + \
            other.numerador * self.denominador
        res_denominador = self.denominador * other.denominador
        mdc = self.__mdc(res_numerador, res_denominador)
        return '%d %d' % (int(res_numerador/mdc), int(res_denominador/mdc))


n1, d1, n2, d2 = map(int, input().split())

frac1 = Fracao(n1, d1)
frac2 = Fracao(n2, d2)
print(frac1 + frac2)
