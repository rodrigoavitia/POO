import roboflow
from ultralytics import YOLO
import cv2
import numpy as np
import easyocr # Asegúrate de tener: pip install easyocr

class LicensePlateDetector:
    def __init__(self, model_name='model/weights/best.pt'):
        """Inicializa el modelo YOLO y el lector OCR."""
        self.model = YOLO(model_name) 
        self.cap = None
        # GPU=True si tienes CUDA configurado, sino False
        self.ocr_reader = easyocr.Reader(['en'], gpu=False) 
        print(f"YOLO model {model_name} initialized.")

    def predict_frame(self, frame_numpy_array):
        """
        Ejecuta la detección y el OCR en un solo frame.
        Retorna: (frame_anotado, texto_placa)
        """
        # 1. Detección YOLO
        results = self.model.predict(frame_numpy_array, conf=0.5, verbose=False)
        
        placa_texto = None
        annotated_frame = frame_numpy_array

        if results and results[0].boxes and len(results[0].boxes) > 0:
            # Dibujar cajas
            annotated_frame = results[0].plot()

            # 2. Recorte para OCR
            box = results[0].boxes.xyxy[0].cpu().numpy().astype(int)
            x1, y1, x2, y2 = box
            
            try:
                # Validar coordenadas dentro de la imagen
                h, w, _ = frame_numpy_array.shape
                y1, y2 = max(0, y1), min(h, y2)
                x1, x2 = max(0, x1), min(w, x2)
                
                placa_recortada = frame_numpy_array[y1:y2, x1:x2]
                
                # 3. Lectura OCR
                lectura = self.ocr_reader.readtext(
                    placa_recortada, 
                    allowlist='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ- ', 
                    detail=0
                )
                
                if lectura:
                    # Limpiar texto (quitar espacios, guiones si quieres)
                    placa_texto = "".join(lectura).replace(' ', '').upper()
                    
            except Exception as e:
                print(f"Error OCR: {e}")
                placa_texto = None
            
        return annotated_frame, placa_texto

    def stop_camera(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()