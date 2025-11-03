"""
Realizar un programa que conste de una clase llamda Estudiante, que tenga como atributos
el nombre y la nota del alumno. Definir los metodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""
from conexionBD import *
import os 
os.system("cls")


class Estudiante():
    def __init__(self, nombre, nota):

        self._nombre = nombre
        self._nota = nota
    @property
    def nombre(self):
        return self.nombre 
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
    @property
    def nota(self):
        return self.nota
    @nota.setter
    def nota(self, nota):
        self._nota = nota
  
    def mostrar_cali(self, nombre, nota):
        if self._nota >= 7:
            print(f"\nEl estudiante {self._nombre} ha aprobado con una calificacion de {self._nota}")
        else:
            print(f"\nEl estudiante {self._nombre} ha reprobado con una calificacion de {self._nota}")
           
    def insertar(nombre, nota):
        try:
            cursor.execute(
                "insert into estudiante values(null,%s,%s)",
                (nombre, nota)
            )
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from estudiante")
            return cursor.fetchall()
        except:    
            return []

    @staticmethod
    def actualizar(nombre, nota,id):
        try:
            cursor.execute(
                "update notas set nombre=%s,nota=%s where id=%s",
                (nombre,nota,id)
            )
            conexion.commit()
            return True
        except: 
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from estudiante where id=%s",
                (id,)
            ) 
            conexion.commit() 
            return True  
        except:    
            return False
            

