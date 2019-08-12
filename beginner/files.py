# Read
# rt -> read and text
file = open("files/file_read_text_example.txt", "rt")
read = file.read()

print(read)

# Write
# wt -> write and text
file = open("files/file_write_text_example.txt", "wt")
data_text = "Hola, esta es una linea para grabar en el archivo de texto"
file.write(data_text)
file.close()

# Append Text
# at -> append and text
file = open("files/file_read_text_example.txt", "at")
data_text = "\nEsta es la tercera fila del archivo"
file.write(data_text)
file.close()

# Delete
import os

os.remove("files/file_remove_test_example.txt")
