from tkinter import *
# pack, place, grid


# button
def button_clicked():
    print("I am clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())


window = Tk()
window.title("My First GUI")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)


# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# my_label["text"] = "New Text"
# my_label.config(text="Hallo")

# button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


# entry
input = Entry(width=20)
# input.pack()
input.grid(column=2, row=2)
window.mainloop()
