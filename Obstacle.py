from Point import *

class Obstacle(Point):
    def __init__(self,x,y,canvas):
        self.coordx=x
        self.coordy=y
        
        canvas.create_rectangle(self.coordx-10,self.coordy-10,self.coordx+10,self.coordy+10,fill="black")
        

        