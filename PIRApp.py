from tkinter import *


def command1(event):
    if entry1.get() == 'aut' and entry2.get() == 'pass':
        root.deiconify  # Shows main screen aka root
        top.destroy()  # removes login screen aka top


def command2():
    top.destroy()
    root.destroy()
    sys.exit()


# Main Screen
root = Tk()

# Login Screen
top = Toplevel()

top.geometry('300x330')
top.title('LOGIN SCREEN')
top.configure(background='white')
photo2 = PhotoImage(file='autlogo.png')
photo = Label(top, image=photo2, bg='white')
lbl1 = Label(top, text='Username:', font=('Helvetica', 10))
entry1 = Entry(top)
lbl2 = Label(top, text='Password', font=('Helvetica', 10))
entry2 = Entry(top, show="*")
button2 = Button(top, text='Cancel', command=lambda: command2())

entry2.bind('<Return>', command1)

lbl3 = Label(top, text='Copyright AUT 2020 ya bish', font=('Arial', 9))

# Ordering the elements
photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()

root.title('PIR Project - Main')
root.configure(background='white')
root.geometry('855x650')

root.withdraw()
root.mainloop()
