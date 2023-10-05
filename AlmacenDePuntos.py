from logica import *

class AlmacenDePuntos:
    """clase que se encarga de guardar las puntuaciones obtenidas de los dados
    Attributes:
            logica (object): [contiene los dados y los metodos para calcular los puntos]
            diccionario(dict): [diccionario para almacenar las puntuaciones ]
            name(str): [nombre del dueño de las puntuaciones] """
    def __init__(self,name,logica):
        #diccionario con los valores del jugador:
        self.__diccionario={"uno":None, "dos":None, "tres":None,
        "cuatro":None, "cinco":None, "seis":None, "1par":None, "2par":None,  
        "trio":None, "poker":None, "EscaleraMen":None, "EscaleraMay":None, "full":None,
        "libre":None, "yahtzee":None }
        self.setlogica(logica)
        self.setName(name)

    # ===almacenes===
    def yahtzee(self):      # yahtzee
       """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave yhatzee """ 
       self.__diccionario["yahtzee"]=self.__logica_juego.GetYatzy()
    
    # almacenes de numeros:
    def uno(self):          # uno
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave uno """
        self.__diccionario["uno"]=self.__logica_juego.GetUno()

    def dos(self):          # dos
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave dos """
        self.__diccionario["dos"]= self.__logica_juego.GetDos()
       
    def tres(self):         # tres
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave tres """
        self.__diccionario["tres"]=self.__logica_juego.GetTres()
        
    def cuatro(self):       # cuatro
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave cuatro """
        self.__diccionario["cuatro"]=self.__logica_juego.GetCuatro()
        
    def cinco(self):        # cinco
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave cinco """
        self.__diccionario["cinco"]=self.__logica_juego.GetCinco()
       
    def seis(self):         # seis
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave seis """
        self.__diccionario["seis"]=self.__logica_juego.GetSeis()
        
    
    # almacenes de combinaciones:
    def Full(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave full """
        self.__diccionario["full"]=self.__logica_juego.GetFull()
        
    
    def EscaleraMay(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave EscaleraMay  """
        self.__diccionario["EscaleraMay"]=self.__logica_juego.GetEscaleraMay()
        
    def EscaleraMen(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave EscaleraMen  """
        self.__diccionario["EscaleraMen"]=self.__logica_juego.GetEscaleraMenor()
        
    def Poker(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave poker  """
        self.__diccionario["poker"]=self.__logica_juego.GetPoker()
    
    def Trio(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave trio  """
        self.__diccionario["trio"]=self.__logica_juego.GetTrio()
   
    def Dos_Pares(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave 2par  """
        self.__diccionario["2par"]=self.__logica_juego.Get_Dos_Pares()
   
    def libre(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave libre """
        self.__diccionario["libre"]=self.__logica_juego.GetLibre()
    
    def Par(self):
        """Su objetivo es guardar la puntuacion obtenida en los dados en el diccionario
          en este caso guardara la puntuacion de la llave 1par  """
        self.__diccionario["1par"]=self.__logica_juego.GetPar()
    
    def setlogica(self,objeto):
        """Su objetivo es modificar el atributo logica
           Args:
               objeto(object): [tiene que ser un objeto de la clase logica]
            Raises:
                ValueError:[Excepción que se levanta si el argumento objeto no pertenece a logica]"""
        if type(objeto)!=Logic:
            raise ValueError
        self.__logica_juego=objeto
    
    def setName(self,name):
        """Su objetivo es modificar el atributo name
           Args:
               name(object): [tiene que ser de tipo String]
            Raises:
                ValueError:[Excepción que se levanta si el argumento name no es un String ]"""
        if type(name)!=str:
            raise ValueError
        self.__name=name

    def getName(self):
        """Su objetivo es retornar el atributo name
        Returns:
            String"""
        return self.__name

    def EndGame(self):
        """La funcion de este metodo es verificar si el juego acabo, si acabo retornara: True sino retornara: False
        Returns:
            boolean """
        for i in self.__diccionario.values():
            if i==None:
                return False
        return True
    
    def puntTemp(self):
        """La funcion de este metodo es calcular la puntuacion total temporal en la partida
        Returns:
            int"""
        s=0
        for i in self.__diccionario.values():
            if i!=None:
                s+=i
        return s
    
    def getdicionario(self):
        """Su objetivo es retornar el atributo self.__diccionario
        Returns:
            dict"""
        return self.__diccionario