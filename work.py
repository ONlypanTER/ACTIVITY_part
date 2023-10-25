from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def cargar_datos_desde_archivo(self) -> Tuple[list, list]:
        temperatura = []
        humedad = []
        presion = []
        velocidad_viento = []
        direccion_viento_grados = []
        
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if "Temperatura:" in linea:
                    temperatura.append(float(linea.split(":")[1]))
                elif "Humedad:" in linea:
                    humedad.append(float(linea.split(":")[1]))
                elif "Presión:" in linea:
                    presion.append(float(linea.split(":")[1]))
                elif "Viento:" in linea:
                    viento_info = linea.split(":")[1].split(",")
                    velocidad_viento.append(float(viento_info[0]))
                    direccion_viento = viento_info[1].strip()
                    direccion_viento_grados.append(self.obtener_grados_direccion(direccion_viento))

        return temperatura, humedad, presion, velocidad_viento, direccion_viento_grados

    def obtener_grados_direccion(self, direccion: str) -> float:
        direcciones_a_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
            "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }
        return direcciones_a_grados.get(direccion, 0)

    def calcular_promedios(self, datos: Tuple[list, list, list, list, list]) -> Tuple[float, float, float, float, str]:
        temperatura, humedad, presion, velocidad_viento, direccion_viento_grados = datos

        promedio_temperatura = sum(temperatura) / len(temperatura)
        promedio_humedad = sum(humedad) / len(humedad)
        promedio_presion = sum(presion) / len(presion)
        promedio_velocidad_viento = sum(velocidad_viento) / len(velocidad_viento)

        promedio_direccion_viento_grados = sum(direccion_viento_grados) / len(direccion_viento_grados)
        direccion_viento_predominante = min(self.obtener_direcciones(direccion_viento_grados), key=lambda x: abs(x - promedio_direccion_viento_grados))

        return promedio_temperatura, promedio_humedad, promedio_presion, promedio_velocidad_viento, direccion_viento_predominante

    def obtener_direcciones(self, grados: list) -> list:
        direcciones_a_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
            "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }
        return
