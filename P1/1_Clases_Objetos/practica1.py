"""
Praactica 1: implementar paradigma estructurado VS 00 

Crear un programa que obtenga el area de un rectangulo

"""
#  METODO ESTRUCTURADO

import os

os.system("cls")

print(".::calcular el area de un rectangulo::.")
area=6*5
def area_rectangulo(base, altura):
    area = (base * altura)
    return area

base= 6
altura = 5
print(f"El area del rectangulo es:{area_rectangulo(base, altura)}")



# METODO OO

class AreaRectangulo:
    def area_rectangulo(self,base, altura):
        area = (base * altura)
        return area

rectangulo1 = AreaRectangulo() #Instanciar un  objeto de la clase "AreaRectangulo"
print(f"El area del rectangulo es:{rectangulo1.area_rectangulo(6,5)}")




class AreaRectangulo:
    def __init__(self,base,altura):
        base=base

    def areaRectangulo (self,base,altura):
        area = base * altura
        return area
    
    rectangulo1=AreaRectangulo(5,6)
    print(f"El area del rectangulo es {rectangulo1.area_rectangulo()}")

