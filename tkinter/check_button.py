# tkinter - Component check button
import tkinter

root = tkinter.Tk()
root.title("My program")


# Check Button
def verified():
    value = check.get()
    if value == 1:
        print('El check esta activado')
    else:
        print('El check esta desactivado')


check = tkinter.IntVar()

checkbutton = tkinter.Checkbutton(root, text='Option 1', variable=check, onvalue=1, offvalue=0, command=verified)
checkbutton.pack()

root.mainloop()
