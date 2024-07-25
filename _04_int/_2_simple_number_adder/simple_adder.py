from tkinter import Tk, simpledialog, messagebox

window = Tk()
window.withdraw()
name = simpledialog.askinteger(title='greeter', prompt="pick one random numbers")
name1 = simpledialog.askinteger(title='greeter', prompt="pick another random numbers")
messagebox.showinfo(title='greeter', message=name+name1)

"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""