import random

jugadores = int(input("¿Total Jugadores? : "))
banca = random.randint(17, 21)
print(f"La banca tiene {banca} puntos.\n")

for j in range(1, jugadores + 1):
    print(f"--- Jugador {j} ---")
    puntuacion = 0
    while True:
        carta = random.randint(1, 5)
        puntuacion += carta
        print(f"Has sacado un {carta}. Total: {puntuacion}")

        if puntuacion > 21:
            print("Te pasaste de 21. Pierdes.")
            break

        continuar = input("¿Quieres sacar otra carta? (s/n): ")
        if continuar.lower() != "s":
            break

    if puntuacion <= 21:
        if puntuacion > banca:
            print("🎉 ¡Has ganado a la banca!\n")
        else:
            print("La banca gana.\n")

print("Juego terminado.")