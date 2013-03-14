from tkinter import *
import Colonie
import Obstacle
import Globals
import Ressource

class Monde:
    def __init__(self,fenp):
        self.canvas=Canvas(fenp,width=Globals.canvas_size,height=Globals.canvas_size,bg="gray59",bd=2,relief="sunken")
        self.canvas.grid(row=2,rowspan=25,column=1,columnspan=3)
        self.canvas.bind('<Button-1>',self.creation)
        self.canvas.bind("<B1-Motion>",self.creer_obstacles)
        self.list_colo=[]
        self.num_colo=0
        
    def creation(self,event):
        if Globals.cur_button=="Colonie":
            self.list_colo.append(Colonie.Colonie(event.x,event.y,50,self.num_colo,0,80,0,0,0,self.canvas))
            self.num_colo+=1
        elif Globals.cur_button=="Ressource":
            Globals.list_ressources.append(Ressource.Ressource(event.x,event.y,20,self.canvas))
        else:
            Globals.list_obst.append(Obstacle.Obstacle(event.x,event.y,self.canvas))
    
    def go(self):
        for colo in self.list_colo:
            colo.go()
            
    def stop(self):
        for colo in self.list_colo:
            colo.pause()
        for colo in self.list_colo:
            colo.stop()
            
    def pause(self):
        for colo in self.list_colo:
            colo.pause()
            
    def continuer(self):
        for colo in self.list_colo:
            colo.continuer()
    
    def creer_obstacles(self,event):
        if Globals.cur_button=="Obstacle":
            Globals.list_obst.append(Obstacle.Obstacle(event.x,event.y,self.canvas))
        