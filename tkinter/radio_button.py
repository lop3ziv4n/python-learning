# tkinter - Component radio button
import tkinter

root = tkinter.Tk()
root.title("My program")


# Radio Button
def selected():
    print('La opción seleccionada es {}'.format(option.get()))


option = tkinter.IntVar()

radiobutton = tkinter.Radiobutton(root, text='Option 1', variable=option, value=1, command=selected)
radiobutton.pack()

radiobutton1 = tkinter.Radiobutton(root, text='Option 2', variable=option, value=2, command=selected)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(root, text='Option 3', variable=option, value=3, command=selected)
radiobutton2.pack()

root.mainloop()
