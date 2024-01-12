# Problema de POO do capítulo 15 de Pense Em Python do Allen B. Downey

class Time:
    """ Representa um momento no tempo.
atributos = hora, minuto e segundo
"""

# Criando dois tempos que serão usados na função:


time1 = Time()
time2 = Time()

time1.hora = 3
time1.minuto = 26
time1.segundo = 41

time2.hora = 8
time2.minuto = 47
time2.segundo = 39

# As duas funções que serão usadas:


def time_to_int(time):
    n = 0
    n += (time.segundo)
    n += (time.minuto)*60
    n += (time.hora)*3600
    return n


def int_to_time(n):
    time_ = Time()
    time_.hora = (n//3600)
    time_.minuto = (n % 3600) // 60
    time_.segundo = (n % 60)
    return time_

# Por fim, a função que soma dois tempos:


def add_time(t1, t2):
    add = time_to_int(t1) + time_to_int(t2)
    return int_to_time(add)

# Teste


time3 = add_time(time1, time2)

print('%d:%d:%d' % (int(time3.hora), int(time3.minuto), int(time3.segundo)))
