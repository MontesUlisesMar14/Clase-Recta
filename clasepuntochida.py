"""
Clase para representar punto en el plano cartesiano
Autor: Jessica
"""
import math
class Punto:

    def __init__(self, x=0, y=0):
        """
            Constructor de la clase que inicializa
            los atributos x e y de un objeto
            que representa una coordenada
            en un plano cartesiano.
            Params:
                  x(float): Coordenada en el eje X. Por defecto es 0
                  y(float): Coordenada en el eje Y. Por defecto es 0
        """
        self.__x = x
        self.__y = y


    def set_x(self, x:float):
        """
            Método modificador que permite cambiar el
            valor de la coordenada x
            Params:
                x(float) :  El nuevo valor que se le va asignar a x
        """
        self.__x = x
        
    def set_y(self, y_float):
        """
            Método modificador que permite cambiar el
            valor de la coordenada y
            Params:
                y(float) :  El nuevo valor que se le va asignar a y
        """
        self.__y = y
    
    def get_x(self)->float:
        """
            Método acceso que permite obtener el
            valor de la coordenada x
            Returns:
                float:  Regresa el valor de x
        """
        return self.__x

    def get_y(self) -> float:
        """
            Método acceso que permite obtener el
            valor de la coordenada y
            Returns:
                float:  Regresa el valor de y
        """
        return self.__y


    def desplazamiento(self, aumento_x:float , aumento_y:float)->object:
        return Punto(self.get_x() + aumento_x , self.get_y() + aumento_y)
    
    def suma(self,otro_punto:object)-> object:
        """
            Método que permite sumar dos puntos.
            Params:
                otro_punto(Punto) :  Recibe el punto que se va a sumar
                con el punto que manda a llamar al método
            Returns:
                Punto:  Regresa un Punto, que corresponde a la suma de
                dos puntos: (Se suma el punto que manda a llamar al método con
                el punto que se recibe como parámetro)
        """
        coord_x = self.__x + otro_punto.get_x()
        coord_y = self.__y + otro_punto.get_y()
        punto_suma = Punto(coord_x, coord_y)
        return punto_suma
        ## return Punto(self.__x + otro_punto.get_x(), self.__y + otro_punto.get_y())

    def resta(self, otro:object)-> object:
        coord_x_nuevo =  self.get_x() - otro.get_x()
        coord_y_nuevo =  self.get_y() - otro.get_y()

        nuevo = Punto(coord_x_nuevo, coord_y_nuevo)

        return nuevo

    def distancia(self,otro:object)-> float:
        resta1 = otro.get_x() - self.get_x()
        resta2 = otro.get_y() - self.get_y()

        potencia1 =  math.pow(resta1,2)
        potencia2 = math.pow(resta2,2)

        resultado = math.sqrt(potencia1 + potencia2)
        return resultado

    def __str__(self)->str:
        return "(" + str(self.get_x()) + " , " + str(self.get_y()) + ")"

    def __eq__(self, otro:object)->bool:

        return self.get_x() == otro.get_x() and self.get_y() == otro.get_y()
    
