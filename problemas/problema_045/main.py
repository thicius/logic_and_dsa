# Problema Consecutivos do NepsAcademy
# Link do Problema: https://neps.academy/br/course/programacao-basica-(codcad)/lesson/consecutivos


n = int(input())
l = input().split()
m = []                      # Maior lista, cujo len(m) será a saída
t = []


for i in range(len(l)):
    if i != len(l) - 1:
        if l[i] == l[i+1]:
            t += [l[i]]
        else:
            t += [l[i]]
            if len(t) > len(m):             # Agora preciso comparar a lista com a maior o momento
                m = t
                t = []
            else:
                t = []
    else:
        t += [l[i]]
        if len(t) > len(m):
            m = t

print(len(m))
