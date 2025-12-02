import os 

os.system("cls")

class Coches:
    __marca=""
    __color=""
    __modelo="" 
    __velocidad=0
    __caballaje=0
    __plazas=0







    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self._color= color
        self._marca= marca
        self._modelo= modelo
        self._velocidad= velocidad
        self._caballaje= caballaje
        self._plazas= plazas

    @property
    def color(self):
        return self._color     
    

    @color.setter
    def color(self, color):             
        self._color=color

    
    @property
    def marca(self, marca):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca=marca
  
    @property
    def modelo(self, modelo):
        return self._modelo
    @modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo

    @property
    def velocidad(self, velocidad):
     return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad=velocidad

    @property
    def caballaje(self, caballaje):
        return self._caballaje

    @caballaje.setter
    def caballaje(self, caballaje):
        self._caballaje=caballaje

    @property
    def plazas(self, plazas):
        return self._plazas
    @plazas.setter
    def plazas(self, plazas):
        self._plazas=plazas
#---------------------------------------------------------------------------------------------------------


class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, cargar, caballaje, plazas, eje, capacidad_carga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidad_carga=capacidad_carga


        #metodos set y get

        @property

        def eje(self):
            return self.__eje

        @eje.setter
        def eje(self, eje):
            self.__eje=eje

        @property
        def capacidad_carga(self):
            return self.__capacidad_carga

        @capacidad_carga.setter
        def capacidad_carga(self, capacidad_carga):
            self.__capacidad_carga=capacidad_carga

            #metodos

            def cargar(self,tipo_carga):
                self.__tipo_carga=tipo_carga
                return
            
class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada


        @property
        def traccion(self):
            return self.__traccion
        @traccion.setter
        def traccion(self, traccion):
            self.__traccion=traccion

        @property
        def cerrada(self):
            return self.__cerrada
        @cerrada.setter
        def cerrada(self, cerrada):
            self.__cerrada=cerrada


        def transportar(self, num_pasajeros):
            self.__num_pasajeros=num_pasajeros
            return self.__num_pasajeros
        
