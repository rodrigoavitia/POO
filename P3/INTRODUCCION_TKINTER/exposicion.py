import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 

def convertir():
    
    try:
    
        celsius = float(entrada_celsius.get())
        
        
        fahrenheit = (celsius * 9/5) + 32
        
        
        resultado_output.set(f"{celsius:.2f} °C son equivalentes a {fahrenheit:.2f} °F")
        
    except ValueError:

        messagebox.showerror("Error de Entrada", "Por favor, introduce un número válido.")
        entrada_celsius.delete(0, tk.END) # Limpia el campo de entrada


ventana = tk.Tk()
ventana.title("Conversor °C a °F (Simple)")


resultado_output = tk.StringVar(value="Introduce la temperatura.") 



entrada_celsius = ttk.Entry(ventana, width=10)
entrada_celsius.grid(row=0, column=0, padx=5, pady=10)
entrada_celsius.focus()


ttk.Label(ventana, text="Grados Celsius (°C)").grid(row=0, column=1, padx=5, pady=10, sticky='w')


boton_convertir = ttk.Button(ventana, 
                            text="Convertir", 
                            command=convertir) # Llama a la función simple
boton_convertir.grid(row=1, column=0, columnspan=2, pady=10)


etiqueta_resultado = ttk.Label(ventana, 
                            textvariable=resultado_output, 
                            font=('Arial', 12, 'bold'))
etiqueta_resultado.grid(row=2, column=0, columnspan=2, pady=10)


ventana.mainloop()