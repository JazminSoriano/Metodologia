import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(base_path, 'atus_anual_2024.csv'))

# 1. Seleccionamos solo las columnas numéricas que tienen sentido comparar
# Convertimos EDAD a numérico (ignorando errores de "Se fugó")
df['EDAD_LIMPIA'] = pd.to_numeric(df['ID_EDAD'], errors='coerce')

columnas_analisis = ['MES', 'ID_DIA', 'ID_HORA', 'EDAD_LIMPIA', 'ANIO']
df_numerico = df[columnas_analisis].dropna()

# 2. Calculamos la matriz de correlación
matriz = df_numerico.corr()

# 3. Creamos la gráfica (Heatmap)
plt.figure(figsize=(10, 8))
sns.heatmap(matriz, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación: Variables de Accidentes 2024')

# 4. Guardar la imagen
plt.savefig(os.path.join(base_path, 'correlacion.png'))
print("--- MATRIZ GENERADA ---")
print("Busca el archivo 'correlacion.png' en tu carpeta.")