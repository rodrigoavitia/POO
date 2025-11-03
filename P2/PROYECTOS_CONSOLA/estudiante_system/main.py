import conexionBD
from estudiante import estudiante
import os 

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\n\t Preciona Enter para Continuar")
    
    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingrese los siguientes datos del estudiante: '{tipo}' ...")
        nombre=input("Nombre completo: ").upper()
        nota=input("Nota o calificacion del alumno: ").upper()
        return nombre, nota

    def menu_acciones(self):
        print(f"\n\t\t.::  Menu de Estudiante ::.\n\t1.- Insertar calificación \n\t2.- Consultar calificación\n\t3.- Actualizar calificación\n\t4.- Eliminar calificación\n\t5.- Regresar ")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion
    
    def respuesta_sql(self, respuesta):
        if respuesta:
            print("\n\t... ¡ Accion realizada con Éxito !...")
        else:
            print("\n\t... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...") 

    def menu_estudiante(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Estudiante\n\t2.-Salir\n\tElige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_acciones() 
                case "2": 
                    print("La ejecución del programa a terminado :)")
                    opcion = False
                    
                case _:
                    opcion = True 
                    input("\nOpcion invalida ... vuelva a intertarlo ... ") 

    def main(self):
        self.menu_estudiante()
        
if __name__ == "__main__":
  app=App()


