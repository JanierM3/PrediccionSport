import os
import pandas as pd

def guardar_datos_csv(datos, ruta):
    df = pd.DataFrame(datos)
    df.to_csv(ruta, mode='a', header=not os.path.exists(ruta), index=False)

def cargar_datos_csv(ruta):
    return pd.read_csv(ruta)

def leer_archivos_en_carpeta(carpeta):
    datos = []
    for root, _, files in os.walk(carpeta):
        for file in files:
            if file.endswith(('.csv', '.json', '.txt', '.md')):
                ruta_archivo = os.path.join(root, file)
                if file.endswith('.csv'):
                    datos.append(pd.read_csv(ruta_archivo))
                elif file.endswith('.json'):
                    datos.append(pd.read_json(ruta_archivo))
                elif file.endswith('.txt') or file.endswith('.md'):
                    with open(ruta_archivo, 'r') as f:
                        datos.append(f.read())
    return datos
