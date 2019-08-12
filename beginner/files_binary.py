# Write
# pickle - Module for write binary file
import pickle

colors = ["azul", "verde", "rojo", "amarillo"]
# wb -> write and binary
file = open("files/file_write_binary_example.pckl", "wb")
pickle.dump(colors, file)
file.close()

# Read
# pickle - Module for write binary file
import pickle

# rb -> read and binary
file = open("files/file_write_binary_example.pckl", "rb")

read = pickle.load(file)
print(read)
