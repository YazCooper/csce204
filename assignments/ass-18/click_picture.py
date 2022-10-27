#author yaz c

import turtle
import random

turtle.setup(700,575)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)
turtle.bgcolor("cyan")
pen.up()
pen.setpos(-turtle.window_width(),-150)
pen.down()
pen.color("burlywood")
pen.begin_fill()
for i in range (2):
    pen.forward(600*2)
    pen.left(90)
    pen.forward(325)
    pen.left(90)
pen.end_fill()


def draw_stars(x,y):
    width=20
    draw_star(x,y,width*2)
    draw_eye(x-width*.17,y+width*.03,width/6)
    draw_eye(x+width*.37,y+width*.03,width/6)
    draw_smile(x-width*.2,y-width*.1,width*.5)



def draw_star(x,y,width):
    
    colors = ["white","magenta","orange red","hot pink","gold","medium purple","blue","red","orange","green" ]
    color = random.choice(colors)
    pen.color(color)
    pen.up()
    pen.setpos(x-width//2,y-width//2)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(x-width//2,y)
    pen.down()
    pen.setheading(0)
    pen.begin_fill()
    for j in range(3):
        pen.forward(width)
        pen.right(120)
    pen.end_fill()


def draw_smile(x,y,width):
    pen.up()
    pen.setpos(x-width*.5,y-width//2)
    pen.down()
    pen.color("black")
    pen.setheading(-60)
    pen.circle(width,120)
    pen.setheading(0)


def draw_eye(x,y,width):
    pen.up()
    pen.setpos(x-width*.5,y-width//2)
    pen.down()
    pen.color("black")
    pen.circle(width//2)

    




turtle.onscreenclick(draw_stars)
turtle.done()

#colors = ["white","magenta","orange red","hot pink","gold","medium purple","blue","red","orange","green" ]
#color = random.choice(colors)