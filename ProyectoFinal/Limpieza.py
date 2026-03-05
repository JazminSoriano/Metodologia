
import pandas as pd
import numpy as np
import os

# Configuramos la ruta al directorio donde está este script
base_path = os.path.dirname(__file__)

print("Iniciando proceso de limpieza...")

# 1. CARGA DE LA BASE PRINCIPAL
# Usamos os.path.join para evitar errores de rutas entre Windows/Linux
try:
    df = pd.read_csv(os.path.join(base_path, 'atus_anual_2023.csv'), 
                    dtype={'ID_ENTIDAD': str, 'ID_MUNICIPIO': str, 'ID_DIA': str})

    # 2. CARGA DE TODOS LOS CATÁLOGOS (Nombres actualizados a 'tc_')
    entidades = pd.read_csv(os.path.join(base_path, 'tc_entidad.csv'), dtype={'ID_ENTIDAD': str})
    municipios = pd.read_csv(os.path.join(base_path, 'tc_municipio.csv'), dtype={'ID_ENTIDAD': str, 'ID_MUNICIPIO': str})
    horas = pd.read_csv(os.path.join(base_path, 'tc_hora.csv'))
    edades = pd.read_csv(os.path.join(base_path, 'tc_edad.csv'))
    dias = pd.read_csv(os.path.join(base_path, 'tc_dia.csv'), dtype={'ID_DIA': str})

    # 3. PROCESO DE UNIÓN (EL "MERGE")
    df = pd.merge(df, entidades, on='ID_ENTIDAD', how='left')
    df = pd.merge(df, municipios, on=['ID_ENTIDAD', 'ID_MUNICIPIO'], how='left')
    df = pd.merge(df, horas, on='ID_HORA', how='left')
    df = pd.merge(df, edades, on='ID_EDAD', how='left')
    df = pd.merge(df, dias, on='ID_DIA', how='left')

    # 4. TRADUCCIÓN DE MESES
    meses_map = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
        7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    df['NOM_MES'] = df['MES'].map(meses_map)

    # 5. SELECCIÓN DE COLUMNAS
    # Nota: Verifica que 'DESC_DIA' y 'DESC_EDAD' existan en tus archivos tc_dias y tc_edades
    columnas_finales = [
        'ANIO', 'NOM_MES', 'DESC_DIA', 'DIASEMANA', 'DESC_HORA', 
        'NOM_ENTIDAD', 'NOM_MUNICIPIO', 'DESC_EDAD', 'SEXO', 
        'TIPACCID', 'CLASACC', 'ALIENTO'
    ]

    # Creamos un dataframe solo con las columnas legibles
    df_reporte = df[columnas_finales].copy()

    # 6. EXPORTACIÓN
    df_reporte.to_csv(os.path.join(base_path, 'BASE_ACCIDENTES_FINAL.csv'), index=False)

    print("--- REPORTE LISTO ---")
    print(f"Se generó el archivo: {os.path.join(base_path, 'BASE_ACCIDENTES_FINAL.csv')}")

except FileNotFoundError as e:
    print(f"ERROR: No se encontró uno de los archivos. Detalles: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")