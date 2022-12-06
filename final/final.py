#author yaz c


import turtle

turtle.bgcolor("black")
pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.speed(0)
#pen.hideturtle()

#draw board
def draw_board():
    pen.up()
    pen.setpos(-turtle.window_width()//2.5,-turtle.window_height()//2.2)
    pen.down()
    for i in range(4):
        pen.forward(turtle.window_width()//1.3)
        pen.left(90)

    pen.up()
    pen.setpos(-turtle.window_width()//2.5,-turtle.window_height()//6)
    pen.down()
    pen.forward(turtle.window_width()//1.3)
    pen.up()
    pen.setpos(-turtle.window_width()//2.5,turtle.window_height()//6)
    pen.down()
    pen.forward(turtle.window_width()//1.3)
    pen.up()
    pen.setpos(-turtle.window_width()//7,-turtle.window_height()//2.2)
    pen.down()
    pen.setheading(90)
    pen.forward(turtle.window_width()//1.3)
    pen.up()
    pen.setpos(turtle.window_width()//8,-turtle.window_height()//2.2)
    pen.down()
    pen.forward(turtle.window_width()//1.3)



def draw_x(x,y):
    global turn
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.setheading(120)
    pen.forward(50)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.setheading(45)
    pen.forward(50)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.setheading(225)
    pen.forward(50)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.setheading(300)
    pen.forward(50)
    
    
    turn=turtle.onscreenclick(draw_o)
    




def draw_o(x,y):
    global turn
    pen.up()
    pen.setpos(x,y)
    pen.setheading(180)
    pen.forward(50)
    pen.setheading(270)
    pen.down()
    
    pen.circle(50)
    turn=turtle.onscreenclick(draw_x)
    
row_0=["","",""]
row_1=["","",""]
row_2=["","",""]


def play(row,column):
    draw_x(-200+200*column,200-200*row)

        


for j in range(2):
    for i in range (0):
        if row_0[i] == row_1[i] == row_2[i] != "":
            pen.write(f" The Winner is {row_0[i]} ",font=('arial',50))
        elif row_0[i] == row_1[i+1] == row_2[i+2] != "":
            pen.write(f"The winner is {row_0[i]}",font=('arial',50))
        elif row_0[i+2] == row_1[i+1] == row_2[i] != "":
            pen.write(f"The winner is {row_0[i]}",font=('arial',50))
        elif row_0[i+1] == row_1[i+1] == row_2[i+1] != "":
            pen.write(f"The winner is {row_0[i]}",font=('arial',50))
        elif row_0[i+2] == row_1[i+2] == row_2[i+2] != "":
            pen.write(f"The winner is {row_0[i]}",font=('arial',50))
        else:
            break




draw_board()

turtle.onscreenclick(play)








turtle.done()