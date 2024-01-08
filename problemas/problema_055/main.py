# Problema Cobra Coral do NepsAcademy
# Link: https://neps.academy/br/exercise/72

sequence = input().split()

if sequence[0] == sequence[2] and sequence[1] != sequence[3]:
    print('V')
elif sequence[1] == sequence[3] and sequence[0] != sequence[2]:
    print('V')
else:
    print('F')
