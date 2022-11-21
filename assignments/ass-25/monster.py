#author - yaz c




class Monster:
    def __init__(self,x,y,width,color):
        self.x=x
        self.y=y
        self.width=width
        self.color=color

    def draw(self,pen):
        pen.up()
        pen.setpos(self.x,self.y)

    
        pen.up()
        pen.setpos(self.x-self.width//2,self.y-self.width//2)
        pen.down()
        pen.setheading(15)
        pen.color(self.color)
        pen.begin_fill()
        for i in range (4):
            

            pen.forward(self.width)
            pen.right(90)
        pen.end_fill()
        pen.up()
        pen.setpos(self.x-self.width//1.2,self.y-self.width)
        pen.down()
        pen.forward(self.width*2)

        pen.up()
        pen.setpos(self.x-self.width//5,self.y-self.width*1.1)
        pen.setheading(315)
        pen.down()

        radius = self.width//3
        pen.color("black")
        pen.circle(radius,120)
        pen.color("white")
        pen.up()
        pen.setpos(self.x-self.width//5.5,self.y-self.width*1.1)
        pen.down()
        pen.begin_fill()
        pen.right(40)
        pen.forward(self.width//15)
        pen.right(120)
        pen.forward(self.width//12)
        pen.end_fill()
        
        
        



    
        pen.up()
        pen.setheading(55)
        pen.setpos(self.x+self.width//25,self.y-self.width//1.3)
        pen.down()
        pen.color("white")
        pen.begin_fill()
        pen.circle(self.width//5)
        pen.end_fill()
        pen.up()
        pen.setpos(self.x - self.width//30,self.y-self.width//1.3)
        pen.down()
        #pen.setheading(10)
        pen.color("black")
        pen.begin_fill()
        pen.circle(self.width//7.5)
        pen.end_fill()
        pen.up()
        pen.setx(self.x+self.width//1.9)
        pen.down()
        pen.color("white")
        pen.begin_fill()
        pen.circle(self.width//5)
        pen.end_fill()
        pen.up()
        pen.setpos(self.x+self.width//2.1,self.y-self.width//1.3)
        pen.down()
        pen.color("black")
        pen.begin_fill()
        pen.circle(self.width//7.5)
        pen.end_fill()
        pen.up()
        pen.setpos(self.x-self.width//15,self.y-self.width*1.2)
        pen.setheading(250)
        pen.color(self.color)
        pen.down()
        pen.forward(self.width//2)
        pen.up()
        pen.setpos(self.x+self.width//2,self.y-self.width*1.2)
        pen.down()
        pen.forward(self.width//2)
        






    
    


            
        
        

        


    # def draw_body(self,pen,x,y,width):
    #     pen.up()
    #     pen.setpos(x,y)
    #     pen.down()
    #     for i in range(4):
    #         pen.forward(width)
    #         pen.right(90)
    
   

        











