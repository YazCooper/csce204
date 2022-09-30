#author-yaz c

#author-yaz c


import turtle
import random

turtle.bgcolor("white")
turtle.setup(1600,800)

pen = turtle.Turtle()
pen.pensize(2)
pen.color("red")
pen.hideturtle()
pen.speed(0)



stripeh = turtle.window_height()//13
y=-turtle.window_height()//2


for i in range(7):
    
    pen.up()
    pen.setpos(-turtle.window_width()//2,y)
    pen.down()
    pen.setpos
    pen.begin_fill()
    for j in range (4):

        #OTHER METHOD if j % 2    #if j divides by 2 with no remainder e.g j is even
        if j == 0 or j == 2:
            pen.forward(turtle.window_width())
        else:
            pen.forward(stripeh)
        pen.left(90)
    pen.end_fill()
    y+=stripeh *2



turtle.done()
