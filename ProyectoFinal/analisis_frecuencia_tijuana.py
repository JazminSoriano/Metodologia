import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

base_path = os.path.dirname(__file__)
archivo_maestro = os.path.join(base_path, 'TIJUANA_MASTER.csv')

if os.path.exists(archivo_maestro):
    df = pd.read_csv(archivo_maestro)
    
    # 1. Contar frecuencias de tipos de accidentes
    frecuencias = df['TIPACCID'].value_counts().reset_index()
    frecuencias.columns = ['Tipo de Accidente', 'Total']
    
    # 2. Crear la visualización
    plt.figure(figsize=(12, 7))
    sns.set_style("whitegrid")
    
    # Gráfica de barras horizontales para mejor lectura
    ax = sns.barplot(data=frecuencias, x='Total', y='Tipo de Accidente', palette='viridis')
    
    # Añadir los números exactos al final de cada barra
    for i, p in enumerate(ax.patches):
        ax.annotate(f'{int(p.get_width())}', 
                    (p.get_width(), p.get_y() + p.get_height() / 2), 
                    ha='left', va='center', xytext=(5, 0), textcoords='offset points')

    plt.title('Tipología de Siniestralidad Vial en Tijuana (2022-2024)', fontsize=15, pad=20)
    plt.xlabel('Cantidad de Registros', fontsize=12)
    plt.ylabel('Categoría de Incidente', fontsize=12)
    plt.tight_layout()

    # Guardar para la tesis
    plt.savefig(os.path.join(base_path, 'frecuencia_accidentes_tijuana.png'))
    print("✅ Gráfica generada: frecuencia_accidentes_tijuana.png")
    
    # Mostrar el Top 3 en la terminal para tu análisis
    print("\n--- TOP 3 INCIDENTES EN TIJUANA ---")
    print(frecuencias.head(3).to_string(index=False))

else:
    print("❌ No se encontró el archivo maestro.")