# Ordem: parênteses, expoentes, multiplicações e divisões, soma e subtrações.
# Símbolos: +, -, *, /, ^, (, ).

""" Ainda há alguns problemas a resolver
Postei aqui apenas porque os primeiros passos já foram dados;
 """

conta = input().split()

# A função definida abaixo indica a posição de todos os parenteses, p.ex: [ '(' , 4 ]


def olhar_parenteses(conta_):

    global posicao_dos_parenteses
    posicao_dos_parenteses = []
    global contagem_de_parenteses_e
    contagem_de_parenteses_e = 0
    global contagem_de_parenteses_d
    contagem_de_parenteses_d = 0

    for i in range(len(conta_)):
        if conta_[i] == '(':
            j = ['(', i]
            posicao_dos_parenteses += [j]
            contagem_de_parenteses_e += 1
        elif conta_[i] == ')':
            j = [')', i]
            posicao_dos_parenteses += [j]
            contagem_de_parenteses_d += 1


olhar_parenteses(conta)
k = 0


# Uma vez que a função "olhar_parenteses()" nos indicou quais resolver primeiro;
# A função resolver, recebe o índice inicial e final de qual conta resolver na lista


def resolver(inicio, fim):

    conta_sem_parenteses = conta[inicio + 1: fim]

    while len(conta_sem_parenteses) != 1:

        for i in range(1, len(conta_sem_parenteses)):

            while i <= len(conta_sem_parenteses) - 1:

                if str(conta_sem_parenteses[i]) in '^':
                    conta_sem_parenteses[i] = operar(
                        conta_sem_parenteses[i-1], conta_sem_parenteses[i], conta_sem_parenteses[i+1])
                    conta_sem_parenteses.remove(conta_sem_parenteses[i+1])
                    conta_sem_parenteses.remove(conta_sem_parenteses[i-1])

                elif str(conta_sem_parenteses[i]) in '*/':
                    conta_sem_parenteses[i] = operar(
                        conta_sem_parenteses[i-1], conta_sem_parenteses[i], conta_sem_parenteses[i+1])
                    conta_sem_parenteses.remove(conta_sem_parenteses[i+1])
                    conta_sem_parenteses.remove(conta_sem_parenteses[i-1])

                elif str(conta_sem_parenteses[i]) in '+-':
                    conta_sem_parenteses[i] = operar(
                        conta_sem_parenteses[i-1], conta_sem_parenteses[i], conta_sem_parenteses[i+1])
                    conta_sem_parenteses.remove(conta_sem_parenteses[i+1])
                    conta_sem_parenteses.remove(conta_sem_parenteses[i-1])

                i += 1

    return conta_sem_parenteses[0]


# Dividindo o trabalho em situações menores, temos a função operar que faz as operações entre dois números


def operar(first_number, operation, second_number):

    if operation == '+':
        return float(first_number) + float(second_number)

    elif operation == '-':
        return float(first_number) - float(second_number)

    elif operation == '*':
        return float(first_number) * float(second_number)

    elif operation == '/':
        return float(first_number) / float(second_number)

    elif operation == '^':
        return float(first_number) ** float(second_number)


# Função que identifica quais os primeiros parênteses para calcular


def parenteses_fechados():

    global k
    k = 0

    for i in range(len(posicao_dos_parenteses)):

        if posicao_dos_parenteses[i][0] == '(' and posicao_dos_parenteses[i+1][0] == ')' and k == 0:

            conta[int(posicao_dos_parenteses[i][1])] = resolver(
                posicao_dos_parenteses[i][1], posicao_dos_parenteses[i+1][1])

            desnecessario = int(posicao_dos_parenteses[i+1]
                                [1]) - int(posicao_dos_parenteses[i][1])

            for j in range(desnecessario):
                conta[int(posicao_dos_parenteses[i][1] + 1)] = 'A'
                conta.remove('A')
                k += 1


# O while abaixo segue os passos para resolver os parenteses, repetidas vezes até só sobrar a solução

while len(conta) != 1:
    parenteses_fechados()
    olhar_parenteses(conta)
    k = 0

# Saída

print('A solução é \n%f' % (float(conta[0])))
