from Point import *

class Ressource:
    def __init__(self,x,y,qte_restante,canvas):
        self.coordx=x
        self.coordy=y
        self.qte_restante=qte_restante
        canvas.create_oval(self.coordx-self.qte_restante,self.coordy-self.qte_restante,self.coordx+self.qte_restante,self.coordy+self.qte_restante,fill="Brown",tags="ress",width=self.qte_restante)
        
    def getQteRessource(self):
        return self.qte_restante
    
    def prendreRessource(self,valeur):
        if valeur < self.qte_restante:
            self.qte_restante=self.qte_restante-valeur
        else:
            print("Ne peut plus manger")