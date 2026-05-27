import requests
import os
import json
import csv
from datetime import datetime

# Crear carpeta para almacenar archivos
os.makedirs("datos_paises", exist_ok=True)

# SOLICITUDES WEB
# Persona 2
def obtener_datos():
    pass

def guardar_json(datos):
    pass

# PROCESAMIENTO DE DATOS
# Persona 3
def procesar_datos(datos):
    pass

# EXPORTACIÓN CSV
# Persona 4
def guardar_csv(datos_limpios):
    pass

# ESTADÍSTICAS
# Persona 5
def generar_estadisticas(datos_limpios):
    pass

# REPORTE FINAL
# Persona 6
def generar_reporte(estadisticas):
    pass


def main():
    print("Inicio del programa")
    
    # Obtener datos desde la API
    datos = obtener_datos()
    # Guardar datos originales en JSON
    guardar_json(datos)
    # Procesar información relevante
    datos_limpios = procesar_datos(datos)
    # Guardar datos limpios en CSV
    guardar_csv(datos_limpios)
    # Generar estadísticas
    estadisticas = generar_estadisticas(datos_limpios)
    # Crear reporte final
    generar_reporte(estadisticas)

    print("Programa finalizado correctamente")

if __name__ == "__main__":
    main()
