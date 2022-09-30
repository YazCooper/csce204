#author-yaz c


import turtle
import random

turtle.colormode(255)


turtle.bgcolor("white")


pen = turtle.Turtle()
pen.pensize(2)
pen.color("black")
#pen.hideturtle()
pen.speed(0)
pen.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))

x=0
y=turtle.window_height()//13
spaces = turtle.window_width()//10

lst = []

#store the letters in a list
colors = ("red","orange","yellow","green","blue","indigo","violet" )


while True:
    
    letters = turtle.numinput("Letters","Enter Number of Letters: ","",1,26)

    if letters is None:break
    

    for i in range (int(letters)):
        enter = turtle.textinput("Letters","Enter Letter: ").upper()
        lst.append(enter)
        if enter is None:
            break
    
    

    if len(lst) > 0:
        for i in range (len(lst)):
            rcolor=random.choice(colors)
            pen.fillcolor(rcolor)
            pen.up()
            pen.setpos(-turtle.window_width()//2 +x,y)

            pen.forward(spaces)
            pen.down()
            pen.setheading(0)
            pen.begin_fill()
            for j in range (4):
                pen.fillcolor(rcolor)
                pen.forward(100)
                pen.left(90)
                x+= 40
                
            pen.end_fill()
            pen.up()
            pen.setpos(-turtle.window_width()//1.81+x,y+45)
            pen.down()
         
            pen.color("Black")
            pen.write(lst[i%len(lst)], font=[20,])
            
            #x+=20
        pen.up()
    else:
        break

        




  












turtle.done()