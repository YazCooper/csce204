#author-yaz cooper

import turtle
turtle.bgcolor("medium purple")

pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.speed(0)

shape = turtle.textinput("Shapes","Enter Shape").lower().strip()
shape_size = turtle.window_width()//6






if shape == "circle":
    pen.up()
    pen.setpos(0, -shape_size//2)
    pen.down()
    pen.circle(shape_size//2)
elif shape == "square":
    pen.up()
    pen.setpos(-shape_size//2,0)
    pen.down()
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
elif shape == "triangle":
    pen.up()
    pen.setpos(-shape_size//3,0)
    pen.down()
    pen.forward(shape_size//3)
    pen.left(120)
    pen.forward(shape_size//3)
    pen.left(120)
    pen.forward(shape_size//3)













turtle.done()