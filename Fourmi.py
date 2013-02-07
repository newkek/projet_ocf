from Point import *
import random
import Globals
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
        self.fourm_Id=canvas.create_oval(self.coordx-2,self.coordy-2,self.coordx+2,self.coordy+2,fill=Globals.couleurs_colo[origine])
        self.terminated=False
        self.pause=False


    def continuer(self):
        self.pause=False
             
    def run(self):
        while self.terminated is False:
            time.sleep(0.01)
            if self.pause:
                pass
            else:
                curpos=self.canvas.coords(self.fourm_Id)
                next_dep=self.prochain_dep(curpos)
                self.canvas.move(self.fourm_Id,next_dep[0],next_dep[1])
            
    def stop(self):
        self.terminated=True
        
    def pauser(self):
        self.pause=True
        
    def prochain_dep(self,curpos):
        offset=5
        depx=random.randint(-offset,offset)
        depy=random.randint(-offset,offset)
        if (curpos[0]<=Globals.fourmi_size and depx<0) or (curpos[0]>=Globals.canvas_size-Globals.fourmi_size and depx>0):
            depx=-depx
        if (curpos[1]<=4 and depy<0) or (curpos[1]>=496 and depy>0):
            depy=-depy
        return depx,depy

        
    
    