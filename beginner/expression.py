# Regular expression (search, findall, split, sub)
import re
import operator

# Search
text = "Hola, mi nombre es Jorge Cas"
result = re.search("nombre", text)
print(result)

result = re.search("adios", text)
print(result)

result = re.search("nombre", text)
if result:
    print("Cadena encontrada")
else:
    print("Cadena no encontrada")

# init
result = re.search("´Hola", text)
print(result)

# content
result = re.search("mi.*es", text)
print(result)

# findall
text = """
El auto de Luis es rojo,
el auto de Antonio es blanco,
y el auto de Maria es rojo 
"""

result = re.findall("auto.*rojo", text)
print(result)

# split
text = "La silla es blanca y vale 80"
result = re.split("\s", text)
print(result)

# sub
text = "La silla es blanca y vale 80"
result = re.sub("blanca", "roja", text)
print(result)