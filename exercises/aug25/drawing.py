#Author: Yazmin Cooper
import turtle
turtle.bgcolor("medium purple")

pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.hideturtle() #hides the cursor

#drawing a square
pen.begin_fill()
pen.forward(100)
pen.left(90)
pen.forward(100)  
pen.left(90)
pen.forward(100)  
pen.left(90)
pen.forward(100)
pen.end_fill()

pen.up()
pen.setpos(200,75)
pen.down()

pen.color("black")
pen.setheading(0)

pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)
pen.forward(100)





turtle.done()  #must be the last line of the file.