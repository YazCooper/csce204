#author-yaz c

import turtle

turtle.bgcolor("medium purple")
pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.speed(0)
#pen.hideturtle()

def draw_square(x,y,width,color):
    #draw_rect(x,y,width,width,color) to draw a square in one line
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(0)
    pen.begin_fill()

    for i in range (4):
        pen.forward(width)
        pen.right(90)
    pen.end_fill()
    
def draw_triangle(x,y,width,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(0)
    pen.begin_fill()
    for i in range (3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()    
   
def draw_rect (x,y,width,height,color):

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(0)
    pen.begin_fill()
    for i in range (4):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

def draw_circle(x,y,radius,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    pen.setheading(0)
    for i in range (1):
        pen.circle(radius)
    pen.end_fill()


draw_triangle(0,-23,150,"hot pink")

draw_square(25,-25,100,"sky blue")

draw_rect(65,-125,20,50,"orange")

draw_circle(75,-15,30,"green")
turtle.done()


#for i in range (4)      to draw a rectangle i guess
#    if i % 2 == 0:
#        pen.forward(width)
#    else:
#        pen.forward(height)
#    pen.left(90)