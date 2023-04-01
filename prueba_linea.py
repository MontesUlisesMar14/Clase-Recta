from clasepuntochida import Punto
from claselineachida import Linea


if __name__ == "__main__":
    recta = Linea(3,4,2,8,9,10,11,12)

    while(True):
        print(" \n[0] Salir"+
           "\n[1] Ecuacion general " +
           "\n[2] Pendiente "+
           "\n[3] Ordenada"+
            "\n[4] Comparar dos rectas"+
            "\n[5] Ver si un punto pertenece a la recta")
        print('Para cada opción, se deben otorgar dos puntos con coordenadas X y Y, el programa calcula una recta que pasa por ambos puntos')
        opcion = int(input("Escribe una opción:"))
        
        if opcion == 0:
            print("Fin del programa")
            break
        elif opcion == 1:
            print("Ecuacion general")
            x1 = int(input("Dame primer coordenada: "))
            y1 = int(input("Dame segunda coordenada: "))
            x2 = int(input("Dame primer coordenada: "))
            y2 = int(input("Dame segunda coordenada: "))
            recta=Linea(x1,y1,x2,y2, None, None, None, None)

            re_ecuacion = recta.ecuacion_recta()

            print("Ecuacion general: ",re_ecuacion)
            
        elif opcion == 2:
            print("Pendiente")
            x1 = int(input("Dame primer coordenada: "))
            y1 = int(input("Dame segunda coordenada: "))
            x2 = int(input("Dame primer coordenada: "))
            y2 = int(input("Dame segunda coordenada: "))
            recta=Linea(x1,y1,x2,y2, None, None, None, None)

            re_pendiente = recta.pendiente()

            print("Pendiente: ",re_pendiente) 

        elif opcion == 3:
            print("Ordenada al origen")
            x1 = int(input("Dame primer coordenada: "))
            y1 = int(input("Dame segunda coordenada: "))
            x2 = int(input("Dame primer coordenada: "))
            y2 = int(input("Dame segunda coordenada: "))
            recta=Linea(x1,y1,x2,y2, None, None, None, None)

            re_ordenada = recta.ordenada()

            print("Resultado: ", re_ordenada)

        elif opcion == 4:
            print('Comparar dos rectas')
            print('Recta 1:')
            print('Primer punto:')
            x1 = float(input('Dame primer coordenada: '))
            y1 = float(input('Dame segunda coordenada: '))
            print('Segundo punto:')
            x2 = float(input('Dame primer coordenada: '))
            y2 = float(input('Dame segunda coordenada: '))
            print('Recta 2:')
            print('Primer punto:')
            x3 = float(input('Dame primer coordenada: '))
            y3 = float(input('Dame segunda coordenada: '))
            print('Segundo punto:')
            x4= float(input('Dame primer coordenada: '))
            y4 = float(input('Dame segunda coordenada: '))
            recta1 = Linea(x1, y1, x2, y2, x3, y3, x4, y4)
            if recta1.__eq__() == True:
                print('las rectas son iguales')
            if recta1.es_paralela() == True:
                print('Las rectas son parelelas, por lo tanto no tienen punto de intersección')
            else:
                print('No son paralelas')
            if recta1.es_perpendicular() == True:
                print('Las rectas son perpendiculares')
            else:
                print('Las rectas no son perpendiculares')
            print(f'El punto de intersección es {recta1.punto_de_interseccion()}')

        elif opcion == 5:
            print('Ver si punto pertenece a una recta')
            print('Recta:')
            print('Primer punto:')
            x1 = float(input('Dame primer coordenada: '))
            y1 = float(input('Dame segunda coordenada: '))
            print('\n'+
                  'Segundo punto:')
            x2 = float(input('Dame primer coordenada: '))
            y2 = float(input('Dame segunda coordenada:'))
            print('\n'+
                  'Punto que deseamos averiguar si se encuentra en la recta:')
            c1 = float(input('Dame primer coordenada: '))
            c2 = float(input('Dame segunda coordenada: '))
            recta1 = Linea(x1, y1, x2, y2, c1, c2, None, None)
            #ya que c1 y c2 fueron definidos como self.x3 y self.y3 respectivamente
            if recta1.contiene_a_punto() == True:
                print(f'El punto ({c1},{c2}) pertenece a la recta')
            else:
                print(f'El punto ({c1},{c2}) no pertenece a la recta')
            
        else:
            print("Escribe una opción válida")
            
