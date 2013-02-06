from Point import *
import random
import Couleurs
import threading
import time

class Fourmi(Point,threading.Thread):
    def __init__(self,origine,vitesse,endurance,tps_phero,ratio,vision,basex,basey,canvas):
        threading.Thread.__init__(self)
        self.origine=origine
        self.vitesse=vitesse
        self.endurance=endurance
        self.temps_pheromone=tps_phero
        self.ratio_qte_pheromone=ratio
        self.vision=vision
        self.coordx=basex+random.randint(-30,30)
        self.coordy=basey+random.randint(-30,30)
        self.canvas=canvas
        self.fourm_Id=canvas.create_oval(self.coordx-2,self.coordy-2,self.coordx+2,self.coordy+2,fill=Couleurs.couleurs_colo[origine])
        self.terminated=False
        
    def run(self):
        offset=5
        while self.terminated is False:
            time.sleep(0.01)
            depx=random.randint(-offset,offset)
            depy=random.randint(-offset,offset)
            curpos=self.canvas.coords(self.fourm_Id)
            if (curpos[0]<=4 and depx<0) or (curpos[0]>=496 and depx>0):
                depx=-depx
            if (curpos[1]<=4 and depy<0) or (curpos[1]>=496 and depy>0):
                depy=-depy
            self.canvas.move(self.fourm_Id,depx,depy)
            
    def stop(self):
        self.terminated=True
    
    