from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # No ponemos header en la portada (página 1)
        if self.page_no() > 1:
            self.set_font('Arial', 'B', 10)
            self.set_text_color(128, 128, 128) # Gris
            self.cell(0, 10, 'Proyecto V.E.R.A. - Universidad Tecnológica de Durango', 0, 1, 'R')
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def titulo_slide(self, titulo):
        self.set_font('Arial', 'B', 24)
        self.set_text_color(15, 23, 43) # Azul oscuro (Tu color de header)
        self.cell(0, 20, titulo, 0, 1, 'L')
        self.set_draw_color(255, 185, 0) # Amarillo (Tu color de acento)
        self.set_line_width(1)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(10)

    def bullet_point(self, texto):
        self.set_font('Arial', '', 14)
        self.set_text_color(50, 50, 50)
        self.cell(10) # Sangría
        self.cell(5, 10, chr(149), 0, 0) # Punto bullet
        self.multi_cell(0, 10, texto)
        self.ln(2)

    def parrafo(self, texto):
        self.set_font('Arial', '', 12)
        self.set_text_color(80, 80, 80)
        self.multi_cell(0, 8, texto)
        self.ln(5)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# --- DIAPOSITIVA 1: PORTADA ---
pdf.add_page()
pdf.ln(60)
pdf.set_font('Arial', 'B', 40)
pdf.set_text_color(15, 23, 43)
pdf.cell(0, 20, 'V.E.R.A.', 0, 1, 'C')

pdf.set_font('Arial', '', 18)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 15, 'Sistema de Vigilancia Élite de Reconocimiento de Acceso', 0, 1, 'C')

pdf.ln(20)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Universidad Tecnológica de Durango (UTD)', 0, 1, 'C')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Autor: Rodrigo Abdiel Avitia Benitez', 0, 1, 'C')
pdf.cell(0, 10, 'Fecha: Noviembre 2025', 0, 1, 'C')

# --- DIAPOSITIVA 2: EL PROBLEMA ---
pdf.add_page()
pdf.titulo_slide('El Problema: Situación Actual')
pdf.parrafo("Actualmente, dependemos de procesos manuales (pluma y papel) que generan ineficiencias críticas:")
pdf.bullet_point("Congestión: Filas largas por registro manual en bitácoras.")
pdf.bullet_point("Inseguridad: Validación visual propensa a errores humanos.")
pdf.bullet_point("Falta de Datos: Imposible generar reportes históricos inmediatos.")

# --- DIAPOSITIVA 3: LA SOLUCIÓN ---
pdf.add_page()
pdf.titulo_slide('La Solución: Objetivo del Proyecto')
pdf.parrafo("Desarrollar un sistema de software integral para automatizar, gestionar y asegurar el control de acceso vehicular y peatonal en la UTD.")
pdf.ln(5)
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Tecnologías Clave:', 0, 1)
pdf.bullet_point("Python + CustomTkinter (Interfaz Moderna)")
pdf.bullet_point("MySQL (Base de Datos Robusta)")
pdf.bullet_point("Arquitectura MVC (Escalabilidad)")
pdf.ln(5)
pdf.set_fill_color(220, 255, 220) # Fondo verde claro
pdf.set_font('Arial', 'I', 12)
pdf.cell(0, 10, ' Beneficio: Transformar la seguridad de reactiva a proactiva.', 0, 1, 'C', True)

# --- DIAPOSITIVA 4: ALCANCE ---
pdf.add_page()
pdf.titulo_slide('Alcance del Sistema (Módulos)')
pdf.bullet_point("Gestión de Usuarios (RBAC): Roles jerárquicos (Sudote vs Sudito).")
pdf.bullet_point("Registro Vehicular: Base de datos digital de autos y propietarios.")
pdf.bullet_point("Monitoreo en Tiempo Real: Panel visual para guardias con validación inmediata.")
pdf.bullet_point("Reportes Inteligentes: Historial exportable y filtrable.")

# --- DIAPOSITIVA 5: ARQUITECTURA ---
pdf.add_page()
pdf.titulo_slide('Arquitectura de Software')
pdf.parrafo("El sistema sigue el patrón de diseño Modelo-Vista-Controlador (MVC) para asegurar un código limpio y mantenible.")
pdf.bullet_point("Vista: Interfaces gráficas en CustomTkinter.")
pdf.bullet_point("Controlador: Lógica de navegación y reglas de negocio.")
pdf.bullet_point("Modelo: Consultas SQL y gestión de datos.")

# --- DIAPOSITIVA 6: BASE DE DATOS ---
pdf.add_page()
pdf.titulo_slide('Diseño de Base de Datos')
pdf.parrafo("Estructura relacional optimizada para alto rendimiento:")
pdf.bullet_point("Tabla Usuarios: Datos personales y roles.")
pdf.bullet_point("Tabla Vehículos: Marcas, modelos y placas vinculadas.")
pdf.bullet_point("Tabla Imágenes/Registros: Historial de accesos con evidencia.")

# --- DIAPOSITIVA 7: COSTOS ---
pdf.add_page()
pdf.titulo_slide('Planificación y Costos')
pdf.set_font('Arial', '', 12)
pdf.cell(100, 10, 'Costo Total Estimado:', 1, 0, 'L')
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '$28,000.00 MXN', 1, 1, 'R')

pdf.set_font('Arial', '', 12)
pdf.cell(100, 10, 'Duración Estimada:', 1, 0, 'L')
pdf.cell(0, 10, '12 Semanas (3 Meses)', 1, 1, 'R')

pdf.set_font('Arial', '', 12)
pdf.cell(100, 10, 'Esfuerzo Total:', 1, 0, 'L')
pdf.cell(0, 10, '140 Horas hombre', 1, 1, 'R')
pdf.ln(10)
pdf.parrafo("Nota: Este costo cubre el ciclo completo de desarrollo de software.")

# --- DIAPOSITIVA 8: METAS ---
pdf.add_page()
pdf.titulo_slide('Roadmap (Hoja de Ruta)')
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(0, 146, 184) # Azul VERA
pdf.cell(0, 10, 'Corto Plazo (1 mes):', 0, 1)
pdf.bullet_point("Finalizar CRUDs y generar ejecutable (.exe).")

pdf.ln(5)
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Mediano Plazo (3 meses):', 0, 1)
pdf.bullet_point("Implementación en sitio y conexión de cámaras reales.")

pdf.ln(5)
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Largo Plazo (6 meses+):', 0, 1)
pdf.bullet_point("Integración de IA para lectura automática de placas (OCR).")

# GUARDAR PDF
pdf.output("Presentacion_VERA.pdf")
print("¡PDF Generado con éxito: 'Presentacion_VERA.pdf'!")