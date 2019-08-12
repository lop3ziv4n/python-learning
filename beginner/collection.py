# List
colors = ["rojo", "amarillo", "verde"]
print(colors[0])

colors[1] = "azul"
print(colors[1])

print(len(colors))

colors.append("naranja")
print(colors)

colors.remove("rojo")
print(colors)

for color in colors:
    print(color)

colors.clear()
print(colors)

# Tuple it is immutable it can not be added or deleted
tuple_colors = ("rojo", "verde", "amarillo")

for tuple_color in tuple_colors:
    print(tuple_color)

print(tuple_colors[2])

print(len(tuple_colors))

# Set
set_colors = {"rojo", "verde", "amarillo"}
print(set_colors)

for set_color in set_colors:
    print(set_color)

# set_colors[0] can not be accessed by position

print(len(tuple_colors))

set_colors.add("negro")
print(set_colors)

set_colors.remove("verde")
print(set_colors)

# dictionary
dictionary_colors = {"red": "rojo", "blue": "azul", "yellow": "amarillo"}
print(dictionary_colors)

print(dictionary_colors["red"])
print(dictionary_colors["yellow"])

dictionary_colors["black"] = "negro"
print(dictionary_colors)

dictionary_colors.pop("yellow")
print(dictionary_colors)

del (dictionary_colors["black"])
print(dictionary_colors)

for dictionary_color in dictionary_colors:
    print(dictionary_color)

for key, value in dictionary_colors.items():
    print(key, value)
