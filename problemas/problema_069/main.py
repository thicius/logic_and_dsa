# Função que substitui uma string em um documento por outra, criando um segundo documento

def substituir(string1, string2, archive1, archive2):
    for line in archive1:
        if string1 in line:
            l = line.split()
            for word in l:
                if word == l[-1]:
                    if word != string1:
                        archive2.write(word + '\n')
                    else:
                        archive2.write(string2 + '\n')
                elif word != string1:
                    archive2.write(word + ' ')
                else:
                    archive2.write(string2 + ' ')
        else:
            archive2.write(line)
