from Point import *

class Pheromone(Point):
    def __init__(self,x,y,origine,duree_vie,id_canvas):
        self.coordx=x
        self.coordy=y
        self.temps_restant=duree_vie
        self.id_canvas=id_canvas

    def evaporation(self):
        self.temps_restant=self.temps_restant-1
        return self.temps_restant