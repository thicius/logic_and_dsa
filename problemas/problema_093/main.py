# Exercício 13.5 do livro "Pense em Python" do Allen B. Downey
# Função que a partir de um histograma, devolve uma chave com probabilidade proporcional à sua frequência

d = {'a': 2, 'b': 1}            # Um histograma qualquer


def choose_from_hist(d):
    lista = []
    for item in d:
        lista += item*d[item]
    return random.choice(lista)

# A ideia foi criar uma lista onde cada chave aparece "valor" vezes e usar o random.choice


print(choose_from_hist(d))
