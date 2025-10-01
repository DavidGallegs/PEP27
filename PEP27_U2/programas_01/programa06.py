dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

valida = True

if mes in (1, 3, 5, 7, 8, 10, 12):
    if dia < 1 or dia > 31:
        valida = False

elif mes == 2:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        if dia < 1 or dia > 29:
            valida = False
    else:
        if dia < 1 or dia > 28:
            valida = False

# Mes con 30 días
elif mes in (4, 6, 9, 11):
    if dia < 1 or dia > 30:
        valida = False

else:
    valida = False  

if valida: #True
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")
