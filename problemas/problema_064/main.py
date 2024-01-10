# Problemaa "Teleférico" do NepsAcademy
# Link: https://neps.academy/br/exercise/15

a = int(input())
b = int(input())

r = b // (a-1)
if b % (a-1) != 0:
    r += 1

print(r)
