#Instanciar los objetos para posteriormente implementarlos

from coches import Coches, Camionetas, Camiones


"""
num_coches=int(input("Cuantos coches quieres crear: "))


for i in range(0,num_coches):
	print(f"Datos del coche {i+1}")
	marca=input("Introduce la marca del coche: ").upper()
	color=input("Introduce el color del coche: ").upper()
	modelo=input("Introduce el modelo del coche: ").upper()
	velocidad=int(input("Introduce la velocidad del coche: "))
	potencia=int(input("Introduce el potencia del coche: "))
	plazas=int(input("Introduce el numero de plazas del coche: "))

"""


coche=Coches("VW", "Blanco", "2020", 220, 200, 5)
print(coche._marca, coche._color, coche._modelo)



	