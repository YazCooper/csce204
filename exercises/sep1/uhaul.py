#author:yazmin cooper
import turtle
turtle.bgcolor("medium purple")

pen = turtle.Turtle()
pen.pensize(2)
pen.color("gold")
pen.speed(0)

scale= turtle.numinput("U-Haul","Size (1-10)","",1,10) #name of window, input asked for, default, min, max

width = turtle.window_width()//12*scale
height = width//3
cheight = height //2
cwidth = width//6
dwheel = width //4


pen.up()
pen.setpos(-width // 2, 0)
pen.down()
pen.begin_fill()
pen.fillcolor("red")
pen.forward(width)
pen.setheading(0)
pen.left(90)
pen.forward(cheight)
pen.left(90)
pen.forward(cwidth)
pen.right(90)
pen.forward(height - cwidth)
pen.left(90)
pen.forward(width-cwidth)
pen.left(90)
pen.forward(height)
pen.end_fill()

#set pos for left wheel
pen.setheading(0)
pen.up()
pen.setpos(-width//4 , -dwheel//2)
pen.down()


#draw left
pen.color("black")
pen.begin_fill()
pen.circle(dwheel//2)
pen.end_fill()


#set right pos
pen.setheading(0)
pen.up()
pen.setpos(width//4 , -dwheel//2)
pen.down()


#draw right
pen.color("black")
pen.begin_fill()
pen.circle(dwheel//2)
pen.end_fill()


turtle.done()