horas = int(input("Introduce la hora de salida: "))
minutos = int(input("Introduce los minutos de salida: "))
segundos = int(input("Introduce los segundos de salida: "))


viaje = int(input("Introduce el tiempo de viaje en segundos: "))

# Convertir la hora de salida a segundos
segundos_salida = horas * 3600 + minutos * 60 + segundos

# Calcular la hora de llegada en segundos
segundos_llegada = segundos_salida + viaje

# Convertir de nuevo a horas, minutos y segundos
horaLlegada = (segundos_llegada // 3600) % 24  # %24 por si pasa de medianoche
minutoLlegada = (segundos_llegada % 3600) // 60
segundoLlegada = segundos_llegada % 60

# Mostrar resultado
print("Llega a las ",horaLlegada,"h con ",minutoLlegada,"minutos y",segundoLlegada,"s")
