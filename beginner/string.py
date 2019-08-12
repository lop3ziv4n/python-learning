# String
string = "Hola Mundo"
# left
print(string[6])
# right
print(string[-1])

print(string[2:7])
print(string[2:])

# length
print(len(string))
# upper
print(string.upper())
# lower
print(string.lower())
# split
print(string.split())
string2 = "uva,pera,manzana,naranja"
print(string2.split(","))

# printing
string = "Mundo"
print("Hola " + string)

name = "Jorge"
date = 18
print("Buen Dia {}, feliz {} años".format(name, date))

result = 10/3
print("El resultado es: {r}".format(r=result))
print("El resultado es: {r:1.3f}".format(r=result))

name = "Marcos"
surname = "Perez"
print(f"Su nombre {name} y apellido {surname} no son conocidos")

# input
print("Ingrese un nombre")
name = input()
print("Hola " + name)
