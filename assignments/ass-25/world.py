#author-yaz c

import turtle
import random
from monster import Monster

turtle.bgcolor("blue")

pen = turtle.Turtle()
pen.pensize(2)
#pen.color("white")
#pen.hideturtle()
pen.speed(0)




for i in range(10):
    colors = ["yellow","magenta","orange red","hot pink","gold","medium purple","pink","red","orange","green" ]
    color = random.choice(colors)
    
    x=random.randint(-turtle.window_width()//4,turtle.window_width()//2)


    y=random.randint(-turtle.window_height()//4,turtle.window_height()//2)
    width = random.randint(100,300)
    monster = Monster(x,y,width,color)

    monster.draw(pen)
    
turtle.done()