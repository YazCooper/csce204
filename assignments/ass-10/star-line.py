#author-yaz c


import turtle

pen = turtle.Turtle()
pen.pensize(2)
pen.color("black")
pen.hideturtle()
pen.speed(0)


star =turtle.numinput("Stars","How many Stars?")
x=-turtle.window_width()//2
spacing = turtle.window_width()//10




for i in range (int(star)):

    pen.up()
    pen.setx(turtle.window_width()//36 + x)
    pen.down()
    
    pen.begin_fill()
    pen.fillcolor("pink")
    for j in range (8):
        pen.forward(50)
        pen.left(135)
    pen.end_fill()
    
    pen.up()
    pen.setpos(-5,5)
    pen.down()
    
    x+=spacing

    
        








turtle.done()


