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
    url = 'https://restcountries.com/v3.1/all?fields=name,capital,region,population,area,flags,languages,currencies,timezones,borders'
    try:
        respuesta = requests.get(url, timeout = 5)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos
    except requests.exceptions.ConnectionError:
        print('Error: No se pudo conectar a la URL.')
    except requests.exceptions.Timeout:
        print('Error: La solicitud tardó demasiado.')
    except requests.exceptions.HTTPError as e:
        print(f'Error HTTP: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def guardar_json(datos):
    with open('datos_paises/paises.json', 'w', encoding = 'utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii = False, indent = 2)
    print(f'{len(datos)} países guardados')

# PROCESAMIENTO DE DATOS
# Persona 3
def procesar_datos(datos):
    datos_limpios=[]
    for pais in datos:
        # Nombre del país
        nombre = pais.get("name",{}).get("common", "Desconocido")
        # Capital 
        capital = pais.get("capital", ["No disponible"])
        capital = capital[0] if capital else "No disponible"
        # Región 
        region = pais.get("region", "No disponible")
        # Población 
        poblacion = pais.get("population", 0)
        # Area
        area = pais.get("area", 0)
        # Diccionario limpio 
        pais_limpio = {"nombre": nombre, "capital": capital, "region": region, "poblacion": poblacion, "area": area}
        # Agregar a la lista 
        datos_limpios.append(pais_limpio)
    print("Datos procesados correctamente")
    return datos_limpios


# EXPORTACIÓN CSV
# Persona 4
def guardar_csv(datos_limpios):
    ruta = "paises.csv"
    
    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            # Definir nombres de columnas
            campos = ["nombre", "capital", "region", "poblacion", "area"]
            
            writer = csv.DictWriter(archivo, fieldnames=campos)
            
            # Escribir encabezados
            writer.writeheader()
            
            # Escribir filas
            writer.writerows(datos_limpios)
        
        print(f"Archivo CSV generado correctamente en {ruta}")
    
    except Exception as e:
        print(f"Error al guardar el CSV: {e}")

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
    if datos is None:
        print("No se pudieron obtener los datos.")
        return
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
