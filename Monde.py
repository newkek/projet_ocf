from tkinter import *
import Colonie
import Obstacle
import Globals

class Monde:
    def __init__(self,fenp):
        self.canvas=Canvas(fenp,width=Globals.canvas_size,height=Globals.canvas_size,bg="white",bd=2,relief="sunken")
        self.canvas.grid(row=2,rowspan=25,column=1,columnspan=3)
        cur_button="Chaine correspondant au bouton d'option actif"
        self.canvas.bind('<Button-1>',self.creation)
        #self.canvas.bind('<Button-2>',self.go)
        self.canvas.bind('<Double-Button-1>',quit)
        self.list_colo=[]
        self.num_colo=0
        self.list_obst=[]
        
    def creation(self,event):
        
        self.list_colo.append(Colonie.Colonie(event.x,event.y,10,self.num_colo,0,0,0,0,0,self.canvas))
        self.num_colo+=1
    
    def go(self):
        for colo in self.list_colo:
            colo.go()
            
    def stop(self):
        for colo in self.list_colo:
            colo.stop()
            
    def pause(self):
        for colo in self.list_colo:
            colo.pause()
            
    def continuer(self):
        for colo in self.list_colo:
            colo.continuer()
    
    def creer_obstacle(self,event):
        self.list_obst.append(Obstacle.Obstacle(event.x,event.y,self.canvas))
        