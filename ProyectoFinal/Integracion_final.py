import pandas as pd
import os

base_path = os.path.dirname(__file__)
anios_validos = [2022, 2023, 2024]
lista_df = []

print("--- Integrando Datos de Tijuana (2022-2024) ---")

for anio in anios_validos:
    archivo = f'atus_anual_{anio}.csv'
    df = pd.read_csv(os.path.join(base_path, archivo), low_memory=False)
    
    # Filtrar Tijuana (Entidad 2, Municipio 4)
    df_temp = df[(df['ID_ENTIDAD'].astype(str).isin(['2', '02'])) & 
                 (df['ID_MUNICIPIO'].astype(str).isin(['4', '004']))].copy()
    
    # Agregar columna de origen para auditoría de datos
    df_temp['FUENTE_ANIO'] = anio
    lista_df.append(df_temp)
    print(f"Añadido {anio}: {len(df_temp)} registros.")

# Unir todos los años
df_final = pd.concat(lista_df, ignore_index=True)

# Guardar el archivo maestro
df_final.to_csv(os.path.join(base_path, 'TIJUANA_MASTER.csv'), index=False)
print(f"\n✅ INTEGRACIÓN TOTAL: {len(df_final)} registros guardados en TIJUANA_MASTER.csv")