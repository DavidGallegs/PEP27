import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")
jugador = int(input("Elige (1-3): "))
bot = random.randint(1, 3)

print("Tú elegiste:", jugador)
print("La máquina eligió:", bot)

if jugador == bot:
    print("Empate")
elif (jugador == 1 and bot == 3) or \
    (jugador == 2 and bot == 1) or \
    (jugador == 3 and bot == 2):
    print("Has ganado")
else:
    print("Has perdido")