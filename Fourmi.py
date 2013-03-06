from Point import *
import random
import Globals
import threading
import time
import math
class Fourmi(Point,threading.Thread):
    def __init__(self,origine,vitesse,endurance,tps_phero,ratio,vision,basex,basey,canvas):
        threading.Thread.__init__(self)
        self.origine=origine
        self.vitesse=vitesse
        self.temps_pheromone=tps_phero
        self.ratio_qte_pheromone=ratio
        self.vision=vision
        self.endurance=endurance
        self.coordx=basex+random.randint(-30,30)
        self.coordy=basey+random.randint(-30,30)
        self.canvas=canvas
        self.fourm_Id=canvas.create_oval(self.coordx-2,self.coordy-2,self.coordx+2,self.coordy+2,fill=Globals.couleurs_colo[origine])
        self.terminated=False
        self.pause=False
        self.teta=random.randint(0,360)
        self.teta=(self.teta*3.14)/180
        self.mem_x=3*math.cos(self.teta)
        self.mem_y=3*math.sin(self.teta)
        self.endurance_courante=endurance
        self.trouve=False
        id_nid=self.canvas.find_withtag("colonie{0}".format(self.origine))
        coords_nid=self.canvas.coords(id_nid)
        self.nid=(coords_nid[0]+10,coords_nid[1]+10)

    def continuer(self):
        self.pause=False
             
    def run(self):
        while self.terminated is False:
            time.sleep(0.02)
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
        four=(curpos[0]+2,curpos[1]+2)#four sera le centre de la fourmi
        if (self.endurance_courante):
            depx=self.mem_x
            depy=self.mem_y
            self.endurance_courante-=1
            if (four[0]<=Globals.fourmi_size and depx<0) or (four[0]>=Globals.canvas_size-Globals.fourmi_size and depx>0):
                depx=-depx
            if (four[1]<=Globals.fourmi_size and depy<0) or (four[1]>=Globals.canvas_size-Globals.fourmi_size and depy>0):
                depy=-depy
            if self.endurance_courante <= 0:
                self.retour=True
            depx=depx+random.randint(-2,2)
            depy=depy+random.randint(-1,1)
            
        else:#RETOUR
            if (self.nid[0]<=four[0] and self.nid[1]<=four[1]):
                depx=-3
                depy=-3
            elif(self.nid[0]<=four[0] and self.nid[1]>four[1]):
                depx=-3
                depy=3
            elif(self.nid[0]>four[0] and self.nid[1]<=four[1]):
                depx=3
                depy=-3
            elif(self.nid[0]>four[0] and self.nid[1]>four[1]):
                depx=3
                depy=3
            if((self.nid[0]-10)<four[0]<(self.nid[0]+10) and (self.nid[1]-10)<four[1]<(self.nid[1]+10)):
                self.endurance_courante=self.endurance
                self.teta=random.randint(0,360)
                self.teta=(self.teta*3.14)/180
                self.mem_x=3*math.cos(self.teta)
                self.mem_y=3*math.sin(self.teta)
                self.trouve=False
            if self.trouve:
                rect=self.canvas.create_rectangle(four[0]-2,four[1]-2,four[0]+2,four[1]+2,fill='indianred3',width=0,tags="pher")
                self.canvas.lower(rect)
            depx=depx+random.randint(-2,2)
            depy=depy+random.randint(-2,2)
        closest=self.canvas.find_closest(four[0]+depx,four[1]+depy)
        tags_closest=self.canvas.itemcget(closest,"tags") 
        if tags_closest=="obst":
            depx=-depx
            depy=-depy
            
        elif tags_closest=="ress":
            curwidth=float(self.canvas.itemcget(closest,"width"))
            if curwidth>0:
                if curwidth-0.4<=0:
                    self.canvas.itemconfigure(closest,fill="grey16")
                    self.canvas.lower(closest)
                else:
                    self.canvas.itemconfigure(closest,width=curwidth-0.4)
                    self.endurance_courante=0
                    self.trouve=True
        if tags_closest=="pher":
            if self.endurance_courante:
                pher=self.canvas.coords(closest)
                if (pher[0]<=four[0] and pher[1]<=four[1]):
                    depx=-2
                    depy=-2
                elif(pher[0]<=four[0] and pher[0]>four[1]):
                    depx=-2
                    depy=2
                elif(pher[0]>four[0] and pher[1]<=four[1]):
                    depx=2
                    depy=-2
                elif(pher[0]>four[0] and pher[0]>four[1]):
                    depx=2
                    depy=2
                
        return depx,depy

        
    
    