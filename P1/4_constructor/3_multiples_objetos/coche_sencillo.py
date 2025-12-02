import os 

os.system("cls")

class Coches:
    __marca=""
    __color=""
    __modelo="" 
    __velocidad=0
    __caballaje=0
    __plazas=0





"""
Crear los metodos getters y setters, estos metodos son importantes y necesarios en todas las clasespara que el programador
interactue con los valores de los atributos a traves de estos metodos, dogamos que es la manera mas adecuada y recomendada 
para solicitar un valor get y/o para ingrear o cambiar un valor set a un atributo en particular de la clase a traves de un objeto.

En teoria se deberia de crear un metodo getters y setters por cada atributo que contega la clase

Los metodos get siempre van a regresar valor es decir que el valor de la propiedad a traves del return.

Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion.
"""
#---------------------------------------------------------------------------------------------------------

def getMarca(self):
    return self.__marca

def setMarca(self,marca):
    self.__marca=marca

#---------------------------------------------------------------------------------------------------------


def getColor(self):
    return self.__color

def setColor(self,color):
    self.__color=color

#---------------------------------------------------------------------------------------------------------


def getModelo(self):
    return self.__modelo

def setModelo(self,modelo):
    self.__modelo=modelo

#---------------------------------------------------------------------------------------------------------

def getVelocidad(self):
    return self.__velocidad

def setVelocidad(self,velocidad):
    self.__velocidad=velocidad

#----------------------------------------------------------------------------------------------------------
def getCaballaje(self):
    return self.__caballaje

def setCaballaje(self,caballaje):
    self.__marca=caballaje

#---------------------------------------------------------------------------------------------------------


coche1=Coches()

coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)


print(f"El coche 1 es un {coche1.getMarca()} de color {coche1.getColor()} modelo {coche1.getModelo()} con una velocidad maxima de {coche1.getVelocidad()} y un caballaje de {coche1.getCaballaje()}")

coche2=Coches()

coche2.setMarca("Audi")
coche2.setColor("Rojo")
coche2.setModelo("2021")
coche2.setVelocidad(240)
coche2.setCaballaje(180)

print(f"El coche 2 es un {coche2.getMarca()} de color {coche2.getColor()} modelo {coche2.getModelo()} con una velocidad maxima de {coche2.getVelocidad()} y un caballaje de {coche2.getCaballaje()}")




