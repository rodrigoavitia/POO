from model.cochesBD import VehiculoDB

class Controlador:
    def __init__(self):
        self.base_datos = VehiculoDB() 
        
    def _validar_enteros(self, *args):
        try:
            return [int(a) for a in args]
        except ValueError:
            return None

    # CRUD AUTOS
    def insertar_auto(self, id_auto, marca, color, modelo, velocidad, caballaje, plazas):
        if not all([marca, color, modelo, velocidad, caballaje, plazas]):
             return "Error: Todos los campos son obligatorios."
        enteros = self._validar_enteros(velocidad, caballaje, plazas)
        if not enteros:
            return "Error: Velocidad, Caballaje y Plazas deben ser números enteros."
        
        velocidad, caballaje, plazas = enteros
        return self.base_datos.insertar_auto(marca, color, modelo, velocidad, caballaje, plazas)

    def consultar_autos(self):
        return self.base_datos.consultar_autos()

    def cambiar_auto(self, id_auto, marca, color, modelo, velocidad, caballaje, plazas):
        if not all([id_auto, marca, color, modelo, velocidad, caballaje, plazas]):
             return "Error: Todos los campos son obligatorios."
        enteros = self._validar_enteros(id_auto, velocidad, caballaje, plazas)
        if not enteros:
            return "Error: ID, Velocidad, Caballaje y Plazas deben ser números enteros."
        
        id_auto, velocidad, caballaje, plazas = enteros
        return self.base_datos.cambiar_auto(id_auto, marca, color, modelo, velocidad, caballaje, plazas)

    def borrar_auto(self, id_auto):
        if not id_auto:
             return "Error: El ID es obligatorio para borrar."
        id_entero = self._validar_enteros(id_auto)
        if not id_entero:
            return "Error: El ID debe ser un número."
        return self.base_datos.borrar_auto(id_entero[0])

    # CRUD CAMIONETAS
    def insertar_camioneta(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if not all([marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada]):
             return "Error: Todos los campos son obligatorios."
        enteros = self._validar_enteros(velocidad, caballaje, plazas, cerrada)
        if not enteros:
            return "Error: Velocidad, Caballaje, Plazas y Cerrada deben ser números enteros (0 o 1)."
        
        velocidad, caballaje, plazas, cerrada = enteros
        return self.base_datos.insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)

    def consultar_camionetas(self):
        return self.base_datos.consultar_camionetas()

    def cambiar_camioneta(self, id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        if not all([id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada]):
             return "Error: Todos los campos son obligatorios."
        enteros = self._validar_enteros(id_camioneta, velocidad, caballaje, plazas, cerrada)
        if not enteros:
            return "Error: ID, Velocidad, Caballaje, Plazas y Cerrada deben ser números enteros (0 o 1)."
        
        id_camioneta, velocidad, caballaje, plazas, cerrada = enteros
        return self.base_datos.cambiar_camioneta(id_camioneta, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)

    def borrar_camioneta(self, id_camioneta):
        if not id_camioneta:
             return "Error: El ID es obligatorio para borrar."
        id_entero = self._validar_enteros(id_camioneta)
        if not id_entero:
            return "Error: El ID debe ser un número."
        return self.base_datos.borrar_camioneta(id_entero[0])

    # CRUD CAMIONES
    def insertar_camion(self, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        if not all([marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga]):
             return "Error: Todos los campos son obligatorios."
        enteros = self._validar_enteros(velocidad, caballaje, plazas, eje, capacidadcarga)
        if not enteros:
            return "Error: Velocidad, Caballaje, Plazas, Eje y Capacidad de Carga deben ser números enteros."
        
        velocidad, caballaje, plazas, eje, capacidadcarga = enteros
        return self.base_datos.insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga)

    def consultar_camiones(self):
        return self.base_datos.consultar_camiones()

    def cambiar_camion(self, id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        if not all([id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga]):
             return "Error: Todos los campos son obligatorios."
        enteros = self._validar_enteros(id_camion, velocidad, caballaje, plazas, eje, capacidadcarga)
        if not enteros:
            return "Error: ID, Velocidad, Caballaje, Plazas, Eje y Capacidad de Carga deben ser números enteros."
        
        id_camion, velocidad, caballaje, plazas, eje, capacidadcarga = enteros
        return self.base_datos.cambiar_camion(id_camion, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga)

    def borrar_camion(self, id_camion):
        if not id_camion:
             return "Error: El ID es obligatorio para borrar."
        id_entero = self._validar_enteros(id_camion)
        if not id_entero:
            return "Error: El ID debe ser un número."
        return self.base_datos.borrar_camion(id_entero[0])