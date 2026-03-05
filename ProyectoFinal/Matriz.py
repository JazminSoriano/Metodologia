import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configuración de rutas
base_path = os.path.dirname(__file__)
# Asegúrate de que el nombre del archivo coincida con el que quieres graficar
archivo_a_graficar = 'atus_anual_2017.csv' 
df = pd.read_csv(os.path.join(base_path, archivo_a_graficar))

# 1. Limpieza de datos específicos para la matriz
# Convertimos EDAD a numérico (ignorando errores de texto como "Se fugó")
df['EDAD_LIMPIA'] = pd.to_numeric(df['ID_EDAD'], errors='coerce')

# Seleccionamos SOLO las columnas que queremos comparar
columnas_analisis = ['MES', 'ID_DIA', 'ID_HORA', 'EDAD_LIMPIA', 'ANIO']
df_numerico = df[columnas_analisis].dropna()

# 2. Calculamos la matriz usando SOLO el dataframe filtrado
# Este era el error: antes usabas 'df' completo, ahora usamos 'df_numerico'
matriz = df_numerico.corr(numeric_only=True)

# 3. Configuración visual de la gráfica (Heatmap)
plt.figure(figsize=(10, 8))
sns.heatmap(matriz, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Título dinámico
plt.title(f'Matriz de Correlación: Variables de Accidentes {archivo_a_graficar[-8:-4]}')

# 4. Guardar la imagen
plt.savefig(os.path.join(base_path, 'correlacion.png'))
print("--- MATRIZ GENERADA CORRECTAMENTE ---")
print(f"Se analizó el archivo: {archivo_a_graficar}")
print("Busca el archivo 'correlacion.png' en tu carpeta izquierda.")