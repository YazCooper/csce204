#Author:Yazmin Cooper
import turtle
pen = turtle.Turtle()   
pen.speed(0)
turtle.bgcolor("dim gray")

pen.setpos(0,-100)
pen.pensize(2)
pen.pencolor("black")

pen.begin_fill()
pen.fillcolor("dark orchid")
pen.circle(100)
pen.end_fill()

pen.up()
pen.setpos(-150,50)
pen.down()
pen.begin_fill()
pen.fillcolor("coral")
pen.forward(300)
pen.left(130)
pen.forward(230)
pen.left(100)
pen.forward(230)
pen.end_fill()
pen.up()
pen.setpos(40,120)
pen.down()
pen.setheading(0)

pen.begin_fill()
pen.circle(17)
pen.fillcolor("black")
pen.end_fill()



pen.begin_fill()
pen.circle(10)
pen.fillcolor("gold")
pen.end_fill()
pen.up()
pen.setpos(-40,120)
pen.down()

pen.begin_fill()
pen.circle(17)
pen.fillcolor("black")
pen.end_fill()


pen.begin_fill()
pen.circle(10)
pen.fillcolor("gold")
pen.end_fill()
pen.up()
pen.setpos(-25,100)
pen.down()

pen.begin_fill()
pen.fillcolor("dark orchid")
pen.forward(50)
pen.right(130)
pen.forward(40)
pen.right(100)
pen.forward(40)
pen.end_fill()


pen.up()
pen.setpos(-40,69)
pen.down()
pen.setheading(0)

pen.forward(80)
pen.up()
pen.setpos(-65,-110)
pen.down()

pen.begin_fill()
pen.circle(35)
pen.fillcolor("coral")
pen.end_fill()
pen.up()
pen.setpos(65,-110)
pen.down()

pen.begin_fill()
pen.fillcolor("coral")
pen.circle(35)
pen.end_fill()
pen.up()
pen.setpos(30,195)
pen.down()

pen.begin_fill()
pen.fillcolor("dark orchid")
pen.left(45)
pen.forward(45)
pen.setheading(0)
pen.left(270)
pen.forward(72)
pen.end_fill()
pen.up()
pen.setpos(-25,195)
pen.down()
pen.setheading(0)

pen.begin_fill()
pen.fillcolor("dark orchid")
pen.left(140)
pen.forward(45)
pen.setheading(0)
pen.left(270)
pen.forward(70)
pen.end_fill()

pen.hideturtle()



turtle.done()   