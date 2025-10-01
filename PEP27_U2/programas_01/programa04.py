num = int(input("Introduce un número [0-10]: "))

match num:
    case 0|1|2|3|4:
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6|7:
        print("Bien")
    case 7|8:
        print("Notable")
    case 9|10:
        print("Sobresaliente")