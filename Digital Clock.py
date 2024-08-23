                        #   InternPe -----------> Task 02

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

time()
root.mainloop()
