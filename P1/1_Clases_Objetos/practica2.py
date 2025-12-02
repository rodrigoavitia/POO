
# MODELAR Y DIAGRAMAR EN LA POO (PROGRAMACIÓN ORIENTADA A OBJETOS)
import os 

os.system("cls")

#CLASE DE COCHES
class Coches:
    def __init__(self, color, marca, velocidad): #METODO CONSTRUCTOR QUE INICIALIZA LOS VALORES CUANDO SE INSTANCIA UN OBJETO DE LA CLASE 
        self.__color = color
        self.__marca = marca              #ATRIBUTOS DEL OBJETO (COCHE)
        self.__velocidad = velocidad


# AQUI EMPIEZAN LOS METODOS QUE SON COMO LAS ACCIONES QUE REALIZAN

    def acelerar(self, incremento):
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad
    
    def frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    
#INSTANCIAR O CREAR OBJETOS DE LA CLASE COCHES 

coche1 = Coches("Blanco", "Toyota", 220)
coche2 = Coches("Amarillo", "Nissan", 180)

"""
print (f"Los valores del objeto 1 son: {coche1.__marca}, {coche1.__color}, {coche1.__velocidad} km/hr")
velocidad = coche1.acelerar(50)
print(f"El coche 1 aceleró de: {coche1.__velocidad} a {velocidad} ")


print (f"Los valores del objeto 2 son: {coche2.__marca}, {coche2.__color}, {coche2.__velocidad} km/hr")
velocidad=coche2.frenar(100)
print(f"El coche 2 freno de: {coche1.__velocidad} a {velocidad}")

"""

print(coche1.acelerar(50))
print (coche2.frenar(100))
























