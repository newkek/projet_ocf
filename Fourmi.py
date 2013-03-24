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
        self.departcolo=True

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
        four=(curpos[0]+Globals.fourmi_size/2,curpos[1]+Globals.fourmi_size/2)#four sera le centre de la fourmi
        if self.endurance_courante:
            depx=self.mem_x#deplacement avec l'angle choisi
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
            if self.departcolo is True:
                self.departcolo=False  
        else:#MODE RETOUR
            ###revenir a la colonie
            if (self.nid[0]<=four[0] and self.nid[1]<=four[1]):
                depx=-2
                depy=-2
            elif(self.nid[0]<=four[0] and self.nid[1]>four[1]):
                depx=-2
                depy=2
            elif(self.nid[0]>four[0] and self.nid[1]<=four[1]):
                depx=2
                depy=-2
            elif(self.nid[0]>four[0] and self.nid[1]>four[1]):
                depx=2
                depy=2
                

            ###
            depx=depx+random.randint(-1,1)
            depy=depy+random.randint(-1,1)
            if((self.nid[0]-10)<four[0]<(self.nid[0]+10) and (self.nid[1]-10)<four[1]<(self.nid[1]+10)):#Si on est arrivŽ dans la zone de la colonie    
                self.endurance_courante=self.endurance#mode retour OFF
                self.teta=random.randint(0,360)#nouvel angle de depart
                self.teta=(self.teta*3.14)/180
                self.mem_x=3*math.cos(self.teta)
                self.mem_y=3*math.sin(self.teta)
                self.trouve=False
                self.departcolo=True
            else:
                self.departcolo=False
                
            if self.trouve:#si on a trouve de la bouf on depose des pheromone sur le retour                
                depx=2*self.mem_x+random.uniform(-0.5,0.5)
                depy=2*self.mem_y+random.uniform(-0.5,0.5)
                if int(four[0])%3==0:
                    self.canvas.create_rectangle(four[0]-2,four[1]-2,four[0]+2,four[1]+2,fill='indianred3',width=0,tags="pher")
                #print(four[0])
        ###    I.  A.  
        closest=self.canvas.find_closest(four[0]+depx,four[1]+depy,halo=3)#recherche de l'objet le plus proche
        tags_closest=self.canvas.itemcget(closest,"tags")
        if tags_closest=="obst":
            depx=-depx#on evite le l'obstacle, en inversant on cree l effet 'zombie'
            depy=-depy
        elif tags_closest=="ress":
            curwidth=float(self.canvas.itemcget(closest,"width"))
            if curwidth>0:#si la ressource n'est pas 'vide' 
                if curwidth-0.4<=0:#si on c'est la derniere fois que l'on peut subtiliser de la nourriture
                    self.canvas.itemconfigure(closest,fill="grey16")
                    self.canvas.lower(closest)#la ressource est 'supprimee'
                else:
                    self.canvas.itemconfigure(closest,width=curwidth-0.4)
                    self.canvas.tag_raise(closest)
                self.endurance_courante=0#mode retour ON
                self.trouve=True
                B=[self.nid[0],four[1]]
                AB=B[0]-four[0]
                BC=B[1]-self.nid[1]
                tempx=(self.nid[0]-four[0])/abs(self.nid[0]-four[0])
                self.teta=-math.atan(BC/AB)
                self.mem_x=tempx*math.cos(self.teta)
                self.mem_y=tempx*math.sin(self.teta)
                print(self.mem_x,self.mem_y)
                depx=self.mem_x
                depy=self.mem_y
        elif tags_closest=="pher":
            pher=self.canvas.coords(closest)
            if self.endurance_courante:#si on est en mode 'decouverte'
                if (pher[0]<=four[0] and pher[1]<=four[1]):
                    depx=depx-1
                    depy=depy-2#Comportement comme les chiens, elle va plus vite lorsquelle est sur la piste
                elif(pher[0]<=four[0] and pher[0]>four[1]):
                    depx=depx-1
                    depy=depy+2
                elif(pher[0]>four[0] and pher[1]<=four[1]):
                    depx=depx+1
                    depy=depy-2
                elif(pher[0]>four[0] and pher[0]>four[1]):
                    depx=depx+1
                    depy=depy+2
                
                if (self.departcolo is True):
                    dist=math.sqrt(math.pow(pher[0]-four[0],2)+math.pow(pher[1]-four[1],2))
                    #print(dist, pher[0],pher[1],four[0],four[1])
            else:
                
                """if (pher[0]<=four[0]+depx):
                    depx=depx+random.randint(0,int(dist))
                    pass
                elif(pher[0]>four[0]+depx):
                    depx=depx-random.randint(0,int(dist))
                    pass
                if (pher[0]<=four[0] and pher[1]<=four[1]):
                    self.mem_x=-2
                    self.mem_y=-2
                elif(pher[0]<=four[0] and pher[0]>four[1]):
                    self.mem_x=-2
                    self.mem_y=2
                elif(pher[0]>four[0] and pher[1]<=four[1]):
                    self.mem_x=2
                    self.mem_y=-2
                elif(pher[0]>four[0] and pher[0]>four[1]):
                    self.mem_x=2
                    self.mem_y=2"""
                pass
        #print("fin",self.fourm_Id,depx,depy)
        return depx,depy

        
    
    