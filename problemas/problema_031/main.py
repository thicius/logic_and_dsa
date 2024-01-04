# Exercício "https://neps.academy/br/course/programacao-basica-(codcad)/lesson/overflow"
# Overflow

overflow = int(input())
line2 = input().split()

first_n = int(line2[0])
operation = line2[1]
second_n = int(line2[2])

if operation == '+':
    result = first_n + second_n
elif operation == '*':
    result = first_n * second_n

if result <= overflow:
    print('OK')
else:
    print('OVERFLOW')
