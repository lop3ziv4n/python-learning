# try ... except ... else ... finally

try:
    number1 = 5
    number2 = 0
    div = number1 / number2
    print(div)
except:
    print("Error")

try:
    number1 = 5
    number2 = 0
    div = number1 / number2
    print(div)
except ZeroDivisionError:
    print("Error: No dividir por 0")

try:
    number1 = 5
    number2 = 2
    div = number1 / number2
    print(div)
except ZeroDivisionError:
    print("Error: No dividir por 0")
except:
    print("Error")
else:
    print("La division funciono correctamente")

try:
    number1 = 5
    number2 = 0
    div = number1 / number2
    print(div)
except ZeroDivisionError:
    print("Error: No dividir por 0")
finally:
    print("Esta prueba del try terminó")
