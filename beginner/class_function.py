# Class Object - POO
class ClassChair:
    color = "blanco"
    price = 100


classChair = ClassChair()
print(classChair.color)
print(classChair.price)

classChair = ClassChair()
classChair.color = "verde"
classChair.price = 120
print(classChair.color)
print(classChair.price)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("hola, me llamo {} y tengo {} años".format(self.name, self.age))


person = Person("Juan", 35)
print(person.name)
print(person.age)
person.hello()


# Function
def hello():
    print("Buenos Dias")


hello()


def hello(name):
    print("Buenos Dias " + name)


hello("Jorge")


def add(number1, number2):
    return number1 + number2


print(add(5, 3))

# params reference
colors = ["rojo", "verde", "azul"]


def add_color(colors, color):
    colors.append(color)


color = "negro"
add_color(colors, color)

print(colors)

# Function Lambda

result = lambda number: number + 30

print(result(10))

result1 = lambda number1, number2: number1 + number2

print(result1(5, 8))
