# semaforo.py
import json
from datetime import datetime

class SemaforoInteligente:
    def __init__(self):
        self.historial = []

    def calcular_tiempos(self, flujo_a, flujo_b):
        """
        Calcula el tiempo de luz verde para cada vía basado en el flujo vehicular.
        - flujo_a: cantidad de autos en vía A
        - flujo_b: cantidad de autos en vía B
        Retorna una tupla (tiempo_A, tiempo_B)
        """
        total = flujo_a + flujo_b
        if total == 0:
            return (30, 30)  # tiempos base por defecto

        # proporción del flujo
        tiempo_a = round((flujo_a / total) * 60, 2)
        tiempo_b = round((flujo_b / total) * 60, 2)

        # Guardar registro en historial
        registro = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "flujo_a": flujo_a,
            "flujo_b": flujo_b,
            "tiempo_a": tiempo_a,
            "tiempo_b": tiempo_b
        }
        self.historial.append(registro)
        return (tiempo_a, tiempo_b)

    def guardar_datos(self, archivo="datos.json"):
        with open(archivo, "w") as f:
            json.dump(self.historial, f, indent=4)