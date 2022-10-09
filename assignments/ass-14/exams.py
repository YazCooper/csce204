#author-yaz c



from datetime import date, time, datetime      #to use dates



import turtle



turtle.bgcolor("white")
turtle.setup(800,600)
counter = 1
pen = turtle.Turtle()
pen.pensize(5)
pen.color("red")
#pen.hideturtle()
pen.speed(0)


exams={
    "ITEC 240":datetime(2022,10,8,14,20),
    "ITEC 567":datetime(2022,10,8,15,25),
    "RETL 345":datetime(2022,10,14,8,15),
    "ASTR 980":datetime(2022,10,9,16,30),
    "ENGL 245":datetime(2022,10,10,12,45),
    "MATH 904":datetime(2022,10,31,10,20)
    }

boxtop = turtle.window_width()//3

pen.up()
pen.setpos(-turtle.window_width()//2.5,turtle.window_height()//4)
pen.down()

for i in range (4):
    
    pen.forward(boxtop)
    pen.right(90)
    pen.forward(boxtop)
    pen.right(90)
pen.up()
pen.forward(boxtop*1.5)
pen.down()
for j in range(4):
    pen.forward(boxtop)
    pen.right(90)
    pen.forward(boxtop)
    pen.right(90)
pen.up()
pen.setpos(-turtle.window_width()//3,turtle.window_height()//8)
pen.color("black")
pen.down()


pen.write("Todays Exams: \n \n ", font=(24)) 

#while True:
today = datetime(2022,10,8).date()
tdy = date.today()
#ttt = datetime.date()
for exam in exams:           
    ggg= exams[exam]
    

    if datetime.today().date()  ==  exams[exam].date() :
        pen.write( f"{exam} {ggg.strftime('%I:%M %p')}", align='left' )
        pen.up()
        pen.right(90)
        pen.forward(25)
        pen.down()
        pen.setheading(0)
    else:
        break

pen.up()
pen.setpos(turtle.window_width()//6, turtle.window_height()//8)
pen.down()
pen.write("Upcoming Exams: \n \n",font=(24))

for exam in exams:
    
    if datetime.today().date() != exams[exam].date():
        pen.write( f"{exam} {ggg.strftime('%I:%M %p')}", align='left' )
        pen.up()
        pen.right(90)
        pen.forward(25)
        pen.down()
        pen.setheading(0)

        

        
    
    
    
   
   

        
        
       
        

    
    
        
        

    
    



turtle.done()