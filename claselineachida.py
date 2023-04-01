from clasepuntochida import Punto

class Linea:

    def __init__(self, x1,y1,x2,y2,x3,y3,x4,y4):
        """
        Inicializa una instancia de la clase Linea con las coordenadas de dos puntos
        para los primeros metodos y de cuatro puntos para los restantes.
        
        :parametro x1: Coordenada x del primer punto.
        :parametro y1: Coordenada y del primer punto.
        :parametro x2: Coordenada x del segundo punto.
        :parametro y2: Coordenada y del segundo punto.
        ...
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    
    def ecuacion_recta(self) -> str:
        """
        Calcula la ecuación de la recta que pasa por los dos puntos de la línea.

        Returns:
        - (str): la ecuación de la recta en forma de cadena de texto
        """
        a = self.y2 - self.y1
        b = self.x1 - self.x2
        c = self.y1 * self.x2 - self.y2 * self.x1
        #si algun coeficiente es 0, lo elimina. Si es 1 o -1, lo quita y deja su signo.
        if a == 0:
            return f"{b}y + {c} = 0"
        elif b == 0:
            return f"{a}x + {c} = 0"
        elif c == 0:
            return f"{a}x + {b}y = 0"
        elif a == 1:
            return f"x + {b}y + {c} = 0"
        elif b == 1:
            return f"{a}x + y + {c} = 0"
        elif a == -1:
            return f"-x + {b}y + {c} = 0"
        elif b == -1:
            return f"{a}x + -y + {c} = 0"
        else:
            return f"{a}x + {b}y + {c} = 0"

    def pendiente(self)->str:
        """
        Calcula la pendiente de la recta.

        Returns:
        - (str): la pendiente de la recta en forma de cadena de texto.
        """
        if self.x1 == self.x2 and self.y1 == self.y2:
            return None  # Si los puntos son iguales, la pendiente no está definida
        else:
            numerador = self.y2 - self.y1
            denominador = self.x2 - self.x1
            pendiente = numerador / denominador
            return f"{pendiente:.0f}" if pendiente.is_integer() else f"{numerador}/{denominador}"
        
    def ordenada(self):
        """
        Calcula la ordenada al origen de la recta que pasa por los dos puntos
        representados por la instancia de la clase Linea.
        
        :return: La ordenada al origen de la recta en forma de string.
        :rtype: str
        """
        numerador = self.y1 * (self.x2 - self.x1) - self.x1 * (self.y2 - self.y1)
        denominador = self.x2 - self.x1
        if denominador == 0:
            return "indefinido"
        b = numerador / denominador
        if b == 0:
            return "0"
        else:
            #convierte b a un numero racional si es que NO es entero
            return f"{b:.0f}" if b.is_integer() else f"{numerador}/{denominador}"

    def contiene_a_punto(self)->object:
        '''
        Se calcula la ecuacion general, se agregan nuevos parametros los cuales son
        las coordenadas del nuevo punto
        :return: True si la igualdad resulta verdadera al ser evaluada en el punto (c1,c2)
        De otro modo retorna False.
        '''
        # obtener la ecuación general de la recta y = mx + b
        c1 = self.x3
        c2 = self.y3
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        b = self.y1 - m * self.x1
        # comprobar si el punto (c1, c2) satisface la ecuación general de la recta
        if c2 == m * c1 + b:
            return True
        else:
            return False

    def es_paralela(self)->object:
        '''
        El metodo calcula las pendientes de ambas rectas
        :return: True Si las pendientes son las mismas. False en caso contrario.
        '''
        m1 = (self.y2 - self.y1) / (self.x2 - self.x1)  # pendiente de la recta 1
        m2 = (self.y4 - self.y3) / (self.x4 - self.x3)  # pendiente de la recta 2
        if m1 == m2: # dos rectas son paralelas si sus pendientes son iguales
            return True
        else:
            return False

    def es_perpendicular(self)->object:
        '''
        El metodo es_perpendicular calcula las pendientes de los 4 puntos correspondientes
        :return: True si el producto de ambas pendientes es -1. False en caso contrario
        
        '''
        m1 = (self.y2 - self.y1) / (self.x2 - self.x1)  # pendiente de la recta 1
        m2 = (self.y4 - self.y3) / (self.x4 - self.x3)  # pendiente de la recta 2
        c = m1 * m2
        if c == -1: # dos rectas son perpendiculares si el producto de sus pendientes es -1
            return True
        else:
            return False 

    def punto_de_interseccion(self)->object:
        '''
        El metodo calcula las pendientes y la interseccion
        :return: Si las pendientes son iguales nos regresa un None puesto que nunca hay interseccion.
        Retorna un punto en la forma (x,y) si encuentra interseccion
        '''
        m1 = (self.y2 - self.y1) / (self.x2 - self.x1)  # pendiente de la recta 1
        m2 = (self.y4 - self.y3) / (self.x4 - self.x3)  # pendiente de la recta 2
        b1 = self.y1 - m1 * self.x1  # intersección con el eje y de la recta 1
        b2 = self.y3 - m2 * self.x3  # intersección con el eje y de la recta 2

        if m1 == m2:  # si las rectas son paralelas no tienen punto de intersección
            return None
        else:
            x = round((b2 - b1) / (m1 - m2),7)  # fórmula para calcular la coordenada x del punto de intersección
            y = round(m1 * x + b1,7)  # fórmula para calcular la coordenada y del punto de intersección
            return f"({x}, {y})"
        
        
    def __eq__(self): #Metodo __eq__ para saber si son iguales
        
        '''
        Se calculan las pendientes, ademas se toma en cuenta la ordenada al origen
        :return: True si las ordenadas al origen coinciden. False en caso contrario.
        '''
        m1 = (self.y2 - self.y1) / (self.x2 - self.x1)
        m2 = (self.y4 - self.y3) / (self.x4 - self.x3)
        o1 = round(self.y1-(m1*self.x1),7) #Definimos a la ordenada de la primera recta
        o2 = round(self.y4-(m2*self.x4),7) #Definimos a la ordenada de la segunda recta
        if o1 == o2: #Tomando en cuenta las pendientes y con ello, si ambas ordenadas son iguales, las rectas son las mismas
            return True
        else:
            return False


    def __str__(self):
        """
        Retorna una representación en string de la instancia de la clase Linea.
        
        :return: Una representación en string de la instancia de la clase Linea.
        :rtype: str
        """
        ecuacion = self.ecuacion_recta()
        pendiente = self.pendiente()
        ordenada = self.ordenada()
        return f"Los puntos de la recta: ({self.x1},{self.y1}), ({self.x2},{self.y2})\nLa ecuacion de la recta: {ecuacion}\nLa pendiente de la recta: pendiente = {pendiente}\nLa ordenada al origen: ordenada = {ordenada}"

if __name__ == "__main__":
    recta1 = Linea(5,8,3,2, None, None, None, None)
    print(recta1)
    print("\n")
    recta2 = Linea(3,4,2,8, None, None, None, None)
    print(recta2)
    print("\n")
    recta3 = Linea(-5,4,0,0, None, None, None, None)
    print(recta3)
