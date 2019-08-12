# tkinter - Component message box
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("My program")


# Message Box
def popup_info():
    tkinter.messagebox.showinfo('Title information', 'Message information')


button1 = tkinter.Button(root, text='Pulsar para popup (Info)', command=popup_info)
button1.pack()


# Message Box
def popup_question():
    question = tkinter.messagebox.askquestion('Title question', 'Quieres borrar este fichero?')
    if question == 'yes':
        print('Si, quiero borrar el fichero')
    else:
        print('No, no quiero borrar el fichero')


button2 = tkinter.Button(root, text='Pulsar para popup (Question)', command=popup_question)
button2.pack()

root.mainloop()
