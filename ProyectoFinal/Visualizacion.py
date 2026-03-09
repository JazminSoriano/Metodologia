import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_path = os.path.dirname(__file__)
archivo = 'DATOS_TIJUANA_LIMPIOS.csv'

if os.path.exists(os.path.join(base_path, archivo)):
    df = pd.read_csv(os.path.join(base_path, archivo))
    
    # 1. Gráfica de Tipos de Accidente
    plt.figure(figsize=(12, 6))
    order = df['TIPACCID'].value_counts().index
    sns.countplot(data=df, y='TIPACCID', order=order, palette='magma')
    plt.title('Tipos de Accidentes más frecuentes en Tijuana (2014)')
    plt.tight_layout()
    plt.savefig(os.path.join(base_path, 'tipos_accidentes_tijuana.png'))
    print("Gráfica 1 generada: tipos_accidentes_tijuana.png")

    # 2. Gráfica de Accidentes por Hora (Para detectar horas pico)
    plt.figure(figsize=(12, 6))
    sns.histplot(df['ID_HORA'], bins=24, kde=True, color='blue')
    plt.title('Distribución de Accidentes por Hora del Día')
    plt.xlabel('Hora (0-23)')
    plt.ylabel('Frecuencia de Accidentes')
    plt.savefig(os.path.join(base_path, 'accidentes_por_hora.png'))
    print("Gráfica 2 generada: accidentes_por_hora.png")
else:
    print("Corre primero limpieza.py")