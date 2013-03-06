from Point import *

class Obstacle(Point):
    def __init__(self,x,y,canvas):
        self.coordx=x
        self.coordy=y
        canvas.create_rectangle(self.coordx-3,self.coordy-3,self.coordx+3,self.coordy+3,fill="black",tags="obst")
        

        