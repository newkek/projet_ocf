from Point import *
import Fourmi
import Couleurs
import threading
#Commentaire ligne 5
class Colonie(Point):
    def __init__(self,x,y,nombre_fourmi,origine,vitesse,endurance,tps_phero,ratio,vision,canvas):
        self.coordx=x
        self.coordy=y
        self.origine=origine
        self.canvas=canvas
        canvas.create_oval(self.coordx-10,self.coordy-10,self.coordx+10,self.coordy+10,fill=Couleurs.couleurs_colo[origine])
        #creation de toutes les fourmis
        self.liste_fourmi=[]
        for step in range(nombre_fourmi):
            self.liste_fourmi.append(Fourmi.Fourmi(origine,vitesse,endurance,tps_phero,ratio,vision,self.coordx,self.coordy,canvas))
            #print("Creation de la fourmi",step)
            
    def go(self):
        for fourmi in self.liste_fourmi:
            fourmi.start()