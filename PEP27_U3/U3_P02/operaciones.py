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