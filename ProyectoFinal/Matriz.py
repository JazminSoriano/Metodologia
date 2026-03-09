
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configuración de rutas
base_path = os.path.dirname(__file__)
archivo_maestro = os.path.join(base_path, 'TIJUANA_MASTER.csv')

print("--- Generando Matriz de Correlación de Inteligencia de Negocios ---")

if os.path.exists(archivo_maestro):
    # Cargar los datos integrados
    df = pd.read_csv(archivo_maestro)

    # 1. Preparación de variables para la matriz
    # Convertimos categorías a números para que Python pueda calcular correlaciones
    # Creamos un subconjunto con las variables que realmente impactan el tráfico
    df_analisis = df[['MES', 'ID_HORA', 'ID_DIA', 'AUTOMOVIL', 'MOTOCICLET']].copy()
    
    # Añadimos una variable numérica para el tipo de accidente (Factor de Severidad)
    # Esto ayuda a ver si ciertos horarios se asocian a tipos específicos de choque
    df_analisis['TIPO_NUM'] = df['TIPACCID'].astype('category').cat.codes

    # 2. Calcular la matriz de correlación (Método de Pearson)
    matriz_corr = df_analisis.corr()

    # 3. Diseño visual de la Matriz (Heatmap)
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_corr, annot=True, cmap='RdYlGn', fmt=".2f", linewidths=0.5)
    
    plt.title('Matriz de Correlación: Factores de Siniestralidad en Tijuana (2022-2024)', fontsize=14)
    plt.tight_layout()

    # Guardar el resultado para la tesis
    plt.savefig(os.path.join(base_path, 'matriz_tijuana_final.png'))
    print("✅ ¡ÉXITO! Matriz generada como 'matriz_tijuana_final.png'")
    
    # Tip para la interpretación en tu tesis
    print("\n💡 Tip de BI: Busca valores cercanos a 1 o -1.")
    print("Si ID_HORA y TIPO_NUM tienen correlación, significa que ciertos accidentes son exclusivos de las horas pico.")

else:
    print("❌ Error: Primero debes ejecutar el script de integración para crear TIJUANA_MASTER.csv")