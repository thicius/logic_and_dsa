# Esta função recebe um texto em formato de string (d1) junto com uma lista de palavras d2
# E retorna em um dicionário as palavras de d1 que não estão em d2, com valor = none


def subtrair(d1, d2):
    res = {}
    for word in d1.lower().split():
        word = word.strip(string.punctuation + ' ')
        if word not in d2:
            res[word] = None
    return print(res)

# Exemplo:


d1 = 'Minha terra tem palmeiras onde canta o sabiá; as aves, que aqui gorjeiam, não gorjeiam como lá.'
d2 = ['minha', 'tem', 'onde', 'o', 'as', 'que', 'gorjeiam', 'como']

print(subtrair(d1, d2))
