from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=250, height=200)
window.config(padx=50, pady=50)

label = Label(text="is equal to")
label.grid(column=1, row=2)

entry = Entry(width=10)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=2, row=1)

labelM = Label(text="Miles")
labelM.grid(column=3, row=1)

labelAns = Label(text="0")
labelAns.grid(column=2, row=2)

labelK = Label(text="Km")
labelK.grid(column=3, row=2)

def calculate():
    miles = float(entry.get())
    km = miles * 1.60934
    labelAns.config(text=km)
    
button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

window.mainloop()

