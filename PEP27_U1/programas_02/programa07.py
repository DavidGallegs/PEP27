minutos = int(input("Introduce una cantidad de minutos: "))

horas = minutos // 60
minutosR = minutos - (horas * 60)
print(minutosR)
if minutosR <= 0:
    print("Los minutos introducidos son: ",horas,"h")
else:
    print("Los minutos introducidos son: ",horas,"h y ",minutosR,"min")