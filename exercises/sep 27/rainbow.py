#author-yaz c


import turtle
import random

pen = turtle.Turtle()
pen.pensize(2)
pen.color("gold")
pen.hideturtle()
pen.speed(0)
turtle.bgcolor("black")

colors = ("red","orange","yellow","green","blue","indigo","violet" )

radius = turtle.window_width()//6
x=0
y=0

for color in colors:
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(60)
    pen.circle(-radius,120)
    y+=2  #spacing









turtle.done()
