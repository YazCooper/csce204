#author-Yaz c

import turtle
import random

pen = turtle.Turtle()
pen.pensize(2)
pen.color("black")
pen.hideturtle()
pen.speed(0)
turtle.colormode(255)  #color range/type of color this much red/green/blue
style = ("Arial", 30)    #(Arial,30,Normal)  Not sure about the normal part
 
#ask the user for their name

name = turtle.textinput("Name Program", "What is your name?: ")


#ask how many times they want to see thier name
many = int(turtle.numinput("Name Program","How many times would you like to see your name?: ",10,1,100))


#loop through and display their name the given number of times
#make the names go in random spots on screen
#make the names have random colors
for i in range (int(many)):
    x = random.randint(-turtle.window_width()//2,turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2,turtle.window_height()//2)
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    pen.color(r,g,b)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write(name, font = (style) )









turtle.done()