import pandas as pd
import os

base_path = os.path.dirname(__file__)
rango_anios = range(2014, 2025) # De 2014 a 2024
archivos_encontrados = []

print("--- REVISIÓN GLOBAL DE BASES DE DATOS (2014-2024) ---")
print(f"Buscando Tijuana (Entidad 2, Municipio 4) en cada archivo...\n")

for anio in rango_anios:
    archivo = f'atus_anual_{anio}.csv'
    ruta_completa = os.path.join(base_path, archivo)
    
    if os.path.exists(ruta_completa):
        try:
            # Leemos solo una parte o usamos low_memory para no trabar la PC
            df = pd.read_csv(ruta_completa, low_memory=False)
            
            # Limpieza rápida de columnas para asegurar el match
            df['ID_ENTIDAD'] = pd.to_numeric(df['ID_ENTIDAD'], errors='coerce')
            df['ID_MUNICIPIO'] = pd.to_numeric(df['ID_MUNICIPIO'], errors='coerce')
            
            # Contamos cuántos registros hay de Tijuana
            conteo = len(df[(df['ID_ENTIDAD'] == 2) & (df['ID_MUNICIPIO'] == 4)])
            
            if conteo > 0:
                print(f"✅ {archivo}: ¡EXITO! Se encontraron {conteo} registros.")
                archivos_encontrados.append((archivo, conteo))
            else:
                print(f"⚠️  {archivo}: Existe el archivo, pero tiene 0 registros de Tijuana.")
                
        except Exception as e:
            print(f"❌ {archivo}: Error al leer el archivo ({e})")
    else:
        print(f"🌑 {archivo}: No se encontró el archivo en la carpeta.")

print("\n--- RESUMEN FINAL ---")
if archivos_encontrados:
    print(f"Puedes usar {len(archivos_encontrados)} archivos para tu proyecto de BI.")
else:
    print("Ninguno de los archivos revisados contiene datos de Tijuana.")