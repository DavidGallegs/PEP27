import math

#Operaciones
def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error. NO se puede dividir entre 0")

#Figuras

def area_rectangulo(base ,altura):
    return base* altura

def area_triangulo(base ,altura):
    return base*altura/2

def area_circulo(radio):
    return math.pi*(radio**2)

#Conversion binario

def a_binario(numero):
    return bin(numero)[2:]

def a_hexadecimal(numero):
    return hex(numero)[2:]

def a_octal(numero):
    return oct(numero)[2:]