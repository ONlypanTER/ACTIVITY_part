from work import DatosMeteorologicos

nombre_archivo = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(nombre_archivo)
resultados = datos.calcular_promedios()
print("Temperatura promedio:", resultados[0])
print("Humedad promedio:", resultados[1])
print("Presión promedio:", resultados[2])
print("Velocidad promedio del viento:", resultados[3])
print("Dirección predominante del viento:", resultados[4])
