"""
Realizar un programa que conste de una clase llamda Estudiante, que tenga como atributos
el nombre y la nota del alumno. Definir los metodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""
from conexionBD import conexion
import os

class Estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        try:
            # acepta cadenas numéricas también
            self._nota = float(nota)
        except Exception:
            self._nota = 0.0

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        try:
            self._nota = float(nota)
        except Exception:
            pass

    def mostrar_cali(self):
        if self._nota >= 7:
            print(f"\nEl estudiante {self._nombre} ha aprobado con una calificacion de {self._nota}")
        else:
            print(f"\nEl estudiante {self._nombre} ha reprobado con una calificacion de {self._nota}")

# ------------------------
# Funciones a nivel de módulo usadas por el menú
# ------------------------

def insertar(nombre, nota):
    """
    Inserta un estudiante. Devuelve True/False.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO estudiante (nombre, nota) VALUES (%s, %s)",
            (nombre, nota)
        )
        conexion.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error al insertar estudiante: {e}")
        return False

def consultar(nombre=None):
    """
    Si nombre es None devuelve todos los registros.
    Si se pasa nombre devuelve los registros que hagan LIKE sobre el nombre.
    Muestra los resultados de forma tabular, imprime mensaje de éxito o no encontrados
    y espera que el usuario presione Enter antes de retornar la lista de resultados.
    Retorna lista de tuplas.
    """
    try:
        cursor = conexion.cursor()
        if nombre and nombre.strip() != "":
            like = f"%{nombre}%"
            cursor.execute("SELECT * FROM estudiante WHERE nombre LIKE %s", (like,))
            resultados = cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM estudiante")
            resultados = cursor.fetchall()
        cursor.close()

        # Mostrar resultados de forma más natural/tabular
        if resultados and len(resultados) > 0:
            print("\nResultados de la consulta:\n")
            print(f"{'ID':<6}{'Nombre':<40}{'Nota':<10}")
            print("-" * 58)
            for fila in resultados:
                
                id_val = fila[0]
                nombre_val = fila[1] if len(fila) > 1 else ""
                nota_val = fila[2] if len(fila) > 2 else ""
                print(f"{str(id_val):<6}{str(nombre_val):<40}{str(nota_val):<10}")
            print("\nConsulta realizada con éxito.")
            input("\nPresiona Enter para continuar ... ")
        else:
            print("\nNo se encontraron registros para la consulta.")
            input("\nPresiona Enter para continuar ... ")

        #return resultados
    except Exception as e:
        print(f"Error al consultar estudiantes: {e}")

def actualizar(nombre, nota):
    """
    Actualiza la nota del/los estudiante(s) que coincidan exactamente con 'nombre'.
    Retorna True/False.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE estudiante SET nota=%s WHERE nombre=%s",
            (nota, nombre)
        )
        conexion.commit()
        afectadas = cursor.rowcount
        cursor.close()
        print("Se actualizaron los datos correctamente.")
        input("\nPresiona Enter para continuar ... ") 
        return afectadas > 0  
    except Exception as e:
        print(f"Error al actualizar estudiante: {e}")
        return False

def eliminar(nombre):
    """
    Elimina estudiante(s) por nombre exacto. Retorna True/False.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM estudiante WHERE nombre=%s",
            (nombre,)
        )
        conexion.commit()
        afectadas = cursor.rowcount
        cursor.close()
        print(f"\nSe eliminaron {afectadas} registro(s).")
        input("\nPresiona Enter para continuar ... ")
        return afectadas > 0
    except Exception as e:
        print(f"Error al eliminar estudiante: {e}")
        return False


