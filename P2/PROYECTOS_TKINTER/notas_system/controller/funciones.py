class Funcion():
   
  def borrarPantalla(self):
    import os  
    os.system("cls")

  def esperarTecla(self):
    input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

  def menu_usurios(self):
    print("\n \t.:: Sistema de Gestión de Notas ::.. \n\t\t1.- Registro  \n\t\t2.- Login \n\t\t3.- Salir ")
    opcion=input("\t\t Elige una opción: ").upper().strip() 
    return opcion

  def menu_notas(self):
    print("\n \t .::  Menu Notas ::. \n\t1.- Crear \n\t2.- Mostrar \n\t3.- Cambiar \n\t4.- Eliminar \n\t5.- Buscar \n\t6.- Salir """)
    opcion = input("\t\t Elige una opción: ").upper().strip()
    return opcion   