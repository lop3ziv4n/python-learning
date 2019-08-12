# Conditional {if, elif, else}
a = 8
b = 4

if a > b:
    print("a es mayor que b")

a = 8
b = 4
c = 2
d = 6

if (a > c) and (b < d):
    print("la primera expresion es correcta")

if (a > c) and (b > d):
    print("la primera expresion es correcta")
else:
    print("la primera expresion NO es correcta")

if a > b:
    print("a es mayor a b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor a b")

# Loop {for}
colors = ["rojo", "verde", "azul"]
for color in colors:
    print(color)

strings = "Hola Mundo"
for char in strings:
    print(char)

print(range(8))
for number in range(8):
    print(number)

for number in range(3, 8):
    print(number)
# range init, end, range
for number in range(3, 8, 2):
    print(number)

# break - stop loop
for number in range(10):
    if number == 5:
        break
    print(number)

# continue - stop thread loop
for number in range(10):
    if number == 6:
        break
    print(number)

# for double
for number1 in range(4):
    for number2 in range(3):
        print(number1, number2)

# Loop while
value = 1
end = 10
while value < end:
    print(value)
    value += 1

# break - stop loop
value = 1
end = 10
while value < end:
    print(value)
    value += 1
    if value == 5:
        break

# continue - stop thread loop
value = 1
end = 10
while value < end:
    value += 1
    if value == 6:
        continue
    print(value)
