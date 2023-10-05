from Dado import *
class Logic:
    """clase que tiene el objetivo de calcular los puntos obtenidos en cada tirada mediante sus metodos tambien tiene
       la responsabilidad de lanzar los dados los 5 dados
    Attributes:
        dado1(object): [dado que pertenece a la clase Dado]
        dado2(object): [dado que pertenece a la clase Dado]
        dado3(object): [dado que pertenece a la clase Dado]
        dado4(object): [dado que pertenece a la clase Dado]
        dado5(object): [dado que pertenece a la clase Dado]"""
    def __init__(self):
        self.__dado1=Dado()
        self.__dado2=Dado() 
        self.__dado3=Dado()
        self.__dado4=Dado()
        self.__dado5=Dado()   
    
    #esta funcion se encargara de rodar los 5 dados
    def Rodar_5_Dados(self):
        """este metodo se encargar de rodar los dados que no esten detenidos"""
        self.__dado1.rodar_dados()
        self.__dado2.rodar_dados()
        self.__dado3.rodar_dados()
        self.__dado4.rodar_dados()
        self.__dado5.rodar_dados()
    
    def estadoTrue(self):
        """este metodo cambia el estado de los dados a True 
           esto significa que si los lanzas todos rodaran"""
        self.__dado1.EstadoTrue()
        self.__dado2.EstadoTrue()
        self.__dado3.EstadoTrue()
        self.__dado4.EstadoTrue()
        self.__dado5.EstadoTrue()    
    #funcion que devuelve el valor de los dados
    def listaValores(self):
        """La funcion de este metodo como su nombre indica es crear una lista con los valores de los dados en tiempo real
           para que los demas metodos trabajen con esa informacion 
        Returns:
            list"""
        dados=[self.__dado1, self.__dado2, self.__dado3, self.__dado4, self.__dado5]
        l=[]
        for i in dados:
            l.append(i.getvalor())
        return l

    #interruptores logicos de los dados seran utilizados en la interfaz 
    def interruptor1(self):   # dado1
        """modifica el estado del dado si su estado = True lo cambiara a estado=False y si estado= False lo volvera True
           haciendo como un interruptor"""
        self.__dado1.interruptor()
    
    def interruptor2(self):   # dado2
        """modifica el estado del dado si su estado = True lo cambiara a estado=False y si estado= False lo volvera True
           haciendo como un interruptor"""
        self.__dado2.interruptor()
    def interruptor3(self):   # dado3
        """modifica el estado del dado si su estado = True lo cambiara a estado=False y si estado= False lo volvera True
           haciendo como un interruptor"""
        self.__dado3.interruptor()
    
    def interruptor4(self):   # dado4
        """modifica el estado del dado si su estado = True lo cambiara a estado=False y si estado= False lo volvera True
           haciendo como un interruptor"""
        self.__dado4.interruptor()     
                
    def interruptor5(self):   # dado5
        """modifica el estado del dado si su estado = True lo cambiara a estado=False y si estado= False lo volvera True
           haciendo como un interruptor"""
        self.__dado5.interruptor()    
    #gets
    def Dado1GetEstado(self):
        """devuelve el estado del dado 1
        Returns:
            boolean"""
        return self.__dado1.getestado()
    
    def Dado2GetEstado(self):
        """devuelve el estado del dado 1
        Returns:
            boolean"""
        return self.__dado2.getestado()
    
    def Dado3GetEstado(self):
        """devuelve el estado del dado 1
        Returns:
            boolean"""
        return self.__dado3.getestado()
    def Dado4GetEstado(self):
        """devuelve el estado del dado 1
        Returns:
            boolean"""
        return self.__dado4.getestado()
    
    def Dado5GetEstado(self):
        """devuelve el estado del dado 1
        Returns:
            boolean"""
        return self.__dado5.getestado()
    
     # ===comprobadores===      
    def GetYatzy(self): 
        """devuelve el Yatzy, en caso de existir retorna 50 si no retorna 0
        Returns:
            int"""
        if len(set(self.listaValores()))==1:
            return 50
        return 0
    
    # numeros:
    def GetUno(self):
        """devuelve el resultado de la suma de todos los unos en caso de extistir si no existe retornara 0
        Returns:
            int"""
        s=0
        for i in self.listaValores():
            if i == 1:
                s+=i
        return s
    
    def GetDos(self):
        """devuelve el resultado de la suma de todos los dos en caso de extistir si no existe retornara 0
        Returns:
            int"""
        s=0
        for i in self.listaValores():
            if i == 2:
                s+=i
        return s
    
    def GetTres(self):
        """devuelve el resultado de la suma de todos los tres en caso de extistir si no existe retornara 0
        Returns:
            int"""
        s=0
        for i in self.listaValores():
            if i == 3:
                s+=i  
        return s
    
    def GetCuatro(self):
        """devuelve el resultado de la suma de todos los cuatro en caso de extistir si no existe retornara 0
        Returns:
            int"""
        s=0
        for i in self.listaValores():
           if i == 4:
               s+=i
        return s
    
    def GetCinco(self):
        """devuelve el resultado de la suma de todos los cinco en caso de extistir si no existe retornara 0
        Returns:
            int"""
        s=0
        for i in self.listaValores():
            if i == 5:
              s+=i  
        return s    
    
    def GetSeis(self):
        """devuelve el resultado de la suma de todos los unos en caso de extistir si no existe retornara 0
        Returns:
            int"""
        s=0
        for i in self.listaValores():
            if i == 6:
              s+=i  
        return s
   
    # combinaciones:
    def GetFull(self):
        """verifica la existencia de una pareja y un trio si existe retornara 25 si no retornara 0
        Returns:
            int"""
        l=self.listaValores()
        l.sort()
        s=0
        if len(set(l))!=2:
            return s
        if l[0]!=l[3] and l[1]!=l[4]:
            s=25
        return s
    
    def GetEscaleraMay(self):
        """verifica la existencia de una escalera mayor en caso de existir retorna 20 si no retornara 0
        Returns:
            int"""
        l=self.listaValores()
        l.sort()
        if len(set(l))==5 and l[4]==6 and l[0]==2:             
            return 20
        return 0
    
    def GetEscaleraMenor(self):
        """verifica la existencia de una escalera menor en caso de existir retorna 15 si no retornara 0
        Returns:
            int"""
        l=self.listaValores()
        l.sort()
        if len(set(l))==5 and l[4]==5 and l[0]==1:
            return 15
        return 0
    
    def GetPoker(self):
        """verifica la existencia de un poker en caso de existir retorna la suma de los cuatro dados  si no retornara 0
        Returns:
            int"""
        l=self.listaValores()
        l.sort()
        s=0
        if l[0]==l[3]:
            s=sum(l[0:4])
        if l[1]==l[4]:
            s=sum(l[1:5])
        return s

    def GetTrio(self):
      """verifica la existencia de un trio en caso de existir retorna la suma de los tres dados  si no retornara 0
        Returns:
            int"""
      l=self.listaValores()
      l.sort() 
      s=0
      if l[0]==l[2]:
        s=sum(l[0:3]) 
      if l[1]==l[3]:
        s=sum(l[1:4])
      if l[2]==l[4]:
        s=sum(l[2:5])  
      return s      
    
    def Get_Dos_Pares(self):
        """verifica la existencia de dos pares diferentes en caso de existir retorna la suma de los dos   si no retornara 0
        Returns:
            int"""
        l=self.listaValores()
        l.sort()
        s=0
        if l[0]==l[1] and l[2]==l[3]:
            s=sum(l[0:4])
            
        if l[0]==[1] and l[3]==l[4]:
            s=sum(l[0:2])+sum(l[3:5])
            
        if l[1]==l[2] and l[3]==l[4]:
            s= sum(l[1:5])
        return s       
    
    def GetPar(self):
        """verifica la existencia de una pareja en caso de existir dos retorna la suma de la de mayor valor y si existe una  
         retorna la suma de esa si no retornara 0
        Returns:
            int"""          
        l=self.listaValores()
        l.sort()
        s=0
        if l[0]==l[1] :
            s=sum(l[0:2])
        if l[1]==l[2]:
            s=sum(l[1:3])
        if l[2]==l[3]:
            s=sum(l[2:4])
        if l[3]==l[4]:
            s=sum(l[3:5])
        if l[0]==l[1] and l[2]==l[3] and sum(l[0:2])> sum(l[2:4]):
            s=sum(l[0:2])
        if l[0]==l[1] and l[2]==l[3] and sum(l[0:2])< sum(l[2:4]):
            s=sum(l[2:4])
        if l[0]==[1] and l[3]==l[4] and sum(l[0:2])>sum(l[3:5]):
            s=sum(l[0:2])
        if l[0]==[1] and l[3]==l[4] and sum(l[0:2])<sum(l[3:5]):
            s=sum(l[3:5])
        if l[1]==l[2] and l[3]==l[4] and sum(l[1:3])>sum(l[3:5]):
            s=sum(l[1:3])
        if l[1]==l[2] and l[3]==l[4] and sum(l[1:3])<sum(l[3:5]):
            s=sum(l[3:5])
        
        return s
    
    def GetLibre(self):
        """su objetivo es calcular la suma de todos los dados
        Returns:
            int"""
        s=0
        for i in self.listaValores():
            s+=i
        return s