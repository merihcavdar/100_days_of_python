from tkinter import *


def miles_to_km():
    km = round(float(mile_input.get()) * 1.6)
    result_label.config(text=str(f"{km}"))


window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

ex_label = Label(text="is equal to ")
ex_label.grid(column=0, row=1)


mile_input = Entry(width=10, font=("Arial", 12, "bold"))
mile_input.grid(column=1, row=0)


mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)


result_label = Label(text="")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

cal_button = Button(text="Calculate", command=miles_to_km)
cal_button.grid(column=1, row=3)


window.mainloop()
