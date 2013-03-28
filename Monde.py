from tkinter import *
import Colonie
import Obstacle
import Globals
import Ressource
import time
import threading


global terminated
terminated=False


def evap(canvas):
    time.sleep(2)
    global terminated
    while terminated is False:
        if (Globals.list_pher):
            for pher in Globals.list_pher:
                cur=pher.evaporation()
                if cur==0:
                    canvas.delete(pher.id_canvas)
                    time.sleep(0.01)
            time.sleep(0.5)
        else:
            time.sleep(1)
                
                


class Monde:
    def __init__(self,fenp):
        self.canvas=Canvas(fenp,width=Globals.canvas_size,height=Globals.canvas_size,bg="gray59",bd=2,relief="sunken")
        self.canvas.grid(row=2,rowspan=25,column=1,columnspan=3)
        self.canvas.bind('<Button-1>',self.creation)
        self.canvas.bind("<B1-Motion>",self.creer_obstacles)
        self.list_colo=[]
        self.num_colo=0
        self.deroul_eval=0
        
    def creation(self,event):
        if Globals.cur_button=="Colonie":
            self.list_colo.append(Colonie.Colonie(event.x,event.y,int(Globals.entrys["value_nid"].get()),self.num_colo,int(Globals.entrys["value_speed"].get()),int(Globals.entrys["value_endurance"].get()),int(Globals.entrys["value_evaporation"].get()),0,int(Globals.entrys["value_vision"].get()),self.canvas))
            self.num_colo+=1
            Globals.buttons["b_start"].configure(state="normal")
            Globals.buttons["b_stop"].configure(state="normal")

        elif Globals.cur_button=="Ressource":
            Globals.list_ressources.append(Ressource.Ressource(event.x,event.y,int(Globals.entrys["value_food"].get()),self.canvas))
        else:
            Globals.list_obst.append(Obstacle.Obstacle(event.x,event.y,self.canvas))
        
    def go(self):
        for colo in self.list_colo:
            colo.go()
        self.deroul_eval=threading.Thread(None,evap,None,(self.canvas,),{})
        self.deroul_eval.start()
        
    def stop(self):
        global terminated
        terminated=True
        for colo in self.list_colo:
            colo.pause()
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
        