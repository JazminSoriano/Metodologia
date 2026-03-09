import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_path = os.path.dirname(__file__)
archivo = 'TIJUANA_MASTER.csv'

if os.path.exists(os.path.join(base_path, archivo)):
    df = pd.read_csv(os.path.join(base_path, archivo))
    
    # Agrupamos por año y mes
    tendencia = df.groupby(['FUENTE_ANIO', 'MES']).size().reset_index(name='TOTAL')
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=tendencia, x='MES', y='TOTAL', hue='FUENTE_ANIO', marker='o', palette='Set1')
    
    plt.title('Tendencia Mensual de Incidentes Viales en Tijuana (2022-2024)', fontsize=14)
    plt.xlabel('Mes del Año')
    plt.ylabel('Cantidad de Accidentes')
    plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.grid(True, alpha=0.3)
    
    plt.savefig(os.path.join(base_path, 'tendencia_temporal_tijuana.png'))
    print("✅ Gráfica generada: tendencia_temporal_tijuana.png")
else:
    print("Error: No se encuentra el archivo maestro.")