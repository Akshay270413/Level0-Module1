from tkinter import Tk, simpledialog, messagebox

window = Tk()
window.withdraw()
name = simpledialog.askstring(title='greeter', prompt="Mr and Mrs mustard had 5 daughters. Each daughter had 1 brother. how many people are in the mustard family?")
if name== "9":
    messagebox.showinfo(title='greeter', message="nice job")
else:
    messagebox.showinfo(title='greeter', message="Wrong")
name1 = simpledialog.askstring(title='greeter', prompt="Next Riddle... What has 6 faces but does not wear makeup, has 21 eyes but cant see. ")
if name1== "Dice":
    messagebox.showinfo(title='greeter', message="nice job")
else:
    messagebox.showinfo(title='greeter', message="Wrong")
name2 = simpledialog.askstring(title='greeter', prompt="Always in you,Sometimes on you;If I surround you, I can kill you")
if name2== "water":
    messagebox.showinfo(title='greeter', message="nice job")
else:
    messagebox.showinfo(title='greeter', message="Wrong")
"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
