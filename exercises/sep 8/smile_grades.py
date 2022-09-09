#author-yaz c.


import turtle
turtle.bgcolor("medium purple")

pen = turtle.Turtle() #to set up a pen
#pen specifics
pen.pensize(2) #to change pen width
pen.color("gold")
pen.speed(0)

radius = turtle.window_width()//5
eye_radius = radius // 6
mouth_radius = radius//2
grade = turtle.numinput("Grades", "Enter Grade","",0,100)
arc_radius = 100

#draw head
pen.up()
pen.setpos(0,0)
pen.down()
pen.circle(arc_radius)


#eyes

pen.up()
pen.setpos(-radius//4,radius//1.5)
pen.down()
pen.circle(eye_radius)
pen.up()
pen.setpos(radius//4,radius//1.5 )
pen.down()
pen.circle(eye_radius)

#based on grade draw smile
if grade >= 89.5:
    pen.up()
    pen.setpos(-mouth_radius//1.15, radius//3)
    pen.down()

#smile
    pen.setheading(-60)
    pen.circle(mouth_radius,120)

#straight face

elif grade >= 79.5:
    pen.up()
    pen.setpos(-mouth_radius//1.15,radius//3)
    pen.down()
    pen.forward(mouth_radius*2)

#sad face

elif grade >= 69.5:
    pen.up()
    pen.setpos(-mouth_radius//1.15, radius//3)
    pen.down()
    pen.setheading(60)
    pen.circle(-mouth_radius, 120)









turtle.done()