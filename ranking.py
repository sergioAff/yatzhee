from pickle import *
from AlmacenDePuntos import *
class Ranking():
    """clase Ranking tiene la labor de crear ficheros con pickle para guardar las puntuaciones de forma permanente
    Attributes:
        diccionario(dict): [contiene la informacion ya cargada del fichero]"""
    def __init__(self):
        self.__diccionario=self.cargar()
        
    
    def crearFichero(self): 
        """esta funcion crea un fichero se puede usar para cambiar el fichero existente por uno modificado"""
        self.__fichero_binario= open("ranking","wb")
        dump(self.__diccionario,self.__fichero_binario)
        self.__fichero_binario.close()    
    
    def cargar(self):
        """esta el objetivo de esta funcion es cargar la informacion de un fichero y guardarla en un diccionario
        Returns:
            dict"""
        try:
            self.__fichero_binario=open("ranking","rb")
            l=load(self.__fichero_binario)
            self.__fichero_binario.close()
            return l
        except FileNotFoundError:
            l= {}
            return l
    
    

    def comprobador_coin(self,name,objeto):    
        """comprueba que el elemento nuevo a agregar no exista en la lista y si de casualidad existe 
            comprobara cual de los dos elementos tiene mayor puntuacion para quedarse con ese elemento 
            Args:
                name(str): [argumento que representa el nombre del jugador]
                objeto(object) [este argumento tiene que ser un objeto de la clase Almacen de puntos]
            Raises:
                ValueError: [lanza ValueError si name no es te tipo string o si objeto no pertenece a la clase almacen de puntos]
            Returns:
                Boolean """
        if type(name)!=str:
            raise ValueError
        if type(objeto)!= AlmacenDePuntos:
            raise ValueError
        for i in self.__diccionario.keys():    
            if name==i and self.__diccionario[i]>objeto.puntTemp():
                return False
        return True
    
    
    
    def agregarpuntos(self,name,objeto):
        """su funcion es agregar nuevas puntuaciones en el diccionario 
        Args:
            name(str): [argumento que representa el nombre del jugador]
            objeto(object) [este argumento tiene que ser un objeto de la clase Almacen de puntos]"""
        
        if self.comprobador_coin(name,objeto):
            self.__diccionario[name]=objeto.puntTemp()
    
    
    def Ordenar(self): 
        """esta funcion mostrar una lista es lo que se le mostrara a los usuarios la lista de tuplas ordenada nombre puntuacion
        Returns:
            list"""
        l=list(self.__diccionario.items())
        l.sort(key=lambda x: x[1],reverse=True)
        return l
    def eliminar_elemento(self,key):
        """este metodo elimina un elemento del diccionario
        Args:
            key(string): [es la llave del diccionario a eliminar]
        Raises:
            ValueError: [este error salta si la llave no es de tipo str]"""
        if type(key)!=str:
            raise ValueError
        self.__diccionario.pop(key)
    def getDicionario(self):
        return self.__diccionario
