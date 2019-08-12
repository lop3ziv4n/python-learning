# tkinter - Component entry
import tkinter

root = tkinter.Tk()
root.title("My program")

# Entry
entry = tkinter.Entry(root)
entry.config(justify='center')
# password entry.config(justify='center', show='*')
entry.pack()

root.mainloop()
