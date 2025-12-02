import os
os.system("cls")


"""

num1=int(input("Ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero:"))


def suma():
    suma=num1+num2
    print(suma)

def resta():
    resta=num1-num2
    print(resta)

def multi():
    multi=num1*num2
    print(multi)

def divi():
    divi=num1/num2
    print(divi)


opcion = True
while opcion:
    match opcion:
        case "1":
            suma()
        case "2":
            resta()
        case "3":
            multi()
        case "4":
            divi()

                        """

class Calculadora:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número: "))
        self.num2 = int(input("Ingrese el segundo número: "))

    @property
    def numero1(self):
        return self.numero1
    @numero1.setter
    def numero1(self, numero1):
        self.numero1=numero1

    @property
    def numero2(self):
        return self.numero2
    @numero2.setter
    def numero2(self, numero2):
        self.numero2=numero2

    @property
    def suma(self):
        return self.suma
    
    @suma.setter
    def suma(self, suma):
        self.suma=suma

    @property
    def resta(self):
        return self.resta
    @resta.setter
    def resta(self, resta):
        self.resta=resta

    @property
    def multiplicacion(self):
        return self.multiplicacion
    @multiplicacion.setter
    def multiplicacion(self, multiplicacion):
        self.multiplicacion=multiplicacion

    @property
    def division(self):
        return self.division
    @division.setter
    def division(self, division):
        self.division=division
        

    

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"

# Crear objeto de la clase Calculadora
calc = Calculadora()

print("Suma:", calc.suma())
print("Resta:", calc.resta())
print("Multiplicación:", calc.multiplicacion())
print("División:", calc.division())



