import random

j1_dado1 = random.randint(1, 6)
j1_dado2 = random.randint(1, 6)
j2_dado1 = random.randint(1, 6)
j2_dado2 = random.randint(1, 6)

j1_total = j1_dado1 + j1_dado2
j2_total = j2_dado1 + j2_dado2

print(f"Jugador 1: {j1_dado1} + {j1_dado2} = {j1_total}")
print(f"Jugador 2: {j2_dado1} + {j2_dado2} = {j2_total}")

if j1_total > j2_total:
    print("Gana el Jugador 1")
elif j2_total > j1_total:
    print("Gana el Jugador 2")
else:
    if j1_dado1 > j2_dado1 and j1_dado1 >= j1_dado2 and j1_dado1 >= j2_dado2:
        print("Gana el Jugador 1 por dado más alto")
    elif j1_dado2 > j2_dado1 and j1_dado2 >= j2_dado2:
        print("Gana el Jugador 1 por dado más alto")
    elif j2_dado1 > j1_dado1 and j2_dado1 >= j1_dado2 and j2_dado1 >= j2_dado2:
        print("Gana el Jugador 2 por dado más alto")
    elif j2_dado2 > j1_dado1 and j2_dado2 >= j1_dado2:
        print("Gana el Jugador 2 por dado más alto")
    else:
        print("¡Empate total!")