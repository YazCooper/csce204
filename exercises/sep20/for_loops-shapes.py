#author-yaz c

import turtle

pen = turtle.Turtle()
pen.pensize(2)
pen.color("black")
pen.hideturtle()
pen.speed(0)


shp=turtle.textinput("Shape", "Enter Shape").lower().strip()
shpwd = turtle.window_width()//5

if shp == "circle":
    pen.begin_fill()
    pen.fillcolor("medium purple")
    pen.up()
    pen.setx(0)
    pen.down()
    pen.circle(shpwd//2)
    pen.end_fill()
elif shp == "square":
    pen.begin_fill()
    pen.fillcolor("orange")
    for i in range(4):
        
        pen.forward(shpwd)
        pen.left(90)
    pen.end_fill()
elif shp == "triangle":
    pen.begin_fill()
    pen.fillcolor("pink")
    for i in range (3):
       
        pen.forward(shpwd)
        pen.left(120)
    pen.end_fill()

else:
    print("Sorry, Invalid Shape")




turtle.done()