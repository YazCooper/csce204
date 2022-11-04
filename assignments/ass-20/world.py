#author- yaz c
import turtle
pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
#pen.hideturtle() #hides the cur
pen.speed(0)
turtle.bgcolor("medium purple")

def get_candies():

    candies = []
    with open("assignments/ass-20/scene.txt") as file:
        for line in file:
            if line.strip() != "":
                candies.append(line.strip())
    return candies


def draw_mint(x,y,size):
    
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color("gold")
    pen.setheading(30)
    pen.begin_fill()
    for i in range (3):
        
        pen.forward(size)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.forward(size)
    pen.down()
    pen.begin_fill()
    for j in range (3):
        pen.forward(size)
        pen.right(120) 
    pen.end_fill()
    pen.up()
    pen.setheading(90)
    pen.forward(size//2)
    pen.setheading(180)

    pen.down()  
    pen.begin_fill()
    pen.circle(size//2)
    pen.end_fill()
    pen.color("beige")
    pen.up()
    pen.setheading(-100)
    pen.forward(4)
    pen.down()
    pen.setheading(0)
    for g in range (6):
        pen.up()
        pen.sety(y)
        y+=5
        pen.down()
        pen.circle(size//2)
        size -= 10
    #pen.setheading(0)

def draw_lollipop(x,y,size):
   
    pen.up()
    pen.setpos(x,y)
    pen.color("brown")
    pen.down()
    pen.setheading(90)
    pen.forward(size//2)
    pen.up()
    pen.forward(size//30)
    pen.setheading(0)
    pen.color("beige")
    
    pen.down()
    pen.begin_fill()
    pen.circle(size//3)
    pen.end_fill()
    pen.color("hot pink")
    
    
    for g in range (6):
        pen.circle(size//3)
        pen.up()
        pen.setheading(90)
        pen.forward(5)
        
        pen.down()
        size-=15
        pen.setheading(0)
        
        
    

candies = get_candies()
spacing = 150
x=-turtle.window_width()//2
y=0       
for candy in candies:
    
    if candy == "lollipop":
        draw_lollipop(x,y,60)
        
    elif candy == "mint":
         draw_mint(x,y,60)
         x+=spacing//2
    x+=spacing


    






turtle.done()