from tkinter import Tk, simpledialog, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(title='greeter', prompt="when is your birthday")
    if name=="7/24":
        messagebox.showinfo(title='greeter', message="Happy Birthday!")
    else:
        messagebox.showinfo(title='greeter', message="Happy unbirthday")
