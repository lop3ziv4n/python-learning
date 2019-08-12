# tkinter - Component label
import tkinter

root = tkinter.Tk()
root.title("My program")

# Label
text = "Hello World!"
label = tkinter.Label(root, text=text)
label.config(fg='green', bg='lightgrey', font=('Cortana', 30))
label.pack()

root.mainloop()
