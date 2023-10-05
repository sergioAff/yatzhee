import random
class Dado:
    """clase dado su labor es modelar el funcionamiento de un dado
    Attributes:
        valor(int): [representa el valor del dado este comienza en 0 por defecto]
        estado(boolean) [representa el estado del dado en el que se encuentra]"""
    def __init__(self,estado=True):
        self.__valor=0
        self.__estado=estado
    
    def rodar_dados(self):
        """su funcion es modificar el valor del dado """
        if self.__estado==True:
            self.__valor=random.randint(1,6)
    
    def EstadoTrue(self):
        """su funcion es modificar el estado del dado a True"""
        self.setestado(True)  
    
    def interruptor(self):
        """modifica el estado del dado si su estado = True lo cambiara a estado=False y si estado= False lo volvera True
           haciendo como un interruptor"""
        if self.getestado():
            self.setestado(False)
        else:
            self.setestado(True)
    
    def getvalor(self):
        """retorna el valor del dado
        Returns:
            int"""
        return self.__valor
    
    def setestado(self,estado):
        """modifica el estado 
        Args:
            estado(boolean): [ese argumento solo puede ser de tipo boolean]
        Raises:
            ValueError:[Exepcion que se levanta si el argumento estado no es de tipo boolean]"""
        
        if type(estado)!=bool:
            raise ValueError

        self.__estado=estado
    
    def getestado(self):
        """devuelve el estado del dado
        Returns:
            boolean"""
        return self.__estado
    