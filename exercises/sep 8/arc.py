#author-yaz c.

import turtle
turtle.bgcolor("medium purple")

pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.speed(0)

arc_radius = 100 

pen.up()
pen.setpos(-arc_radius,0)
pen.down()

#happy smile
pen.setheading(-60)
pen.circle(arc_radius,120)

#frown
pen.up()
pen.setpos(0,0)
pen.down()
pen.setheading(60)
pen.circle(-arc_radius,120)







turtle.done()