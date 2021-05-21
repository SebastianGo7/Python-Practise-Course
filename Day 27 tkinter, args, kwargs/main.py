from tkinter import *


def button_clicked():
    miles_input_number = float(miles_input.get())
    km_output = round((miles_input_number * 1.60934), 2)
    km_output_label.config(text=km_output)
    km_output_label.grid(column=2, row=1)


window = Tk()
window.title("My distance converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


# Labels for miles, km and is equal to
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=3, row=0)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=3, row=1)

equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=1, row=1)

km_output_label = Label(text="0", font=("Arial", 24, "bold"))
km_output_label.grid(column=2, row=1)

button = Button(text="Calculate", font=("Arial", 24, "bold"), command=button_clicked)
button.grid(column=2, row=3)

# Entry of miles which should be converted
miles_input = Entry(width="10")
miles_input.grid(column=2, row=0)


window.mainloop()
