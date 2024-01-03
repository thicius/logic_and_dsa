# Exercício 5 da parte 1 do livro "Python para Desenvolvedores" de Luiz Eduardo Borges

s = 'temos aqui um belo texto'


def inverso(s):
    lista = s.split()
    nova_frase = ''
    for palavra in lista:
        for i in range(0, len(palavra)):
            nova_frase += palavra[len(palavra)-1-i]
        nova_frase += ' '
    return nova_frase

# A ideia usada foi trasnformar a string "s" em uma lista para separar as palavras, criar uma nova frase
# e ir adicionando cada letra de cada palavra só que começando das últimas


print(inverso(s))
