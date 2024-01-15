# Método

class Time():
    def time_to_int(self):
        r = int(self.segundo) + int(self.minuto)*60 + int(self.hora)*3600
        return r

# Teste


start = Time()
start.segundo = 34
start.minuto = 46
start.hora = 2

print(Time.time_to_int(start))
