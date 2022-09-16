#author-yaz c

import turtle

pen = turtle.Turtle()
pen.pensize(2)
pen.color("black")
pen.hideturtle()
pen.speed(0)

sq = 50


pen.up()
pen.down()

for i in range (sq):
    pen.forward(sq)
    pen.left(90)
pen.up()



turtle.done()