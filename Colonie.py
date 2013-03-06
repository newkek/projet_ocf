from Point import *
import Fourmi
import Globals
import threading
class Colonie(Point):
    def __init__(self,x,y,nombre_fourmi,origine,vitesse,endurance,tps_phero,ratio,vision,canvas):
        self.coordx=x
        self.coordy=y
        self.origine=origine
        self.canvas=canvas
        canvas.create_oval(self.coordx-10,self.coordy-10,self.coordx+10,self.coordy+10,fill=Globals.couleurs_colo[origine],tags="colonie{0}".format(self.origine))
        #creation de toutes les fourmis
        print("lalal","colonie {0}".format(self.origine))
        self.liste_fourmi=[]
        for step in range(nombre_fourmi):
            self.liste_fourmi.append(Fourmi.Fourmi(self.origine,vitesse,endurance,tps_phero,ratio,vision,self.coordx,self.coordy,canvas))
            
    def go(self):
        for fourmi in self.liste_fourmi:
            fourmi.start()
            
    def stop(self):
        for fourmi in self.liste_fourmi:
            fourmi.stop()
            
    def pause(self):
        for fourmi in self.liste_fourmi:
            fourmi.pauser()
            
    def continuer(self):
        for fourmi in self.liste_fourmi:
            fourmi.continuer()