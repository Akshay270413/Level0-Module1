import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_dog8 = turtle.Turtle()
    my_dog8.shape("turtle")
    # Ask the user what shape they want to draw and store it in a variable
    name = simpledialog.askstring(title='greeter', prompt="what shape to you want to draw,circle,square,triangle")
    # Draw the shape requested by the user using if-elif-else statements
    if name== "circle":
        my_dog8.circle(1000)
    elif name== "square":
        for i in range(4):
            my_dog8.forward(90)
            my_dog8.left(90)
    else:
        for i in range(3):
            my_dog8.forward(90)
            my_dog8.left(120)
    # Call the turtle .done() method
    turtle.done()
