#1.Crear variable
num1 = 7

#2.Visualización
print(num1, "su tipo de dato es: ", type(num1))

#3.Asignación
num2 = num1

#4.Visualización 2
print("\n")
print(num1, "su tipo de dato es: ", type(num1))
print(num2, "su tipo de dato es: ", type(num2))

#5. is /is not
print("\n")
print("Is: ", num1 is num2) #true
print("Is not: ", num1 is not num2)#False

#6. Reasginación a num1
num1 = "Hola"
print("\n")
print(num1, "su tipo de dato es: ", type(num1)) #str
print(num2, "su tipo de dato es: ", type(num2)) #int

#7. is /is not
print("\n")
print("Is: ", num1 is num2) #False
print("Is not: ", num1 is not num2)#True