#author-yaz c


import turtle

pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
#pen.hideturtle() #hides the cur
pen.speed(0)

def get_colors():
    colors = []
    try:
        with open("exercises/nov1/colors.txt") as file:
            for line in file:
                if line.strip() != "":
                    colors.append(line.strip())
    except FileNotFoundError:
        print("Invalid File Name.")

    return colors


def draw_color_strip(y,height,color):
    x=-turtle.window_width()//2
    pen.up()
    pen.setpos(x, y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range (4):
        if i % 2 == 0:
            pen.forward(turtle.window_width())
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()
    
#main program

colors = get_colors()

y = -turtle.window_height()//2
height = turtle.window_height()/len(colors)    #len(colors) means that it will consider the length of the list to make room

for color in colors:
    draw_color_strip(y,height,color)
    y+=height


turtle.done()























