from Point import *

class Obstacle(Point):
    def __init__(self,x,y,canvas):
        self.coordx=x
        self.coordy=y
        canvas.create_rectangle(self.coordx-2,self.coordy-2,self.coordx+2,self.coordy+2,fill="black",tags="obst")
        

        