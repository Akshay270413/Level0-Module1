from tkinter import Tk, simpledialog, messagebox

window = Tk()
window.withdraw()
name = simpledialog.askinteger(title='greeter', prompt="pick one random number")
name1 = simpledialog.askinteger(title='greeter', prompt="pick another random number")
name2 = simpledialog.askstring(title='greeter', prompt="would you like to +,-,*,or /")
if name2=="+":
    messagebox.showinfo(title='greeter', message=name+name1)
if name2=="-":
    messagebox.showinfo(title='greeter', message=name-name1)
if name2=="*":
    messagebox.showinfo(title='greeter', message=name*name1)
if name2=="/":
    messagebox.showinfo(title='greeter', message=name/name1)
else:
    messagebox.showinfo(title='greeter', message="Unavailable")
"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""