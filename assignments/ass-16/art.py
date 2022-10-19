#author yaz c


import turtle


import random


turtle.bgcolor("black")
pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.speed(0)
pen.hideturtle()

def draw_triangle(x,y,width,color):
    pen.color(color)
    pen.setpos(x,y)
    for i in range (3):
        
        pen.forward(width)  
        pen.left(120)


colores = ["pink","green","dodger blue","chartreuse","hot pink","lime green","orange","dark orange","spring green","blue violet","white","gray","steel blue"]


def draw_layered_triangle (x,y,size):
    pen.up()
    x=random.randint(-turtle.window_width()//2,turtle.window_width()//2)
    y=random.randint(-turtle.window_height()//2,turtle.window_height()//2)
    size -= random.randint(80,150)
    pen.down()
    
    for i in range (7):
        pen.up()
        pen.setpos(x,y)
        colorful = random.choice(colores)
        
        pen.down()
        
        draw_triangle(x,y,size,colorful)
        pen.up()
        size-= 20
        x+=10
        y+=5
         
    

for j in range (20):
    draw_layered_triangle(0,0,265)
    









turtle.done()





#triangle function and then special triangle loop decrease the x and y slightly (.1 ish)
#draw a house concept of calling other definitions