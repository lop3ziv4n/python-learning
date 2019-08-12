# tkinter - Component text
import tkinter

root = tkinter.Tk()
root.title("My program")

# Text
text = tkinter.Text(root)
text.config(width=20, height=10, font=('Verdana', 15), padx=10, pady=10, fg='green', selectbackground='lightgrey')
text.pack()

root.mainloop()
