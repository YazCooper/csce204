#author-yaz c

def move(pen,x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()



def draw_rect(pen,x,y,width,height,color):
    move(pen,x,y)
    
    pen.color(color)
    pen.begin_fill()
    
    for i in range(4):
        if i%2 == 0:
            pen.forward(width)
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()

def draw_triangle(pen,x,y,width,color):
    move(pen,x,y)
    pen.color(color)
    pen.begin_fill()
    for i in range (3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_circle(pen,x,y,radius,color):
    move(pen,x,y)
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()



#generic library