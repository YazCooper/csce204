#author-yaz c

import turtle
from house import House

turtle.bgcolor("black")

pen = turtle.Turtle()
pen.pensize(2)
pen.color("black")
pen.hideturtle()
pen.speed(0)

my_house = House("1 A street",0,0,50,"medium purple","hot pink",True)

my_house.draw(pen)   #pass the pen to the function


houses = []
houses.append(House("1 A street",-100,-20,50,"medium purple","hot pink",True))

houses.append(House("7 B street",-250,10,50,"medium purple","yellow",False))

houses.append(House("2 C street",-25,100,50,"red","orange",True))

houses.append(House("3 D street",0,-300,50,"blue","pink",False))

houses.append(House("9 F street",200,-150,50,"medium purple","green",True))

for house in houses:
    house.draw(pen)



turtle.done()

