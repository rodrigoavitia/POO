# /controller/controlador.py
from model import cochesBD
from tkinter import messagebox
# La interfaz se importa para las llamadas de cambio de pantalla después de buscar el ID
from view import interfaz 

# --- Controlador para Autos (Clase renombrada de 'Controladores' a 'AutosControlador') ---
class AutosControlador:
    
    @staticmethod
    def insertar_coche(marca, color, modelo, velocidad, potencia, plazas):
        try:
            # Asegurar que los datos numéricos sean INT
            velocidad = int(velocidad)
            potencia = int(potencia)
            plazas = int(plazas)
        except ValueError:
            messagebox.showinfo(message="Velocidad, Potencia y Plazas deben ser números.", title="Error de Datos", icon="warning")
            return

        respuesta = cochesBD.Autos.insertar(marca, color, modelo, velocidad, potencia, plazas)
        if respuesta:
            messagebox.showinfo(message="El coche se ha agregado con éxito", title="Agregar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Ha ocurrido un error", icon="warning")

    @staticmethod
    def mostrar_coche():
        registros = cochesBD.Autos.consultar()
        if len(registros) == 0:
            messagebox.showinfo(message="No existe ningún registro de coches por el momento", title="No hay registros", icon="warning")
        return registros

    @staticmethod
    def actualizar_coche(marca, color, modelo, velocidad, potencia, plazas, id):
        try:
            # Asegurar que los datos numéricos sean INT
            velocidad = int(velocidad)
            potencia = int(potencia)
            plazas = int(plazas)
            id = int(id)
        except ValueError:
            messagebox.showinfo(message="Velocidad, Potencia, Plazas e ID deben ser números.", title="Error de Datos", icon="warning")
            return

        respuesta = cochesBD.Autos.actualizar(marca, color, modelo, velocidad, potencia, plazas, id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha cambiado el coche de id: {id} con éxito", title="Modificar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción. Verifique el ID.", title="Ha ocurrido un error", icon="warning")
    
    @staticmethod
    def eliminar_coche(id):
        try:
            id = int(id)
        except ValueError:
            messagebox.showinfo(message="El ID debe ser un número entero.", title="Error de Datos", icon="warning")
            return
            
        respuesta = cochesBD.Autos.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha eliminado el coche de id: {id} con éxito", title="Eliminar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción. Verifique el ID.", title="Ha ocurrido un error", icon="warning")

    @staticmethod
    def buscarId_eliminar(ventana, opid, tipo):
        registro = cochesBD.Autos.consultar() 
        confirmacion = False
        for filas in registro:
            if filas[0] == opid:
                confirmacion = True
                # Llama a la interfaz específica de COCHES
                interfaz.InterfacesMenu.coches_eliminar(ventana, opid)
                return
        
        if not confirmacion:
            messagebox.showinfo(message="No se encontró el ID en los registros de Coches", title="Ocurrió un problema")

    @staticmethod
    def buscarId_modificar(ventana, opid, tipo):
        registro = cochesBD.Autos.consultar()
        confirmacion = False
        for filas in registro:
            if filas[0] == opid:
                confirmacion = True
                # Llama a la interfaz específica de COCHES
                interfaz.InterfacesMenu.coches_cambiar(ventana, opid)
                return
        
        if not confirmacion:
            messagebox.showinfo(message="No se encontró el ID en los registros de Coches", title="Ocurrió un problema")


# --- Controlador para Camionetas ---
class CamionetasControlador:
    
    @staticmethod
    def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            velocidad = int(velocidad)
            caballaje = int(caballaje)
            plazas = int(plazas)
            # Convertir 'Si'/'No' a booleano/entero (1/0)
            cerrada_val = 1 if cerrada == "Si" else 0
        except ValueError:
            messagebox.showinfo(message="Velocidad, Potencia y Plazas deben ser números.", title="Error de Datos", icon="warning")
            return

        respuesta = cochesBD.Camionetas.insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada_val)
        if respuesta:
            messagebox.showinfo(message="La camioneta se ha agregado con éxito", title="Agregar camioneta")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Ha ocurrido un error", icon="warning")

    @staticmethod
    def mostrar_camioneta():
        registros = cochesBD.Camionetas.consultar()
        if len(registros) == 0:
            messagebox.showinfo(message="No existe ningún registro de camionetas", title="No hay registros", icon="warning")
        return registros

    @staticmethod
    def actualizar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        try:
            velocidad = int(velocidad)
            caballaje = int(caballaje)
            plazas = int(plazas)
            id = int(id)
            cerrada_val = 1 if cerrada == "Si" else 0
        except ValueError:
            messagebox.showinfo(message="Verifique que los campos numéricos sean correctos.", title="Error de Datos", icon="warning")
            return
            
        respuesta = cochesBD.Camionetas.actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada_val, id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha cambiado la camioneta de id: {id} con éxito", title="Modificar camioneta")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción. Verifique el ID.", title="Ha ocurrido un error", icon="warning")
    
    @staticmethod
    def eliminar_camioneta(id):
        try:
            id = int(id)
        except ValueError:
            messagebox.showinfo(message="El ID debe ser un número entero.", title="Error de Datos", icon="warning")
            return

        respuesta = cochesBD.Camionetas.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha eliminado la camioneta de id: {id} con éxito", title="Eliminar camioneta")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción. Verifique el ID.", title="Ha ocurrido un error", icon="warning")

    @staticmethod
    def buscarId_eliminar(ventana, opid, tipo):
        registro = cochesBD.Camionetas.consultar()
        confirmacion = False
        for filas in registro:
            if filas[0] == opid:
                confirmacion = True
                # Llama a la interfaz específica de CAMIONETAS
                interfaz.InterfacesMenu.camionetas_eliminar(ventana, opid) 
                return
        
        if not confirmacion:
            messagebox.showinfo(message="No se encontró el ID en los registros de Camionetas", title="Ocurrió un problema")

    @staticmethod
    def buscarId_modificar(ventana, opid, tipo):
        registro = cochesBD.Camionetas.consultar()
        confirmacion = False
        for filas in registro:
            if filas[0] == opid:
                confirmacion = True
                # Llama a la interfaz específica de CAMIONETAS
                interfaz.InterfacesMenu.camionetas_cambiar(ventana, opid) 
                return
        
        if not confirmacion:
            messagebox.showinfo(message="No se encontró el ID en los registros de Camionetas", title="Ocurrió un problema")

# --- Controlador para Camiones ---
class CamionesControlador:
    
    @staticmethod
    def insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
        try:
            velocidad = int(velocidad)
            caballaje = int(caballaje)
            plazas = int(plazas)
            eje = int(eje)
            capacidadcarga = int(capacidadcarga)
        except ValueError:
            messagebox.showinfo(message="Velocidad, Potencia, Plazas, Eje y Capacidad deben ser números.", title="Error de Datos", icon="warning")
            return

        respuesta = cochesBD.Camiones.insertar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga)
        if respuesta:
            messagebox.showinfo(message="El camión se ha agregado con éxito", title="Agregar camión")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Ha ocurrido un error", icon="warning")

    @staticmethod
    def mostrar_camion():
        registros = cochesBD.Camiones.consultar()
        if len(registros) == 0:
            messagebox.showinfo(message="No existe ningún registro de camiones", title="No hay registros", icon="warning")
        return registros

    @staticmethod
    def actualizar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga, id):
        try:
            velocidad = int(velocidad)
            caballaje = int(caballaje)
            plazas = int(plazas)
            eje = int(eje)
            capacidadcarga = int(capacidadcarga)
            id = int(id)
        except ValueError:
            messagebox.showinfo(message="Verifique que los campos numéricos sean correctos.", title="Error de Datos", icon="warning")
            return

        respuesta = cochesBD.Camiones.actualizar(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga, id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha cambiado el camión de id: {id} con éxito", title="Modificar camión")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción. Verifique el ID.", title="Ha ocurrido un error", icon="warning")
    
    @staticmethod
    def eliminar_camion(id):
        try:
            id = int(id)
        except ValueError:
            messagebox.showinfo(message="El ID debe ser un número entero.", title="Error de Datos", icon="warning")
            return

        respuesta = cochesBD.Camiones.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha eliminado el camión de id: {id} con éxito", title="Eliminar camión")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción. Verifique el ID.", title="Ha ocurrido un error", icon="warning")

    @staticmethod
    def buscarId_eliminar(ventana, opid, tipo):
        registro = cochesBD.Camiones.consultar()
        confirmacion = False
        for filas in registro:
            if filas[0] == opid:
                confirmacion = True
                # Llama a la interfaz específica de CAMIONES
                interfaz.InterfacesMenu.camiones_eliminar(ventana, opid) 
                return
        
        if not confirmacion:
            messagebox.showinfo(message="No se encontró el ID en los registros de Camiones", title="Ocurrió un problema")

    @staticmethod
    def buscarId_modificar(ventana, opid, tipo):
        registro = cochesBD.Camiones.consultar()
        confirmacion = False
        for filas in registro:
            if filas[0] == opid:
                confirmacion = True
                # Llama a la interfaz específica de CAMIONES
                interfaz.InterfacesMenu.camiones_cambiar(ventana, opid) 
                return
        
        if not confirmacion:
            messagebox.showinfo(message="No se encontró el ID en los registros de Camiones", title="Ocurrió un problema")