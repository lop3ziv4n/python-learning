# tkinter - Component fame
import tkinter

root = tkinter.Tk()
root.title("My program")

# Frame
frame = tkinter.Frame(root)
frame.config(bg='blue', width=400, height=300)
frame.pack()

root.mainloop()
