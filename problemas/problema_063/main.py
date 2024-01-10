x = int(input())
k = 0


def collatz(x):
    if x == 1:
        return 's'
    else:
        if x % 2 == 0:
            collatz(int(x/2))
        else:
            collatz(3*x + 1)


print(collatz(x))
