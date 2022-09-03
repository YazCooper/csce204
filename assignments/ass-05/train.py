#author: yazmin cooper

import turtle

turtle.bgcolor("medium purple")

pen = turtle.Turtle()
pen.pensize(2)
pen.color("gold")
pen.speed(0)

scale= turtle.numinput("Train","Size (1-10)","",1,10)

width1 = turtle.window_width()//45*scale
height1 = width1 * 1.2
height2 = height1 // 1.5
lwheel = width1 //8
bwheel = width1 // 4

pen.up()
pen.setpos(-width1, 0)
pen.down()
pen.begin_fill()
pen.fillcolor("deep pink")
pen.forward(width1)
pen.left(90)
pen.forward(height1)
pen.left(90)
pen.forward(width1)
pen.left(90)
pen.forward(height1)
pen.end_fill()


pen.up()
pen.setpos(0,0)
pen.down()
pen.begin_fill()
pen.fillcolor("deep pink")
pen.setheading(0)
pen.forward(height1)
pen.left(90)
pen.forward(height2)
pen.left(90)
pen.forward(height1)
pen.end_fill()
pen.up()
pen.setpos(-height1,height1)
pen.down()

pen.begin_fill()
pen.fillcolor("deep pink")
pen.setheading(0)
pen.forward(width1 * 1.5)
pen.left(90)
pen.forward(width1//6)
pen.left(90)
pen.forward(width1* 1.5)
pen.left(90)
pen.forward(width1//6)
pen.end_fill()

pen.up()
pen.setheading(0)
pen.setpos(-width1 * .9, height2)
pen.down()

pen.begin_fill()
pen.fillcolor("medium purple")
pen.forward(height2)
pen.left(90)
pen.forward(width1//3)
pen.left(90)
pen.forward(height2)
pen.left(90)
pen.forward(width1//3)
pen.end_fill()

pen.up()
pen.setheading(0)
pen.setpos(-width1 * .9, -width1*.2)
pen.down()

pen.begin_fill()
pen.fillcolor("black")
pen.circle(bwheel)
pen.end_fill()

pen.up()
pen.setheading(0)
pen.setpos(-width1 * .2, -width1*.2)
pen.down()

pen.begin_fill()
pen.fillcolor("black")
pen.circle(bwheel)
pen.end_fill()

pen.up()
pen.setheading(0)
pen.setpos(width1//1.5,-width1*.1)
pen.down()

pen.begin_fill()
pen.fillcolor("black")
pen.circle(lwheel)
pen.end_fill()

pen.up()
pen.setpos(width1,-width1*.1)
pen.down()

pen.begin_fill()
pen.fillcolor("black")
pen.circle(lwheel)
pen.end_fill()












turtle.done()


