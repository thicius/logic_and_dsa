# Exercício 9.5 do livro Pense em Python de Allen B. Downey

def uses_all(palavra, letras_obrigatorias):
    n = 0
    for letra in letras_obrigatorias:
        if letra in palavra:
            n += 1
    if n == len(letras_obrigatorias):
        return True
    else:
        return False

# Esta função recebe uma palavra e uma string, que se suas letras estiverem todas na palavra, retorna True


print(uses_all('Amazing', 'aing'))
print(uses_all('Amazing', 'oing'))
