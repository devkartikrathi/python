from tkinter import *

window = Tk()
window.title("My first GUI")

def change_text():
    new_text = input.get()
    label.config(text=new_text)

label = Label(text="This text can be changed by the click of a button", font=("Arial", 15, "bold"))
label.pack()

input = Entry(width=15)
input.insert(END, "Type new text")
input.pack()

button = Button(text="Change text", command=change_text)
button.pack()

window.mainloop()