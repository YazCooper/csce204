#author-yaz c


import turtle
import random

pen = turtle.Turtle()
pen.pensize(2)
pen.color("gold")
pen.hideturtle()
pen.speed(0)
turtle.bgcolor("black")

def draw_smiley_face(x,y):
    width=50
    draw_circle(x,y,width,"yellow")
    draw_circle(x-width*.2,y+width*.05,width/6,"black")
    draw_circle(x+width*.2,y+width*.05,width/6,"black")
    draw_smile(x,y-width*.3,width*.5,"black")
#draw a filled in circle
def draw_circle(x,y,width,color):
    pen.color(color)
    pen.up()
    pen.setpos(x,y-width/2)
    pen.down()
    pen.begin_fill()
    pen.circle(width//2)
    pen.end_fill()

#def draw_eyes(x,y,width):
#    pen.up()
#    pen.setpos(x,y - width/2)
#    pen.down()
#    pen.color("black")
#    pen.begin_fill()
#    pen.circle(width//2)
#    pen.end_fill()
#VERY SIMILAR SO WE REFACTOR AND GOT RID OF THIS

def draw_smile(x,y,width,color):

    rand_num=random.randint(0,1)
    if (rand_num==0):                           #TO MAKE THE FACES CHANGE RANDOMLY
        pen.up()
        pen.setpos(x-width*.9,y+width//3)
        pen.setheading(-60)
        pen.down()
        pen.color(color)
        pen.circle(width,120)
        pen.setheading(0)
    else:
        pen.up()
        pen.setpos(x+width*.7,y-width*.2)
        pen.down()
        pen.color(color)
        pen.setheading(120)
        pen.circle(width*.8,120)
        pen.setheading(0)

    

turtle.onscreenclick(draw_smiley_face)

















turtle.done()