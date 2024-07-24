# Write a Python program that asks the user for the radius of a circle.
import math
from tkinter import Tk, simpledialog, messagebox

window = Tk()
window.withdraw
# Next, ask the user if they would like to calculate the area or circumference of a circle.
name = simpledialog.askstring(title='greeter', prompt="Would you rather calculate the area or the circumference of a circle ")
# If they choose area, display the area of the circle using the radius.
name1 = simpledialog.askfloat(title='greeter', prompt="whats the radius")
if name=="area":
    messagebox.showinfo(title='greeter', message=math.pi*name1*name1)
# Otherwise, display the circumference of the circle using the radius.
else:
    messagebox.showinfo(title='greeter',message=math.pi*2*name1)
#Area = πr^2
#Circumference = 2πr
