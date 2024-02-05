# Problema "Fórmula 1" do NepsAcademy: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/formula-1

# Preparando os inputs para cancelar quando n = ['0', '0']

while True:
    n = input().split()

    if n == ['0', '0']:
        break

    quantidade_de_corridas = int(n[0])
    quantidade_de_competidores = int(n[1])

    # Criação da lista

    resultados_das_corridas = []
    for i in range(quantidade_de_corridas):
        resultados_das_corridas += [input().split()]

    # Resolvendo os sistemas de pontuações

    quantidade_de_sistemas = int(input())

    sistemas_de_pontuacoes = []
    for i in range(quantidade_de_sistemas):
        sistemas_de_pontuacoes += [input().split()]

    # Função que depende dos sistemas de pontuações para printar uma saída

    # OBS: "sistema_de_pontuação" é apenas UM da lista "sistema_de_pontuações"
    def f(sistema_de_pontuação):

        # Criando da lista que relacionará índice à pontuação

        pontuacoes = []
        for i in range(quantidade_de_competidores):
            pontuacoes += [0]

        # Depois de criar a lista, vamos atribuir aos competidores seus pontos

        for corrida in resultados_das_corridas:
            for j in range(int(sistema_de_pontuação[0])):
                pontuacoes[int(corrida.index(str(j+1)))
                           ] += int(sistema_de_pontuação[j+1])

            # Agora precisamos ver quais os índices dessa lista "pontuacoes" que obtiveram maiores pontos:
            # Criarei uma nova lista chamada "campeoes" que terá os índices

        campeoes = []
        for i in range(len(pontuacoes)):
            if pontuacoes[i] == max(pontuacoes):
                campeoes += [i+1]

        mensagem = ''
        for i in range(len(campeoes)):
            mensagem += str(sorted(campeoes)[i]) + ' '
        return mensagem

        # Preciso printar todos os sistemas de pontuações

    for systems in sistemas_de_pontuacoes:
        print(f(systems))
