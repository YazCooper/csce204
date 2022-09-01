#Author: Yazmin Cooper
import turtle

turtle.bgcolor("medium purple")
pen = turtle.Turtle()
pen.pensize(2)
pen.color("gold")
pen.speed(0)

scale= turtle.numinput("Snowman","Size (1-5)","",1,5) #name of window, input asked for, default, min, max

ldiameter = turtle.window_height()//9 * scale
mdiameter = ldiameter * 2 // 3
sdiameter = mdiameter * 2//3 

#draw large snowball with white fill
pen.up()
pen.setpos(0,-ldiameter)
pen.down()
pen.begin_fill()
pen.fillcolor("white")
pen.circle(ldiameter//2)
pen.end_fill()


#draw medium white filled snowball
pen.up()
pen.setpos(0,0)
pen.down()
pen.begin_fill()
pen.fillcolor("white")
pen.circle(mdiameter//2)
pen.end_fill()


#draw small white filled snowball
pen.up()
pen.setpos(0,mdiameter)
pen.down()
pen.begin_fill()
pen.fillcolor("white")
pen.circle(sdiameter//2)
pen.end_fill()


turtle.done()