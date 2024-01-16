# Problema Troco em Moedas do NepsAcademy
# Link: https://neps.academy/br/exercise/143

n = int(input())

um_real = n // 100
n = n % 100

cinquenta_centavos = n // 50
n = n % 50

vinte_e_cinco_centavos = n // 25
n = n % 25

dez_centavos = n // 10
n = n % 10

cinco_centavos = n // 5
n = n % 5

um_centavo = n


s = 0
for number in (um_real, cinquenta_centavos, vinte_e_cinco_centavos, dez_centavos, cinco_centavos, um_centavo):
    s += number


print(s)
print(um_real)
print(cinquenta_centavos)
print(vinte_e_cinco_centavos)
print(dez_centavos)
print(cinco_centavos)
print(um_centavo)
