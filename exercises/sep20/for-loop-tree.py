#author-yazmin cooper

import turtle

pen = turtle.Turtle()
pen.pensize(2)
pen.color("black")
pen.hideturtle()
pen.speed(0)
turtle.bgcolor("medium purple")


shpwidth=turtle.window_width()//36
botwidth = shpwidth*3
midwidth = botwidth * 2/3
topwidth = midwidth * 2/3


pen.up()
pen.setpos(-shpwidth//2,-shpwidth)
pen.down()
pen.begin_fill()
pen.fillcolor("brown")
for i in range(4):
    pen.forward(shpwidth)
    pen.left(90)  
pen.end_fill()  
pen.up()

pen.setpos(-botwidth//2,0)

pen.down()
pen.begin_fill()
pen.fillcolor("green")
for i in range(3):
    pen.forward(botwidth)
    pen.left(120)
pen.end_fill()
pen.up()

pen.setpos(-midwidth//2,botwidth//2)

pen.down()
pen.begin_fill()
for i in range (3):
    pen.forward(midwidth)
    pen.left(120)
pen.end_fill()
pen.up()

pen.setpos(-topwidth//2,midwidth*1.3)

pen.down()
pen.begin_fill()

for i in range (3):
    pen.forward(topwidth)
    pen.left(120)
pen.end_fill()    


pen.up()
pen.setpos(-5,-5)
pen.down()

#for i in range (5):
 #   pen.forward(100)
  #  pen.right(144)
















turtle.done()