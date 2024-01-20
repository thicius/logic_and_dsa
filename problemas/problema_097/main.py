# Problema do livro PenseEmPython sobre o método __lt__

class Time:

    def __init__(self, hora: int, minuto: int, segundo: int) -> None:
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def __lt__(self, other):
        t1 = self.hora, self.minuto, self.segundo
        t2 = other.hora, other.minuto, other.segundo
        return t1 < t2


# Testando

agora = Time(21, 45, 30)
qualquer_hora = Time(13, 30, 00)

print(qualquer_hora < agora)
