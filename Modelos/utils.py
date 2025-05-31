import joblib
import pandas as pd
import os

def guardar_modelo(modelo, nombre_archivo):
    joblib.dump(modelo, nombre_archivo)

def cargar_modelo(nombre_archivo):
    return joblib.load(nombre_archivo)

def guardar_datos_csv(datos, nombre_archivo):
    df = pd.DataFrame(datos)
    df.to_csv(nombre_archivo, mode='a', header=not os.path.exists(nombre_archivo), index=False)

