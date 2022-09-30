#author-Yaz C

import turtle
import random

pen = turtle.Turtle()
pen.pensize(2)
pen.color("gold")
pen.hideturtle()
pen.speed(0)
turtle.bgcolor("black")

colors = ["white","magenta","orange red","hot pink","gold","medium purple" ]


#draw multiple stars
for i in range (25):
    
    x=random.randint(-turtle.window_width()//2,turtle.window_width()//2)
    y=random.randint(-turtle.window_height()//2,turtle.window_height()//2)
    width = random.randint(25,100)
    pen.up()
    pen.setpos(x-width//2,y-width//2)
    pen.down()
    star_color=random.choice(colors)
    pen.color(star_color)
    #  draw rightside up triangle
    pen.begin_fill()
    for j in range (3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(x-width//2,y)
    pen.down()
    pen.setheading(0)


    #draw upside down triangle
    pen.begin_fill()

    for j in range (3):
        pen.forward(width)
        pen.right(120)
    pen.end_fill()

 


turtle.done()