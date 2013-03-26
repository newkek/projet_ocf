from tkinter import *
import Colonie
import Obstacle
import Globals
import Ressource


class infoBulle(Toplevel):
	def __init__(self,parent=None,texte='',temps=1000):
		Toplevel.__init__(self,parent,bd=1,bg='black')
		self.tps=temps
		self.parent=parent
		self.withdraw()
		self.overrideredirect(1)
		self.transient()     
		l=Label(self,text=texte,bg="yellow",justify='left')
		l.update_idletasks()
		l.pack()
		l.update_idletasks()
		self.tipwidth = l.winfo_width()
		self.tipheight = l.winfo_height()
		self.parent.bind('<Enter>',self.delai)
		self.parent.bind('<Button-1>',self.efface)
		self.parent.bind('<Leave>',self.efface)
	def delai(self,event):
		self.action=self.parent.after(self.tps,self.affiche)
	def affiche(self):
		self.update_idletasks()
		posX = self.parent.winfo_rootx()+self.parent.winfo_width()
		posY = self.parent.winfo_rooty()+self.parent.winfo_height()
		if posX + self.tipwidth > self.winfo_screenwidth():
			posX = posX-self.winfo_width()-self.tipwidth
		if posY + self.tipheight > self.winfo_screenheight():
			posY = posY-self.winfo_height()-self.tipheight
		#~ print posX,print posY
		self.geometry('+%d+%d'%(posX,posY))
		self.deiconify()
	def efface(self,event):
		self.withdraw()
		self.parent.after_cancel(self.action)

