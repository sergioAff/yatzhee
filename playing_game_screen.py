from tkinter import *
from tkinter import messagebox 
from logica import *
from AlmacenDePuntos import *
from ranking import*
class PlayingGameScreen:
    def __init__(self, players: list[str]) -> None:
        self.window=Toplevel()
        self.window.resizable(False, False)
        self.window.iconbitmap("unnamed.ico")
        self.window.grab_set()
        self.imagen1=PhotoImage(file=(f"dado1.png"))
        self.imagen2=PhotoImage(file=(f"dado2.png"))
        self.imagen3=PhotoImage(file=(f"dado3.png"))
        self.imagen4=PhotoImage(file=(f"dado4.png"))
        self.imagen5=PhotoImage(file=(f"dado5.png"))
        self.imagen6=PhotoImage(file=(f"dado6.png"))
        self.listaImagen=[self.imagen1,self.imagen2,self.imagen3,self.imagen4,self.imagen5,self.imagen6]
        
        self.playing_game_frame = Frame(self.window)
        self.frame_inferior=Frame(self.window)
        self.ultimoframe=Frame(self.window)
        self.object_logical=Logic()
        self.objects_almacen = []
#========variables=============================       
        self.turno=0
        self.lanzamiento=0
        
        for i in players:
            self.objetoAl=AlmacenDePuntos(i,self.object_logical)
            self.objects_almacen.append(self.objetoAl)
#========Variables stringsVar==================
        self.StringsVar=[]
        for i in range(21):
         s=StringVar()
         self.StringsVar.append(s)
        self.todosEnCero()
        self.playersNameSt=StringVar()
        self.playersNameSt.set(self.objects_almacen[self.turno].getName())
        self.puntosSt=StringVar()
        self.puntosSt.set(self.objects_almacen[self.turno].puntTemp())
        
        self.playersName=Label(self.playing_game_frame,textvariable=self.playersNameSt,width=6)    
        self.nombre_label=Label(self.playing_game_frame,text="JUGADOR: ")
        self.puntos_label=Label(self.playing_game_frame, text= "PUNTUACION TOTAL")
        self.mostrarPuntos=Label(self.playing_game_frame, textvariable=self.puntosSt,width=6)    
        
        self.playing_game_frame.grid(row=0, column=0)
        self.frame_inferior.grid(row=1,column=0)
        self.ultimoframe.grid(row=2,column=0)
        self.nombre_label.grid(row=0,column=0,padx=5,pady=5)
        self.playersName.grid(row=0,column=1,padx=5,pady=5)
        self.puntos_label.grid(row=0,column=2,padx=5,pady=5)
        self.mostrarPuntos.grid(row=0, column=3,padx=5,pady=5)

#====================================================================================================================================================
#                                               botones de combinacion 
#====================================================================================================================================================
        self.boton_uno=Button(self.playing_game_frame,text="UNO",width=12,command=self.BotonUno)
        self.boton_dos=Button(self.playing_game_frame,text="DOS",width=12,command=self.BotonDos)    
        self.boton_tres=Button(self.playing_game_frame, text="TRES",width=12,command=self.BotonTres)
        self.boton_cuatro=Button(self.playing_game_frame, text="CUATRO",width=12,command=self.BotonCuatro)
        self.boton_cinco=Button(self.playing_game_frame, text="CINCO",width=12,command=self.BotonCinco)
        self.boton_seis=Button(self.playing_game_frame, text="SEIS",width=12,command=self.BotonSeis)
        self.boton_Par=Button(self.playing_game_frame, text="PAR",width=12,command=self.BotonPar)
        self.boton_2Par=Button(self.playing_game_frame, text="2 PARES",width=12,command=self.Boton2par)
        self.boton_trio=Button(self.playing_game_frame, text="TRIO",width=12,command=self.BotonTrio)
        self.boton_poker=Button(self.playing_game_frame, text="POKER",width=12,command=self.BotonPoker)
        self.boton_escalera_menor=Button(self.playing_game_frame, text="Escalera Menor",width=12,command=self.BotonEscaleraMen)
        self.boton_escalera_mayor=Button(self.playing_game_frame, text="Escalera Mayor",width=12,command=self.BotonEscaleraMay)
        self.boton_full=Button(self.playing_game_frame, text="Full",width=12,command=self.BotonFull)
        self.boton_libre=Button(self.playing_game_frame, text="Libre",width=12,command=self.BotonLibre)
        self.boton_yahtzee=Button(self.playing_game_frame, text="Yahtzee",width=12,command=self.BotonYahtzee)
        self.desactivarCombina()
#====================================================================================================================================================
#                                               posicion de botones
#====================================================================================================================================================
        self.boton_uno.grid(row=1,column=0,padx=5,pady=5)
        self.boton_dos.grid(row=2,column=0,padx=5,pady=5)
        self.boton_tres.grid(row=3,column=0,padx=5,pady=5)
        self.boton_cuatro.grid(row=4,column=0,padx=5,pady=5)
        self.boton_cinco.grid(row=5,column=0,padx=5,pady=5)
        self.boton_seis.grid(row=6,column=0,padx=5,pady=5)
        self.boton_Par.grid(row=1,column=2,padx=5,pady=5)
        self.boton_2Par.grid(row=2,column=2,padx=5,pady=5)
        self.boton_trio.grid(row=3,column=2,padx=5,pady=5)
        self.boton_poker.grid(row=4,column=2,padx=5,pady=5)
        self.boton_escalera_menor.grid(row=5,column=2,padx=5,pady=5)
        self.boton_escalera_mayor.grid(row=6,column=2,padx=5,pady=5)
        self.boton_full.grid(row=1,column=4,padx=5,pady=5)
        self.boton_libre.grid(row=3,column=4,padx=5,pady=5)
        self.boton_yahtzee.grid(row=2,column=4,padx=5,pady=5)
#====================================================================================================================================================
#                                                 labels
#====================================================================================================================================================
        self.label_uno=Label(self.playing_game_frame,textvariable=self.StringsVar[0],width=6)
        self.label_dos=Label(self.playing_game_frame,textvariable=self.StringsVar[1],width=6)
        self.label_tres=Label(self.playing_game_frame,textvariable=self.StringsVar[2],width=6)
        self.label_cuatro=Label(self.playing_game_frame,textvariable=self.StringsVar[3],width=6)
        self.label_cinco=Label(self.playing_game_frame,textvariable=self.StringsVar[4],width=6)
        self.label_seis=Label(self.playing_game_frame,textvariable=self.StringsVar[5],width=6)
        self.label_par=Label(self.playing_game_frame,textvariable=self.StringsVar[6],width=6)
        self.label_2par=Label(self.playing_game_frame,textvariable=self.StringsVar[7],width=6)
        self.label_trio=Label(self.playing_game_frame,textvariable=self.StringsVar[8],width=6)
        self.label_poker=Label(self.playing_game_frame,textvariable=self.StringsVar[9],width=6)
        self.label_escalera_menor=Label(self.playing_game_frame,textvariable=self.StringsVar[10],width=6)
        self.label_escalera_mayor=Label(self.playing_game_frame,textvariable=self.StringsVar[11],width=6)
        self.label_full=Label(self.playing_game_frame,textvariable=self.StringsVar[12],width=6)
        self.label_libre=Label(self.playing_game_frame,textvariable=self.StringsVar[13],width=6)
        self.label_yahtzee=Label(self.playing_game_frame,textvariable=self.StringsVar[14],width=6)
        self.actualizarPuntos()
#====================================================================================================================================================
#                                               grids de los labels
#====================================================================================================================================================
        self.label_uno.grid(row=1,column=1,padx=5,pady=5)
        self.label_dos.grid(row=2,column=1,padx=5,pady=5)
        self.label_tres.grid(row=3,column=1,padx=5,pady=5)
        self.label_cuatro.grid(row=4,column=1,padx=5,pady=5)
        self.label_cinco.grid(row=5,column=1,padx=5,pady=5)
        self.label_seis.grid(row=6,column=1,padx=5,pady=5)
        self.label_par.grid(row=1,column=3,padx=5,pady=5)
        self.label_2par.grid(row=2,column=3,padx=5,pady=5)
        self.label_trio.grid(row=3,column=3,padx=5,pady=5)
        self.label_poker.grid(row=4,column=3,padx=5,pady=5)
        self.label_escalera_menor.grid(row=5,column=3,padx=5,pady=5)
        self.label_escalera_mayor.grid(row=6,column=3,padx=5,pady=5)
        self.label_full.grid(row=1,column=5,padx=5,pady=5)
        self.label_libre.grid(row=3,column=5,padx=5,pady=5)
        self.label_yahtzee.grid(row=2,column=5,padx=5,pady=5)
        
#====================================================================================================================================================
#                                                             Frame inferior
#====================================================================================================================================================
        self.label1=Label(self.frame_inferior)
        self.label2=Label(self.frame_inferior)
        self.label3=Label(self.frame_inferior)           #hecho
        self.label4=Label(self.frame_inferior)
        self.label5=Label(self.frame_inferior)
        self.interruptor1=Button(self.frame_inferior,text="HOLD",width=10,command=self.BotonInterruptor1,bg="tomato")
        self.interruptor2=Button(self.frame_inferior,text="HOLD",width=10,command=self.BotonInterruptor2,bg="tomato")
        self.interruptor3=Button(self.frame_inferior,text="HOLD",width=10,command=self.BotonInterruptor3,bg="tomato")
        self.interruptor4=Button(self.frame_inferior,text="HOLD",width=10,command=self.BotonInterruptor4,bg="tomato")
        self.interruptor5=Button(self.frame_inferior,text="HOLD",width=10,command=self.BotonInterruptor5,bg="tomato")
        #grids
        self.label1.grid(row=0,column=0,padx=5,pady=5)
        self.label2.grid(row=0,column=1,padx=5,pady=5)
        self.label3.grid(row=0,column=2,padx=5,pady=5)
        self.label4.grid(row=0,column=3,padx=5,pady=5)
        self.label5.grid(row=0,column=4,padx=5,pady=5)
        self.interruptor1.grid(row=1,column=0,padx=5,pady=5)
        self.interruptor2.grid(row=1,column=1,padx=5,pady=5)
        self.interruptor3.grid(row=1,column=2,padx=5,pady=5)
        self.interruptor4.grid(row=1,column=3,padx=5,pady=5)
        self.interruptor5.grid(row=1,column=4,padx=5,pady=5)
#====================================================================================================================================================
#                                                             ultimo Frame
#====================================================================================================================================================
        self.lanzar_dados=Button(self.ultimoframe,text="lanzar",width=20,command=self.LanzarDados)
        self.lanzar_dados.grid(row=0,column=0,padx=10,pady=10)
        self.numero=Label(self.ultimoframe,textvariable=self.StringsVar[20])        #hecho
        self.numero.grid(row=0,column=1,padx=10,pady=10)       
    

    def playerNameLabel(self):
      if self.turno>=len(self.objects_almacen):
         self.turno=0
      
      self.playersNameSt.set(self.objects_almacen[self.turno].getName())
    
    def BotonInterruptor1(self):
      if self.lanzamiento>0:
         self.object_logical.interruptor1()
         if self.object_logical.Dado1GetEstado():
            self.interruptor1.config(bg="tomato")
         else:
            self.interruptor1.config(bg="medium sea green")
    def BotonInterruptor2(self):
      if self.lanzamiento>0:
         self.object_logical.interruptor2()
         if self.object_logical.Dado2GetEstado():
            self.interruptor2.config(bg="tomato")
         else:
            self.interruptor2.config(bg="medium sea green")
    def BotonInterruptor3(self):
      if self.lanzamiento>0:
         self.object_logical.interruptor3()
         if self.object_logical.Dado3GetEstado():
            self.interruptor3.config(bg="tomato")
         else:
            self.interruptor3.config(bg="medium sea green")
    def BotonInterruptor4(self):
      if self.lanzamiento>0:
         self.object_logical.interruptor4()
         if self.object_logical.Dado4GetEstado():
            self.interruptor4.config(bg="tomato")
         else:
            self.interruptor4.config(bg="medium sea green")
    def BotonInterruptor5(self):
      if self.lanzamiento>0:
         self.object_logical.interruptor5()
         if self.object_logical.Dado5GetEstado():
            self.interruptor5.config(bg="tomato")
         else:
            self.interruptor5.config(bg="medium sea green") 
        
    
    def LanzarDados(self):
      if self.lanzamiento<3:
         self.object_logical.Rodar_5_Dados()
         self.playerNameLabel()
         self.mostrarLabel_uno()
         self.mostrarLabel_dos()
         self.mostrarLabel_tres()
         self.mostrarLabel_cuatro()
         self.mostrarLabel_cinco()
         self.mostrarLabel_seis()
         self.mostrarLabel_par()
         self.mostrarLabel_2par()
         self.mostrarLabel_trio()
         self.mostrarLabel_poker()
         self.mostrarLabel_escaleraMen()
         self.mostrarLabel_escaleraMay()
         self.mostrarLabel_full()
         self.mostrarLabel_libre()
         self.mostrarLabel_yahtzee()
         self.mostrarDados()
         self.lanzamiento+=1
         if self.lanzamiento==3:
            self.lanzar_dados.config(state="disabled")
         self.StringsVar[20].set(f"lanzamiento: {self.lanzamiento}")
         
#====================================================================================================================================================
#                                                             metodos para hacer Funcionar a los labels
#====================================================================================================================================================               
    def mostrarDados(self):
      l=self.object_logical.listaValores()
      
      listaImag=[]
      for i in l:
         if i==1:
            imagen=self.listaImagen[0]
         if i==2:
            imagen=self.listaImagen[1]
         if i==3:
            imagen=self.listaImagen[2]
         if i==4:
            imagen=self.listaImagen[3]
         if i==5:
            imagen=self.listaImagen[4]
         if i==6:
            imagen=self.listaImagen[5]
         listaImag.append(imagen)
      self.label1.grid_forget()
      self.label1=Label(self.frame_inferior,image=listaImag[0])
      self.label1.grid(row=0,column=0,padx=5,pady=5,sticky="nsew")
      self.label2.grid_forget()
      self.label2=Label(self.frame_inferior,image=listaImag[1])
      self.label2.grid(row=0,column=1,padx=5,pady=5,sticky="nsew")
      self.label3.grid_forget()
      self.label3=Label(self.frame_inferior,image=listaImag[2])
      self.label3.grid(row=0,column=2,padx=5,pady=5,sticky="nsew")
      self.label4.grid_forget()
      self.label4=Label(self.frame_inferior,image=listaImag[3])
      self.label4.grid(row=0,column=3,padx=5,pady=5,sticky="nsew")
      self.label5.grid_forget()
      self.label5=Label(self.frame_inferior,image=listaImag[4])
      self.label5.grid(row=0,column=4,padx=5,pady=5,sticky="nsew")
    
    def mostrarLabel_uno(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["uno"]==None:
         self.boton_uno.config(state="normal")
         self.StringsVar[0].set(self.object_logical.GetUno())
      else:
         self.StringsVar[0].set(l["uno"])
         self.boton_uno.config(state="disabled")

    def mostrarLabel_dos(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["dos"]==None:
         self.boton_dos.config(state="normal")
         self.StringsVar[1].set(self.object_logical.GetDos())
      else:
         self.StringsVar[1].set(l["dos"])
         self.boton_dos.config(state="disabled")
    
    def mostrarLabel_tres(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["tres"]==None:
         self.boton_tres.config(state="normal")
         self.StringsVar[2].set(self.object_logical.GetTres())
      else:
         self.StringsVar[2].set(l["tres"])
         self.boton_tres.config(state="disabled")
    def mostrarLabel_cuatro(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["cuatro"]==None:
         self.boton_cuatro.config(state="normal")
         self.StringsVar[3].set(self.object_logical.GetCuatro())
      else:
         self.StringsVar[3].set(l["cuatro"])
         self.boton_cuatro.config(state="disabled")
    
    def mostrarLabel_cinco(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["cinco"]==None:
         self.boton_cinco.config(state="normal")
         self.StringsVar[4].set(self.object_logical.GetCinco())
      else:
         self.StringsVar[4].set(l["cinco"])
         self.boton_cinco.config(state="disabled")
    def mostrarLabel_seis(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["seis"]==None:
         self.boton_seis.config(state="normal")
         self.StringsVar[5].set(self.object_logical.GetSeis())
      else:
         self.StringsVar[5].set(l["seis"])
         self.boton_seis.config(state="disabled") 
    
    def mostrarLabel_par(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["1par"]==None:
         self.boton_Par.config(state="normal")
         self.StringsVar[6].set(self.object_logical.GetPar())
      else:
         self.StringsVar[6].set(l["1par"])
         self.boton_Par.config(state="disabled")
    
    def mostrarLabel_2par(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["2par"]==None:
         self.boton_2Par.config(state="normal")
         self.StringsVar[7].set(self.object_logical.Get_Dos_Pares())
      else:
         self.StringsVar[7].set(l["2par"])
         self.boton_2Par.config(state="disabled")
    
    def mostrarLabel_trio(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["trio"]==None:
         self.boton_trio.config(state="normal")
         self.StringsVar[8].set(self.object_logical.GetTrio())
      else:
         self.StringsVar[8].set(l["trio"])
         self.boton_trio.config(state="disabled")       
    
    def mostrarLabel_poker(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["poker"]==None:
         self.boton_poker.config(state="normal")
         self.StringsVar[9].set(self.object_logical.GetPoker())
      else:
         self.StringsVar[9].set(l["poker"])
         self.boton_poker.config(state="disabled")       
    
    def mostrarLabel_escaleraMen(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["EscaleraMen"]==None:
         self.boton_escalera_menor.config(state="normal")
         self.StringsVar[10].set(self.object_logical.GetEscaleraMenor())
      else:
         self.StringsVar[10].set(l["EscaleraMen"])
         self.boton_escalera_menor.config(state="disabled")
    def mostrarLabel_escaleraMay(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["EscaleraMay"]==None:
         self.boton_escalera_mayor.config(state="normal")
         self.StringsVar[11].set(self.object_logical.GetEscaleraMay())
      else:
         self.StringsVar[11].set(l["EscaleraMay"])
         self.boton_escalera_mayor.config(state="disabled")
    
    def mostrarLabel_full(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["full"]==None:
         self.boton_full.config(state="normal")
         self.StringsVar[12].set(self.object_logical.GetFull())
      else:
         self.StringsVar[12].set(l["full"])
         self.boton_full.config(state="disabled")
    
    def mostrarLabel_libre(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["libre"]==None:
         self.boton_libre.config(state="normal")
         self.StringsVar[13].set(self.object_logical.GetLibre())
      else:
         self.StringsVar[13].set(l["libre"])
         self.boton_libre.config(state="disabled")    
    def mostrarLabel_yahtzee(self):
      l=self.objects_almacen[self.turno].getdicionario() 
      if l["yahtzee"]==None:
         self.boton_yahtzee.config(state="normal")
         self.StringsVar[14].set(self.object_logical.GetYatzy())
      else:
         self.StringsVar[14].set(l["yahtzee"])
         self.boton_yahtzee.config(state="disabled")    
#====================================================================================================================================================
#                                                             Metodos para hacer Funcionar los botones
#====================================================================================================================================================
    def BotonUno(self):
      self.objects_almacen[self.turno].uno()
      self.turno+=1
      self.lanzamiento=0
      self.botonesRojo()
      self.playerNameLabel()
      self.object_logical.estadoTrue()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonDos(self):
      self.objects_almacen[self.turno].dos()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonTres(self):
      self.objects_almacen[self.turno].tres()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame
      self.lanzar_dados.config(state="normal")

    def BotonCuatro(self):
      self.objects_almacen[self.turno].cuatro()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonCinco(self):
      self.objects_almacen[self.turno].cinco()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonSeis(self):
      self.objects_almacen[self.turno].seis()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonPar(self): 
      self.objects_almacen[self.turno].Par()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def Boton2par(self): 
      self.objects_almacen[self.turno].Dos_Pares()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame
      self.lanzar_dados.config(state="normal")

    def BotonTrio(self):
      self.objects_almacen[self.turno].Trio()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonPoker(self): 
      self.objects_almacen[self.turno].Poker()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonEscaleraMen(self): 
      self.objects_almacen[self.turno].EscaleraMen()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonEscaleraMay(self):
      self.objects_almacen[self.turno].EscaleraMay()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.lanzar_dados.config(state="normal")
      self.lanzamiento=0
      self.EndGame()

    def BotonFull(self):
      self.objects_almacen[self.turno].Full()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")

    def BotonLibre(self): 
      self.objects_almacen[self.turno].libre()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.playerNameLabel()
      self.todosEnCero()
      self.actualizarPuntos()
      self.desactivarCombina()
      self.EndGame()
      self.lanzamiento=0
      self.lanzar_dados.config(state="normal")

    def BotonYahtzee(self):
      self.objects_almacen[self.turno].yahtzee()
      self.botonesRojo()
      self.object_logical.estadoTrue()
      self.turno+=1
      self.lanzamiento=0
      self.playerNameLabel()
      self.actualizarPuntos()
      self.todosEnCero()
      self.desactivarCombina()
      self.EndGame()
      self.lanzar_dados.config(state="normal")
      
    def botonesRojo(self):
      self.interruptor1.config(bg="tomato")
      self.interruptor2.config(bg="tomato")
      self.interruptor3.config(bg="tomato")
      self.interruptor4.config(bg="tomato")
      self.interruptor5.config(bg="tomato")

    def desactivarCombina(self):
      self.boton_uno.config(state="disabled")
      self.boton_dos.config(state="disabled")
      self.boton_tres.config(state="disabled")
      self.boton_cuatro.config(state="disabled")
      self.boton_cinco.config(state="disabled")
      self.boton_seis.config(state="disabled")
      self.boton_Par.config(state="disabled")
      self.boton_2Par.config(state="disabled")
      self.boton_trio.config(state="disabled")
      self.boton_poker.config(state="disabled")
      self.boton_full.config(state="disabled")
      self.boton_libre.config(state="disabled")
      self.boton_escalera_mayor.config(state="disabled")
      self.boton_escalera_menor.config(state="disabled")
      self.boton_yahtzee.config(state="disabled")
      
    def todosEnCero(self):
      for i in range(15,20):
         self.StringsVar[i].set(0)
      self.StringsVar[20].set(f"Turno para: {self.objects_almacen[self.turno].getName()} ")
    def actualizarPuntos(self):
      c=-1
      l=self.objects_almacen[self.turno].getdicionario()
      for i in l.values():
         listaLabel=[self.label_uno,self.label_dos,self.label_tres,self.label_cuatro,self.label_cinco,self.label_seis,self.label_par,
         self.label_2par,self.label_trio,self.label_poker,self.label_escalera_menor,self.label_escalera_mayor,self.label_full,self.label_libre,
         self.label_yahtzee]
         c+=1
         if i==None:
            self.StringsVar[c].set("")
            listaLabel[c].config(bg="tomato")
         else:
            self.StringsVar[c].set(i)
            listaLabel[c].config(bg="medium sea green")
      self.puntosSt.set(self.objects_almacen[self.turno].puntTemp())
    def EndGame(self):
      c=0
      for i in self.objects_almacen:
         if i.EndGame():
            c+=1
      if c==len(self.objects_almacen):
         ranking=Ranking()
         l=[]
         for i in self.objects_almacen:
            l.append((i.getName(),i.puntTemp()))
            ranking.agregarpuntos(i.getName(),i)
         ranking.crearFichero()
         l.sort(key=lambda x: x[1],reverse=True) 
         messagebox.showinfo("Fin del juego",f"El ganador es: {l[0][0]} con {l[0][1]} puntos")
         self.window.destroy()

    
    
      