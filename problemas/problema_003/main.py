# Problema Ordenação Simples
# Link: https://neps.academy/br/exercise/400

l = []
for i in range(10):
    l += [int(input())]

sl = sorted(l)

s = ''
for number in sl:
    s += str(number) + ' '

inv_s = ''
for i in range(10):
    inv_s += str(sl[10 - i - 1]) + ' '

print(s)
print(inv_s)
