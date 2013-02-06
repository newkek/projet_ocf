from tkinter import *
import Colonie
import Obstacle


class Monde:
    def __init__(self,fenp):
        self.canvas=Canvas(fenp,width=500,height=500,bg="white")
        self.canvas.pack()
        cur_button="Chaine correspondant au bouton d'option actif"
        self.canvas.bind('<Button-1>',self.creation)
        self.canvas.bind('<Button-2>',self.go)
        self.canvas.bind('<Double-Button-1>',quit)
        self.list_colo=[]
        self.num_colo=0
        self.list_obst=[]
        
    def creation(self,event):
        
        self.list_colo.append(Colonie.Colonie(event.x,event.y,100,self.num_colo,0,0,0,0,0,self.canvas))
        self.num_colo+=1
        #print(event.x,event.y)
    
    def go(self,event):
        for colo in self.list_colo:
            colo.go()
    
    def creer_obstacle(self,event):
        self.list_obst.append(Obstacle.Obstacle(event.x,event.y,self.canvas))
        