# Faremos essa questão igual ao problema anterior (problema_070) com algumas modificações
# Se a quantidade de horas for maior que 24 mostraremos a quantidade de dias passados

class Time:
    """ Representa um momento no tempo.
atributos = hora, minuto e segundo
"""


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


def add_time(t1, t2):
    add = time_to_int(t1) + time_to_int(t2)
    return int_to_time(add)

# Aqui está a função que usará as duas anteriores para nosso propósito:


def mul_time(time, n):
    res = time_to_int(time)*n
    time_d = Time()
    if int_to_time(res).hora >= 24:
        time_d = int_to_time(res)
        time_d.dia = int_to_time(res).hora // 24
        time_d.hora = int_to_time(res).hora % 24
        return time_d
    else:
        time_d = int_to_time(res)
        time_d.dia = 0
        return time_d

# Exemplo


time1 = Time()

time1.hora = 3
time1.minuto = 26
time1.segundo = 41

res = mul_time(time1, 6)
print(res.dia, res.hora, res.minuto, res.segundo)
