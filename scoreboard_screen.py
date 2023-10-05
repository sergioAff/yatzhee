from doctest import master
from tkinter.ttk import Frame
from tkinter import CENTER, END, Toplevel, ttk,Scrollbar,Button
from ranking import*
class ScoreboardScreen:

    def __init__(self,window1) -> None:
        self.window = Toplevel(master=window1)
        self.window.configure(bg = "#45c3de")
        self.obj=Ranking()
        self.scoreboard_frame = Frame(self.window)
        self.scoreboard_frame.grid(row=0, column=0, sticky="nsew")
        self.boton=Button(self.scoreboard_frame,text="Borrar",command=self.borrar,bg="maroon1", fg="snow")
        self.boton.grid(row=1,column=0)
        self.lista=[]
        self.score=ttk.Treeview(self.scoreboard_frame,columns=("col1","col2"))
        self.score.column("#0",width=80)
        self.score.column("col1",width=80,anchor=CENTER)
        self.score.column("col2",width=80,anchor=CENTER)
        self.score.heading("#0",text="Posición",anchor=CENTER)
        self.score.heading("col1",text="Jugador",anchor=CENTER)
        self.score.heading("col2",text="Puntos",anchor=CENTER)
        self.barradesplazamiento=Scrollbar(self.scoreboard_frame,command=self.score.yview)
        self.barradesplazamiento.grid(row=0,column=1,sticky="nsew")
        self.score.config(yscrollcommand=self.barradesplazamiento.set)
        self.insert()
        self.window.iconbitmap("unnamed.ico")
        self.window.grab_set()
        
        self.score.grid(row=0,column=0)
    
    def insert(self):
        
        self.lista=self.obj.Ordenar()
       
        for i in range(len(self.lista)):
            self.score.insert("",END,id=f"{i}",text=f"{i+1}",values=(f"{self.lista[i][0]}",f"{self.lista[i][1]}"))
            
        
    def borrar(self):
        
      s=self.score.selection() #selection devuelve una tupla de items uno es el indice del elemento que guarde
      eliminar=self.lista[int(s[0])][0] # lo que esta en self.lista es el nombre int(s[0]) es el indice pero selection lo devuelve como cadena
      self.obj.eliminar_elemento(eliminar) #elimino la llave 
      self.lista.remove(self.lista[int(s[0])]) #remuevo el elemento que habia creado mas arriba para que este actualizada en tiempo real 
      print(self.obj.getDicionario())
      self.obj.crearFichero() # creo un fichero actualizado para que lo lea denuvo y meta la infomacion en el treview
      self.score.grid_forget()
      self.score=ttk.Treeview(self.scoreboard_frame,columns=("col1","col2"))
      self.score.column("#0",width=80)
      self.score.column("col1",width=80,anchor=CENTER)
      self.score.column("col2",width=80,anchor=CENTER)
      self.score.heading("#0",text="Posición",anchor=CENTER)
      self.score.heading("col1",text="Jugador",anchor=CENTER)
      self.score.heading("col2",text="Puntos",anchor=CENTER)
      self.score.config(yscrollcommand=self.barradesplazamiento.set)
      self.score.grid(row=0,column=0)
      self.insert()
        
      
      
       