#Instanciar los Objetos para posteriormente implementarlos.

from coches import Coches
num_coches=int(input("¿Cuantos coches deseas?: "))


for i in range(0,num_coches):
    print(f"\n\t...Datos del Coche...{i+1}")
    marca=input("Ingrese la marca del coche: ").upper()
    color=input("Ingrese el color del coche: ").upper()
    modelo=input("Ingrese el modelo del coche: ").upper()
    velocidad=int(input("Ingrese la velocidad maxima del coche: "))
    potencia=int(input("Ingrese el caballaje del coche: "))
    plazas=int(input("Ingrese el numero de plazas del coche: "))

    #Crea un objeto o instancia de la clase Coches

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"Datos del Vehiculo \n Marca: {coche1.getMarca()} \n Color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n Velocidad Maxima: {coche1.getVelocidad()} \n Caballaje: {coche1.getCaballaje()} \n Numero de Plazas: {coche1.getPlazas()}")

    print(f"\n\n\t {coche1.acelerar()}")