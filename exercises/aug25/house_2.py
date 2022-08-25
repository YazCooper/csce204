#Author: Yamzin Cooper
import turtle
turtle.bgcolor("white")

house_size = 100
pen = turtle.Turtle()
pen.pensize(2)
pen.up()
pen.setpos(-house_size//2, -house_size//2)
pen.down()
pen.color("grey")


pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.setheading(0)


pen.up()
pen.setpos(-house_size*.6 , house_size//2)
pen.down()
pen.forward(house_size * 1.2)
pen.left(120)
pen.forward(house_size * 1.2)
pen.left(120)
pen.forward(house_size * 1.2)
pen.left(120)


turtle.done()