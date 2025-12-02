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
                    # Entrar al submenú de estudiante y mantenerlo en ciclo
                    self.gestionar_estudiante()
                case "2": 
                    print("La ejecución del programa a terminado :)")
                    opcion = False
                    
                case _:
                    opcion = True 
                    input("\nOpcion invalida ... vuelva a intertarlo ... ") 
    
    def gestionar_estudiante(self):
        # Ciclo del submenú de estudiante: muestra opciones y ejecuta acciones
        while True:
            self.borrarPantalla()
            opcion = self.menu_acciones()
            match opcion:
                case "1":
                    nombre, nota = self.datos_estudiante("INSERTAR")
                    # intenta llamar a estudiante.insertar si existe
                    if hasattr(estudiante, "insertar"):
                        try:
                            respuesta = estudiante.insertar(nombre, nota)
                        except Exception as e:
                            print(f"Error al insertar: {e}")
                            respuesta = False
                        self.respuesta_sql(respuesta)
                    else:
                        print("\nFunción 'insertar' no encontrada en módulo 'estudiante'.")
                        self.esperarTecla()

                case "2":
                    nombre, _ = self.datos_estudiante("CONSULTAR")
                    if hasattr(estudiante, "consultar"):
                        try:
                            resultado = estudiante.consultar(nombre)
                        except Exception as e:
                            print(f"Error al consultar: {e}")
                    else:
                        print("\n Ocurrio un error, intente mas tarde.")
                    self.esperarTecla()

                case "3":
                    nombre, nota = self.datos_estudiante("ACTUALIZAR")
                    if hasattr(estudiante, "actualizar"):
                        try:
                            respuesta = estudiante.actualizar(nombre, nota)
                        except Exception as e:
                            print(f"Error al actualizar: {e}")
                            respuesta = False
                        self.respuesta_sql(respuesta)
                    else:
                        print("\nFunción 'actualizar' no encontrada en módulo 'estudiante'.")
                        self.esperarTecla()

                case "4":
                    nombre, _ = self.datos_estudiante("ELIMINAR")
                    if hasattr(estudiante, "eliminar"):
                        try:
                            respuesta = estudiante.eliminar(nombre)
                        except Exception as e:
                            print(f"Error al eliminar: {e}")
                            respuesta = False
                        self.respuesta_sql(respuesta)
                    else:
                        print("\nFunción 'eliminar' no encontrada en módulo 'estudiante'.")
                        self.esperarTecla()

                case "5":
                    # Regresar al menú principal
                    break

                case _:
                    print("\n \t \t Opción no válida. Intenta de nuevo.")
                    self.esperarTecla()

    def main(self):
        self.menu_estudiante()
        
if __name__ == "__main__":
  app=App()


