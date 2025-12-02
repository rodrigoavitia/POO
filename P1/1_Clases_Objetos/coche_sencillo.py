import os 

os.system("cls")

class Coches:
    marca=""
    color=""
    modelo="" 
    velocidad=0
    caballaje=0
    plazas=0
    
    def acelerar(self):
        pass
    def frenar(self):
        pass

coche1=Coches()
coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo=2022
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5
    
print(f"Datos del vehiculo: \n Marca: {coche1.marca} \n color: {coche1.color}")