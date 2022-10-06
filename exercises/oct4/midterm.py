#author-yaz c



import turtle
import random

turtle.setup(600,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
turtle.bgcolor("cyan")
pen.up()
pen.setpos(-turtle.window_width(),-150)
pen.down()
pen.color("burlywood")
pen.begin_fill()
for i in range (2):
    pen.forward(575*2)
    pen.left(90)
    pen.forward(325)
    pen.left(90)
pen.end_fill()




#gridsize = int(turtle.numinput())

#bikename = turtle.textinput("Bike Name","What is the name of the bike? ")
#bikecolor = turtle.textinput("Bike Color","What color do you want the bike to be?: ")


pen.color("black")
bkname = []
bkcolor = []
while True:
    bike = int(turtle.numinput("Bikes","How many bikes do you have?: ",0,1,10))

    bikecolor = turtle.textinput("Bike Color","What color do you want the bike to be?: ")

    for color in bkcolor:
        bkcolor.append(bikecolor)
        

    for name in bkname:
        bksname = turtle.textinput("Name","What is the bikes name?: ")
        bkname.append(bksname)
        

    bikepadding = turtle.window_width()/bike
    rad = bikepadding * .8 / 8
    padding = bikepadding *.1


    for row in range (bike):
        x=-turtle.window_width()/2 + bikepadding /2
        #x=random.randrange(-150,150)
        y=random.randrange(-150,150)
        #y = -turtle.window_height()/4 + bikepadding * row + padding

        for col in range (bike):
            
                pen.up()
                pen.color("black")
                pen.setpos(x,y)
                
                pen.down()

                for i in range (1):
                    pen.setheading(0)
                    pen.circle(rad)
                    pen.up()
                    pen.forward(padding *4)
                    pen.down()
                    pen.circle(rad)
                    
                    #pen.right(180)
                    pen.up()
                    pen.left(90)
                    pen.forward(padding//.8)
                    pen.left(90)
                    pen.down()
                    pen.forward(bikepadding//2)
                    pen.right(90)
                    pen.forward(padding*3)

                x+=bikepadding
                y+=random.randrange(-100,100)
                    
                

                
        else:
            break
    else:
        break













turtle.done()
