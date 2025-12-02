import os

os.system("cls")




class Profesores:

    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre= nombre
        self.__experiencia = experiencia
        self.__num_profesor = num_profesor

    @property
    def nombre(self):
        return self.__nombre     
    

    @nombre.setter
    def nombre(self, nombre):            
        self.__nombre=nombre

    
    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter                      
    def experiencia(self, experiencia):
        self.__experiencia=experiencia
    
    @property
    def num_profesor(self):
        return self.__num_profesor
    
    @num_profesor.setter
    def num_profesor(self, num_profesor):
        self.__num_profesor=num_profesor
    
    def impartir():
        return "El profesor esta impartiendo la clase"
    
    def evaluar():
        return "El profesor esta evaluando"


profesor1=Profesores("Ana Torres Guzman", 40, 123)
profesor2=Profesores("Daniel Contreras", 35, 124)



class Alumnos:

    def __init__(self, nombre, edad, matricula):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula

        @property
        def nombre(self):
            return self.__nombre
        
        @nombre.setter
        def nombre(self, nombre):
            self.__nombre=nombre
        
        @property
        def edad(self):
            return self.__edad
        
        @edad.setter
        def edad(self, edad):
            self.__edad = edad

        @property
        def matricula(self):
            return self.__matricula
        
        @matricula.setter
        def matricula(self, matricula):
            self.__matricula = matricula

        def inscribirse():
            return "El alumno se esta inscribiendo" 
        
        def estudiar():
            return "El alumno est estudiando"


alumno1=Alumnos("Juan Hernandez", 20, 3141240585)
alumno2=Alumnos("Abdiel Avitia", 20, 3141240156)




class Cursos:
    
    def __init__(self, nombre, codigo, num_profesor):

        self.__nombre = nombre
        self.__codigo = codigo
        self.__num_profesor = num_profesor


        @property
        def nombre(self):
            return self.__nombre
        
        @nombre.setter
        def nombre(self, nombre):
            self.__nombre = nombre

        
        @property
        def codigo(self):
            return self.__codigo
        
        @codigo.setter
        def codigo(self, codigo):
            self.__codigo = codigo

        
        @property
        def num_profesor(self):
            return self.__num_profesor
        
        @num_profesor.setter
        def num_profesor(self, codigo):
            self.num_profesor=num_profesor

        def asignar():
            return "La clase esta siendo asignada"
        
curso1=Cursos("POO", 254, 123)
curso2=Cursos("Calculo", 545, 124)




        
