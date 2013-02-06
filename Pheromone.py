from Point import *

class Pheromone(Point):
    def __init__(self,x,y,origine,duree_vie):
        self.coordx=x
        self.coordy=y
        self.temps_restant=duree_vie

    def evaporation(self):
        self.temps_restant=self.temps_restant-1