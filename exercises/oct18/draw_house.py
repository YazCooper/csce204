#author- yaz c



import turtle

turtle.bgcolor("medium purple")
pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.speed(0)
#pen.hideturtle()

def draw_square(x,y,width,color):
    draw_rect(x,y,width,width,color) #to draw a square in one line
    
def draw_triangle(x,y,width,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(0)
    pen.begin_fill()
    for i in range (3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()    
   
def draw_rect (x,y,width,height,color):

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(0)
    pen.begin_fill()
    for i in range (4):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

def draw_circle(x,y,radius,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    pen.setheading(0)
    for i in range (1):
        pen.circle(radius)
    pen.end_fill()

def draw_house(x,y,width,siding_color, roof_color,door_color):

    draw_square(x,y,width,siding_color)
    draw_triangle(x-width*.1,y+width,width*1.2,roof_color)
    draw_rect(x+width*.4,y,width*.2,width*.5, door_color)
    draw_circle(x+width*.55,y+width*.3,width*.025,roof_color)

def draw_appletree (x,y,width):
    draw_rect(x,y,width,width*4,"brown")
    draw_circle(x+width/2,y+width*3.5,width*2,"green")
    draw_circle(x+width/4 , y+width*4.5 , width/4 , "red")
    #draw_circle(x+width/3 , y+width*.5 , width/4 , "red")
    #draw_circle(x+width/2 , y+width*.2 , width/4 , "red")
    #draw_circle(x+width/5 , y+width , width/4, "red")



x = - turtle.window_width()//2
y = 0
num_houses = 6
grid = turtle.window_width() / num_houses
padding = grid*.2

for i in range (6):
    draw_house(x+padding,y,grid//3,"gold","gray","pink")
    draw_appletree(x+padding+grid*2/3, y,grid*.05 )
    x+=grid



#draw_house(-100,-100,100,"hot pink","green","gold")
#draw_appletree(50,-100,30)

#draw_triangle(0,-23,150,"hot pink")



#draw_rect(65,-125,20,50,"orange")

#draw_circle(75,-15,30,"green")
turtle.done()