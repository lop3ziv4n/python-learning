# tkinter - Component filedialog
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.title("My program")


# Filedialog
def open_file():
    path = filedialog.askopenfilename(title='Open file')
    print(path)


button = tkinter.Button(root, text='Pulsar para empezar', command=open_file)
button.pack()

root.mainloop()
