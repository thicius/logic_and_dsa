# Problema do livro "Pense em Python" de Allen B. Downey

d = {}

d['palavra'] = 'word'
d['converse'] = 'talk'
d['conserve'] = 'preserve'

# d é um dicionário qualquer, a função abaixo encontra entre as chaves de 'd' pares de metátese
# Isto é, pares de palavras que podem ser obtidas uma da outra trocando duas e apenas duas letras
the_tuple = []

for i in range(65, 122):
    the_tuple += [(chr(i), chr(i))]

# Com isto acima: criei uma lista de tuples que contém todos os pares como ('A', 'A') ou ('z', 'z')


def verify(x, y):
    n = 0
    for par in zip(x, y):
        if par not in the_tuple:
            n += 1
    if n == 2:
        return print('Temos uma metátese!', '"', x, '"', 'e', '"', y, '"')

# Com isto acima: criei uma função que verifica se duas strings (x, y) são uma metátese
# Verificando se o zip(x, y) tem exatamente 2 pares que não estão no the_tuple


def metátese(d):
    for chave1 in d:
        for chave2 in d:
            if chave1 > chave2 and sorted(chave1) == sorted(chave2):
                verify(chave1, chave2)

# Com isto acima: garatimos que verificaremos apenas chaves que tenham exatamente as mesmas letras
# E que não verificaremos o mesmo par duas vezes


print(metátese(d))
