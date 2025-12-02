from funciones import Funcion
from usuarios import usuario
from notas import nota
import getpass
import hashlib

#Referencia de inicio de sesión
#menu_notas(19,"Dago","Fiscal")
class App(Funcion):
    def __init__(self):
        self.main()
        
    def hash_password(self,cont):
        return hashlib.sha256(cont.encode()).hexdigest()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=self.menu_usurios()

            if opcion=="1" or opcion=="REGISTRO":
                self.borrarPantalla()
                print("\n \t ..:: Registro en el Sistema ::..")
                nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
                apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
                email=input("\t Ingresa tu email: ").lower().strip()
                password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
                password=self.hash_password(password)
                #Código agregado
                result=usuario.Usuario.registrar(nombre, apellidos, email, password)
                if result:
                    print(f"\n\t ::: SE REGISTRÓ EL USUARIO {nombre} CORRECTAMENTE ::: ")
                else:
                    print(f"\n\t ... No fue posible registrar el usuario en este momento, inténtelo más tarde ...")
                self.esperarTecla()

            elif opcion=="2" or opcion=="LOGIN": 
                self.borrarPantalla()
                print("\n \t ..:: Inicio de Sesión ::.. ")     
                email=input("\t Ingresa tu E-mail: ").lower().strip()
                password=input("\t Ingresa tu contraseña: ").strip()
                password=self.hash_password(password)
                #Código agregado
                lista_usuarios=usuario.Usuario.inicio_sesion(email, password)
                if len(lista_usuarios) > 0:
                    self.menu_notas(lista_usuarios[0], lista_usuarios[1], lista_usuarios[2])
                else:
                    print(f"\n\t ... E-mail y/o contraseña incorrectas, por favor verifique ...")
                    self.esperarTecla()

            elif opcion=="3" or opcion=="SALIR": 
                print("Termino la Ejecución del Sistema")
                opcion=False
                self.esperarTecla()

            else:
                print("Opcion no valida")
                opcion=True
                self.esperarTecla() 

    def menu_notas(self,usuario_id,nombre,apellidos):
        while True:
            self.borrarPantalla()
            print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
            opcion=self.menu_notas()

            if opcion == '1' or opcion=="CREAR":
                self.borrarPantalla()
                print(f"\n \t .:: Crear Nota ::. ")
                titulo=input("\tTitulo: ")
                descripcion=input("\tDescripción: ")
                #Codigo agregado
                resp=nota.Nota.crear_nota(usuario_id,titulo,descripcion)
                if resp:
                    print(f"\n\t ::: SE CREÓ LA NOTA {titulo} CON EXITO ::: ")
                else:
                    print(f"\n\t ... No fue posible crear la nota en este momento, inténtalo más adelante ...")
                self.esperarTecla()    

            elif opcion == '2' or opcion=="MOSTRAR":
                self.borrarPantalla()
                #codigo agregado
                lista=nota.Nota.mostrar_nota(usuario_id)
                if len(lista) > 0:
                    print(f"\n\t .:: Lista de notas de {nombre} ::.")
                    print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<50} {'Fecha':<15}\n{'_'*80}")
                    for i in lista:
                        print(f"{i[0]:<10} {i[2]:15} {i[3]:<50} {i[4]}")
                    print(f"{'_'*80}") 
                else:
                    print(f"\n\t ... No fue posible imprimir las notas porque no hay notas para este usuarios ...")
                self.esperarTecla()

            elif opcion == '3' or opcion=="CAMBIAR":
                self.borrarPantalla()
                lista=nota.Nota.mostrar_nota(usuario_id)
                if len(lista) > 0:
                    print(f"\n\t .:: Lista de notas de {nombre} ::.")
                    print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<50} {'Fecha':<15}\n{'_'*80}")
                    for i in lista:
                        print(f"{i[0]:<10} {i[2]:15} {i[3]:<50} {i[4]}")
                    print(f"{'_'*80}") 
                    a=True
                else:
                    print(f"\n\t ... No fue posible imprimir las notas porque no hay notas para este usuarios ...")
                    a=False
                if a:
                    resp1=input("¿Desea modificar alguna nota? (si/no): ").lower().strip()
                    if resp1 == "si":
                        print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar una nota ::. \n")
                        id = input("\t ID de la nota a actualizar: ")
                        titulo = input("\t Nuevo título: ")
                        descripcion = input("\t Nueva descripción: ")
                        #Codigo agregado
                        resp2=nota.Nota.cambiar_notas(titulo, descripcion, id)
                        if resp2:
                            print(f"\n\t ::: SE ACTUALIZÓ LA NOTA {titulo} CON ÉXITO ::: ")
                    else:
                        print("\n\t ... Se canceló la operación con éxito ... ")
                self.esperarTecla()      

            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla()
                lista=nota.Nota.mostrar_nota(usuario_id)
                if len(lista) > 0:
                    print(f"\n\t .:: Lista de notas de {nombre} ::.")
                    print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<50} {'Fecha':<15}\n{'_'*80}")
                    for i in lista:
                        print(f"{i[0]:<10} {i[2]:15} {i[3]:<50} {i[4]}")
                    print(f"{'_'*80}") 
                    a=True
                else:
                    print(f"\n\t ... No fue posible borrar las notas porque no hay notas para este usuarios ...")
                    a=False
                if a:
                    resp1=input("¿Desea borrar alguna nota? (si/no): ").lower().strip()
                    if resp1 == "si":
                        print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                        id = input("\t ID de la nota a eliminar: ")
                        #Codigo agregado
                        resp=nota.Nota.borrar_notas(id)
                        if resp:
                            print(f"\n\t ::: SE BORRÓ LA NOTA {id} CON ÉXITO ::: ")
                    else:
                        print("\n\t ... Se canceló la operación con éxito ...")
                self.esperarTecla()    
            
            elif opcion == '5' or opcion == "BUSCAR":
                self.borrarPantalla()
                lista=nota.Nota.mostrar_nota(usuario_id)
                if len(lista) > 0:
                    print(f"\n\t .:: Lista de notas de {nombre} ::.")
                    print(f"{'ID':<10} {'Titulo':<15} {'Descripcion':<50} {'Fecha':<15}\n{'_'*80}")
                    for i in lista:
                        print(f"{i[0]:<10} {i[2]:15} {i[3]:<50} {i[4]}")
                    print(f"{'_'*80}") 
                    a=True
                else:
                    print(f"\n\t ... No fue posible buscar las notas porque no hay notas para este usuarios ...")
                    a=False
                if a:
                    c=True
                    while c:
                        b=True
                        while b:
                            try: 
                                id=int(input("\tIngrese la ID de la nota a buscar (si quiere cancelar la operación escriba solo '0'): "))
                            except TypeError:
                                print("\t ... Operación incorrecta, ingrese solo números ...\n")
                                b=True
                            else:
                                b=False
                        if id > 0:
                            nota=nota.Nota.buscar_nota(id)
                            for i in nota:
                                print(f"\n\t\t\t\t{i[4]}\n\n\t\t{i[0]}: {i[2]}\n{i[3]}")
                            print(f"\n\t ::: SE ENCONTRÓ LA NOTA {id} CON ÉXITO ::: ")
                            c=False
                        elif id == 0:
                            print("\n\t ... Se canceló la operación con éxito ...")
                            c=False
                        else:
                            print("\t ID de nota no válido, inténtelo de nuevo")
                            c=True

            elif opcion == '6' or opcion=="SALIR":
                break

            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

if __name__ == "__main__":
    app=App()  