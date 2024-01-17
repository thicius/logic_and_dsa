# O problema 3n + 1 do NepsAcademy
# Link: https://neps.academy/br/exercise/259

x = int(input())
k = 0


def collatz(x):
    global k
    if x != 1:
        if str(x)[-1] in '02468':
            k += 1
            return collatz(int(x/2))
        else:
            k += 1
            return collatz(3*x + 1)
    else:
        return k


print(collatz(x))
