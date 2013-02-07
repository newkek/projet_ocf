import Monde
from tkinter import *
global start_clic
start_clic=False

def go_monde():
    global monde
    global start_clic
    if start_clic is not True:
        start_clic=True
        monde.go()
    else:
        monde.continuer()
    
    
def stop_monde():
    global monde
    monde.stop()
    quit()
        
def pause_monde():
    global monde
    monde.pause()
    b_start.configure(text="Reprendre")
    
def initialisation_interface(fenp):
    var_text=StringVar()
    var_text.set("Current status")
    
    value_nid=StringVar()
    value_nid.set("50")
    
    value_food=StringVar()
    value_food.set("100")
    
    value_speed=StringVar()
    value_speed.set("10")
    
    value_endurance=StringVar()
    value_endurance.set("10")
    
    value_evaporation=StringVar()
    value_evaporation.set("10")
    
    value_vision=StringVar()
    value_vision.set("10")
    
    #monde=Canvas(height=500,width=500,bg="white")
    #monde.grid(row=2,rowspan=25,column=1,columnspan=3)
    
    b_nid=Button(fenp,text="Nid",width=10)
    b_nid.grid(row=2,column=0)
    entry_nid=Entry(fenp,textvariable=value_nid,width=10)
    entry_nid.grid(row=3,column=0)
    
    b_food=Button(fenp,text="Ressource",width=10)
    b_food.grid(row=4,column=0)
    entry_food=Entry(fenp,textvariable=value_food,width=10)
    entry_food.grid(row=5,column=0)
    
    b_obstacle=Button(fenp,text="Obstacle",width=10)
    b_obstacle.grid(row=6,column=0)
    
    b_pas=Button(fenp,text="Pas",width=10,command=stop_monde)
    b_pas.grid(row=0,column=1)
    
    b_start=Button(fenp,text="Start",width=10,command=go_monde)
    b_start.grid(row=0,column=2)
    
    b_stop=Button(fenp,text="Pause",width=10,command=pause_monde)
    b_stop.grid(row=0,column=3)
    
    l_vitesse=Label(fenp,text="Vitesse",width=10)
    l_vitesse.grid(row=2,column=19)
    entry_vitesse=Entry(fenp,textvariable=value_speed,width=10)
    entry_vitesse.grid(row=3,column=19)
    
    l_endurance=Label(fenp,text="Endurance",width=10)
    l_endurance.grid(row=4,column=19)
    entry_endurance=Entry(fenp,textvariable=value_endurance,width=10)
    entry_endurance.grid(row=5,column=19)
    
    l_evaporation=Label(fenp,text="Evaporation",width=10)
    l_evaporation.grid(row=6,column=19)
    entry_evaporation=Entry(fenp,textvariable=value_evaporation,width=10)
    entry_evaporation.grid(row=7,column=19)
    
    l_vision=Label(fenp,text="Vision",width=10)
    l_vision.grid(row=8,column=19)
    entry_vision=Entry(fenp,textvariable=value_vision,width=10)
    entry_vision.grid(row=9,column=19)
    
    frame_vide=Frame(fenp,relief="flat",height="10",width="130",bg="black")
    frame_vide.grid(row=1,column=1)
    
    message=Label(fenp,textvariable=var_text)
    message.grid(row=28,column=1,columnspan=3)

fenp=Tk()
initialisation_interface(fenp)
global monde
monde=Monde.Monde(fenp)
fenp.mainloop()