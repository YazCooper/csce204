#author-yaz c

import shapes as sh


class House:
    def __init__(self,address,x,y,width,build_clr,roof_clr,has_chimney):
        self.address = address
        self.x = x
        self.y = y
        self.width = width
        self.build_clr = build_clr
        self.roof_clr = roof_clr
        self.has_chimney = has_chimney

    #no pen must give it
    def draw(self,pen):
        sh.draw_rect(pen,self.x,self.y,self.width,self.width,self.build_clr)
        sh.draw_rect(pen,self.x+self.width*.35,self.y,self.width*.3,self.width*.6,self.roof_clr)
        if self.has_chimney:
            sh.draw_rect(pen,self.x+self.width*.65,self.y+self.width*1.4,self.width*.2,self.width*.4,self.build_clr)
        sh.draw_triangle(pen,self.x-self.width*.1,self.y+self.width,self.width*1.2,self.roof_clr)
        sh.draw_circle(pen,self.x+self.width*.45,self.y + self.width*.2,self.width*.05,self.build_clr)
        
        
    def draw_rect(self,pen,x,y,width,height,color):
        pen.up()
        pen.setpos(x,y)
        pen.color(color)
        pen.begin_fill()
        pen.down()
        for i in range(4):
            if i%2 == 0:
                pen.forward(width)
            else:
                pen.forward(height)
            pen.left(90)
        pen.end_fill()

    def draw_triangle(self,pen,x,y,width,color):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color(color)
        pen.begin_fill()
        for i in range (3):
            pen.forward(width)
            pen.left(120)
        pen.end_fill()

    def draw_circle(self,pen,x,y,radius,color):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color(color)
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()



    






    






