from Point import *

class Ressource:
    def __init__(self,x,y,qte_restante):
        self.coordx=x
        self.coordy=y
        self.qte_restante=qte_restante
        
    def getQteRessource(self):
        return self.qte_restante
    
    def prendreRessource(self,valeur):
        if valeur < self.qte_restante:
            self.qte_restante=self.qte_restante-valeur
        else:
            print("Ne peut plus manger")