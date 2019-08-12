# tkinter - Component button
import tkinter

root = tkinter.Tk()
root.title("My program")

# Button
text = "Execute"


def action():
    print('Hello World!')


button = tkinter.Button(root, text=text, command=action)
button.config(fg='green', bg='lightgrey', font=('Cortana', 10))
button.pack()

root.mainloop()
