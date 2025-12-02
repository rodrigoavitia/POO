"""
Encapsular es un pilar de las POO que permite indicar cual es la manera de como poder utilizar 
los atributos y metodos de una clase a la
hora de usar en objetos o en herencia. 
"""

import os 

os.system("cls")

class Clase:
    atributopublico  = ("Soy un atributo publico")
    _atributo_protegido = ("Soy un atributo protegido")
    __atributo_privado = ("Soy un atributo privado")




    def __init__(self, color, tamanio):
        self.__color= color
        self.__tamanio = tamanio

    @property
    def color(self):
        return self.__color     
    

    @color.setter
    def color(self, color):             
        self.__color=color

    
    @property
    def tamanio(self, tamanio):
        return self.__tamanio
    
    @tamanio.setter                      
    def tamanio(self, tamanio):
        self.__tamanio=tamanio

    def getAtributoPrivado(self):
        return self.__atributo_privado  
    
    @property
    def atributo_publico(self):
        return self.atributo_publico
    
    @atributo_publico.setter
    def atributo_publico(self, atributo_publico):
        self.atributo_publico=atributo_publico

    @property
    def atributo_protegido(self):
        return self._atributo_protegido
    
    @atributo_protegido.setter
    def atributo_protegido(self, atributo_protegido):
        self._atributo_protegido=atributo_protegido

    @property
    def atributo_privado(self):
        return self.__atributo_privado
    
    @atributo_privado.setter
    def atributo_privado(self, atributo_privado):
        self.__atributo_privado=atributo_privado


#Utilizar la clase
objeto=Clase("Rojo", "Grande")

"""
print(objeto.atributo_publico)
print(objeto._atributo_protegido) #Hasta atributo protegido se puede usar sin problemas #Pero no es una buena practica

"""

print(objeto.atributo_privado)  #Esto solo lo puedo usar dentro de la clase y/o creando metodos

print(objeto.atributopublico)

print(objeto.atributo_protegido)










