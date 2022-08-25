#Author: Yazmin Cooper
import turtle
turtle.bgcolor("medium purple")

pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")

pen.setpos(-50,0)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.up()
pen.setpos(-60,100)
pen.down()

pen.setheading(0)
pen.forward(120)
pen.left(120)
pen.forward(120)
pen.left(120)
pen.forward(120)
pen.up()
pen.setpos(10,0)
pen.setheading(0)
pen.down()
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(25)
pen.left(90)
pen.forward(50)
pen.up()
pen.setpos(5,25)
pen.down()
pen.circle(2)
pen.hideturtle()
turtle.done()