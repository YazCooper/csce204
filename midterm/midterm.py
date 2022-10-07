#author-yaz c



import turtle
import random

turtle.setup(700,575)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)
turtle.bgcolor("cyan")
pen.up()
pen.setpos(-turtle.window_width(),-150)
pen.down()
pen.color("burlywood")
pen.begin_fill()
for i in range (2):
    pen.forward(600*2)
    pen.left(90)
    pen.forward(325)
    pen.left(90)
pen.end_fill()

pen.up()
pen.color("black")
pen.setpos(-turtle.window_width()//3,turtle.window_height()//3)
pen.down()
pen.write("Biking Party",font=("Arial", 24))




#gridsize = int(turtle.numinput())

#bikename = turtle.textinput("Bike Name","What is the name of the bike? ")
#bikecolor = turtle.textinput("Bike Color","What color do you want the bike to be?: ")



pen.color("black")
bkname = []
bkcolor = []
while True:
    bike = int(turtle.numinput("Bikes","How many bikes do you have?: ",0,1,10))
    for i in range (bike):



        
       
            

        bikepadding = turtle.window_width()/bike 
        rad = bikepadding * .8 / 8
        padding = bikepadding *.1


        #for row in range (bike):
        x=-turtle.window_width()/2 + bikepadding /2
        #x=random.randrange(-150,150)
        y=random.randrange(-150,150)
         #y = -turtle.window_height()/4 + bikepadding * row + padding

        for col in range (bike):
                
            pen.up()
                    
            pen.setpos(x,y)
                    
            pen.down()

            for i in range (1):
                bikecolor = turtle.textinput("Bike Color","What color do you want the bike to be?: ")
                bkcolor.append(bikecolor)
        
                bksname = turtle.textinput("Name","What is the bikes name?: ")
                bkname.append(bksname)
                pen.setheading(0)
                pen.color("black")
                pen.circle(rad)
                pen.up()
                pen.forward(padding *4)
                pen.down()
                pen.circle(rad)
                       
                pen.up()
                pen.left(90)
                pen.forward(padding//.8)
                pen.left(90)
                pen.down()
                pen.color(bikecolor)
                pen.forward(bikepadding//2)                      
                pen.right(90)
                pen.forward(padding*3)
                pen.setheading(0)
                pen.forward(padding//2)
                pen.setheading(180)
                pen.forward(padding)
                pen.write(bksname)
            x+=bikepadding
            y+=random.randrange(-100,100)
    else:
        break