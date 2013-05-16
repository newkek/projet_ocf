import Monde
from tkinter import *
import Globals
import infoBulle

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

def setRessource():
    Globals.cur_button="Ressource"

def setColonie():
    Globals.cur_button="Colonie"
    
def setObstacle():
    Globals.cur_button="Obstacle"
    
def initialisation_interface(fenp):
    var_text=StringVar()
    var_text.set("Current status")

    Globals.entrys["value_nid"]=StringVar()
    Globals.entrys["value_nid"].set("50")

    Globals.entrys["value_food"]=StringVar()
    Globals.entrys["value_food"].set("20")

    Globals.entrys["value_speed"]=StringVar()
    Globals.entrys["value_speed"].set("10")

    Globals.entrys["value_endurance"]=StringVar()
    Globals.entrys["value_endurance"].set("75")

    Globals.entrys["value_evaporation"]=StringVar()
    Globals.entrys["value_evaporation"].set("50")

    Globals.entrys["value_vision"]=StringVar()
    Globals.entrys["value_vision"].set("3")


    Globals.im["Start_button"]=PhotoImage(file="./IMAGE/start.gif")
    Globals.im["Pause_button"]=PhotoImage(file="./IMAGE/pause.gif")
    Globals.im["Stop_button"]=PhotoImage(file="./IMAGE/Stop.gif")
    Globals.im["Obstacle_button"]=PhotoImage(file="./IMAGE/obstacle.gif")

    ########################################Bloc left####################################""
    
    bloc2=Frame(fenp,bd=2,relief="groove")
    bloc2.grid(row=2,rowspan=8,column=0)

    b_nid=Button(bloc2,text="Colonie",width=10,command=setColonie)
    b_nid.grid(row=0,column=0)
    infoBulle.infoBulle(parent=b_nid,texte="Mode colonie")
    entry_nid=Entry(bloc2,justify=CENTER,textvariable=Globals.entrys["value_nid"],width=10)
    entry_nid.grid(row=1,column=0,padx=10,pady=10)
    infoBulle.infoBulle(parent=entry_nid,texte="Nombre de fourmies/nid")
    
    
    b_food=Button(bloc2,text="Ressource",width=10,command=setRessource)
    b_food.grid(row=2,column=0)
    infoBulle.infoBulle(parent=b_food,texte="Mode ressource")
    entry_food=Entry(bloc2,justify=CENTER,textvariable=Globals.entrys["value_food"],width=10)
    entry_food.grid(row=3,column=0,pady=10)
    infoBulle.infoBulle(parent=entry_food,texte="Quantité de ressource")
    
    
    b_obstacle=Button(bloc2,text="Obstacle",command=setObstacle,image=Globals.im["Obstacle_button"])
    b_obstacle.grid(row=4,column=0,padx=10)
    infoBulle.infoBulle(parent=b_obstacle,texte="Mode obstacle")


    #########################################Bloc Top###################################


    bloc1=Frame(fenp,relief="groove",bd=2)
    bloc1.grid(row=0,column=1,columnspan=3)



    b_quit=Button(bloc1,text="Quitter",command=stop_monde,image=Globals.im["Stop_button"])
    b_quit.grid(row=0,column=3,padx=10)
    infoBulle.infoBulle(parent=b_quit,texte="Quitter")
    
    Globals.buttons["b_start"]=Button(bloc1,text="Start",command=go_monde,image=Globals.im["Start_button"],state="disable")
    Globals.buttons["b_start"].grid(row=0,column=1,padx=10,pady=5)
    infoBulle.infoBulle(parent=Globals.buttons["b_start"],texte="Lancer")
    
    Globals.buttons["b_stop"]=Button(bloc1,text="Pause",command=pause_monde,image=Globals.im["Pause_button"],state="disable")
    Globals.buttons["b_stop"].grid(row=0,column=2)
    infoBulle.infoBulle(parent=Globals.buttons["b_stop"],texte="Suspendre")

    #########################################Bloc right##################################
    
    bloc3=Frame(fenp,bd=2,relief="groove")
    bloc3.grid(row=2,rowspan=8,column=4)
    l_vitesse=Label(bloc3,text="Vitesse",width=10,bd=1,relief="raised")
    l_vitesse.grid(row=0,column=0,pady=5)
    entry_vitesse=Entry(bloc3,justify=CENTER,textvariable=Globals.entrys["value_speed"],width=10)
    entry_vitesse.grid(row=1,column=0,padx=10,pady=10)
    
    l_endurance=Label(bloc3,text="Endurance",width=10,bd=1,relief="raised")
    l_endurance.grid(row=2,column=0)
    entry_endurance=Entry(bloc3,justify=CENTER,textvariable=Globals.entrys["value_endurance"],width=10)
    entry_endurance.grid(row=3,column=0,padx=10,pady=10)
 
    
    l_evaporation=Label(bloc3,text="Evaporation",width=10,bd=1,relief="raised")
    l_evaporation.grid(row=4,column=0)
    entry_evaporation=Entry(bloc3,justify=CENTER,textvariable=Globals.entrys["value_evaporation"],width=10)
    entry_evaporation.grid(row=5,column=0,padx=10,pady=10)

    
    l_vision=Label(bloc3,text="Vision",width=10,bd=1,relief="raised")
    l_vision.grid(row=6,column=0)
    entry_vision=Entry(bloc3,justify=CENTER,textvariable=Globals.entrys["value_vision"],width=10)
    entry_vision.grid(row=7,column=0,pady=10)

    
    message=Label(fenp,textvariable=var_text)
    message.grid(row=28,column=1,columnspan=3)

fenp=Tk()
fenp.title('Optimisation par colonie de fourmies. GALLARDO Kevin, DEVIN Anthony. L3 SI')

initialisation_interface(fenp)
global monde
monde=Monde.Monde(fenp)
fenp.mainloop()