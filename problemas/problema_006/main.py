# Exercício 9.3 do livro Pense em Python, de Allen B. Downey

def avoids(palavra, letras_proibidas):
    for letra in letras_proibidas:
        if letra in palavra:
            return False
    return True

# Esta função recebe uma palavra e uma string de "letras proibidas" que retornaram False se estiverem na palavra


print(avoids('Python', 'yn'))
print(avoids('Python', 'asdfg'))

# A próxima função usa um arquivo em txt contendo palavras, que será chamado words.txt


def avoids_(letras_proibidas):
    n = 0
    for palavra in open('words.txt'):
        if avoids(palavra, letras_proibidas) == True:
            n += 1
    return n

# A função acima, depende da função anterior e do arquivo contendo as palavras
# Recebe uma string contendo certas letras, e devolve o número de palavras em 'words.txt' que não as usam
