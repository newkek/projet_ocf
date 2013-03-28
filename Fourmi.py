from Point import *
import random
import Globals
import threading
import time
import math
import Pheromone

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

        else:#MODE RETOUR
            ###revenir a la colonie sans pheromone
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
            if self.trouve:#si on a trouve de la bouf on depose des pheromone sur le retour                
                depx=2*self.mem_x
                depy=2*self.mem_y
                if int(four[0])%3==0 or int(four[1])%3==0:
                    id=self.canvas.create_rectangle(four[0]-2,four[1]-2,four[0]+2,four[1]+2,fill='indianred3',width=0,tags="pher")
                    Globals.list_pher.append(Pheromone.Pheromone(four[0]+1,four[1]+1,self.origine,int(Globals.entrys["value_evaporation"].get()),id))
                if int(four[0])%10==0 or int(four[1])%10==0:
                    self.redef_depl(four)    

            ###
            depx=depx+random.randint(-1,1)
            depy=depy+random.randint(-1,1)
            
            
            if((self.nid[0]-10)<four[0]<(self.nid[0]+10) and (self.nid[1]-10)<four[1]<(self.nid[1]+10)):#Si on est arriv� dans la zone de la colonie    
                obj=self.canvas.find_enclosed(self.nid[0]-12,self.nid[1]-12,self.nid[0]+12,self.nid[1]+12)
                moy=[0,0]
                cpt=0       
                for item in obj:
                    tags=self.canvas.gettags(item)
                    if tags:
                        if tags[0]=="pher":
                            coord_pher=self.canvas.coords(item)
                            moy[0]+=coord_pher[0]
                            moy[1]+=coord_pher[1]
                            cpt+=1
                if cpt:
                    moy[0]=moy[0]/cpt
                    moy[1]=moy[1]/cpt
                    depx=(self.nid[0]-four[0])
                    depy=(self.nid[1]-four[1])
                    
                    next=(four[0]+depx,four[1]+depy)
                    self.redef_depl_pher(next,moy)   
                else:
                    self.teta=random.randint(0,360)#nouvel angle de depart
                    self.teta=(self.teta*3.14)/180
                    self.mem_x=2*math.cos(self.teta)
                    self.mem_y=2*math.sin(self.teta)
                self.trouve=False
                self.endurance_courante=self.endurance#mode retour OFF
                return depx,depy      
                    
        ###    I.  A.  
        closest=self.canvas.find_closest(four[0]+depx,four[1]+depy,halo=int(Globals.entrys["value_vision"].get()))#recherche de l'objet le plus proche
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
                self.redef_depl(four)
                depx=self.mem_x#premier deplacement pour le retour a vol doiseau
                depy=self.mem_y
        elif tags_closest=="pher":
            if self.endurance_courante:
                pher=self.canvas.coords(closest)
                if (pher[0]<=four[0] and pher[1]<=four[1]):
                    depx=depx-0.5
                    #depy=depy-1
                elif(pher[0]<=four[0] and pher[0]>four[1]):
                    depx=depx-0.5
                    #depy=depy+1
                elif(pher[0]>four[0] and pher[1]<=four[1]):
                    depx=depx+0.5
                    #depy=depy-1
                elif(pher[0]>four[0] and pher[0]>four[1]):
                    depx=depx+0.5
                    #depy=depy+1
        return depx,depy
    
    def redef_depl(self,four):
        B=[self.nid[0],four[1]]###On d�fini l'angle pour le retour a vol doiseau
        AB=B[0]-four[0]
        BC=B[1]-self.nid[1]
        coef=(self.nid[0]-four[0])/abs(self.nid[0]-four[0])
        self.teta=-math.atan(BC/AB)
        self.mem_x=coef*math.cos(self.teta)
        self.mem_y=coef*math.sin(self.teta)

    def redef_depl_pher(self,four,moyenne):
        B=[moyenne[0],four[1]]###On d�fini l'angle pour le retour a vol doiseau
        AB=B[0]-four[0]
        BC=B[1]-moyenne[1]
        coef=(moyenne[0]-four[0])/abs(moyenne[0]-four[0])*2
        self.teta=-math.atan(BC/AB)
        self.mem_x=coef*math.cos(self.teta)
        self.mem_y=coef*math.sin(self.teta)     
    