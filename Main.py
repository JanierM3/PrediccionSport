import os
import pandas as pd
import numpy as np
import time
from Modelos.api import obtener_datos
from Modelos.data_loader import guardar_datos_csv, leer_archivos_en_carpeta
from Modelos.Modelo import entrenar_modelo, guardar_modelo, cargar_modelo

def main():
    # Rutas
    carpeta_datos = './data'
    ruta_modelo = './modelos/modelo_entrenado.pkl'
    ruta_csv_predicciones = './datos/predicciones.csv'

    # Entrenar o cargar el modelo
    if not os.path.exists(ruta_modelo):
        print("No se encontró un modelo. Entrenando uno nuevo...")
        # Ejemplo de datos iniciales para entrenar
        X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        y = np.array([0, 1, 0])
        modelo = entrenar_modelo(X, y)
        guardar_modelo(modelo, ruta_modelo)
    else:
        print("Cargando modelo existente...")
        modelo = cargar_modelo(ruta_modelo)

    print("Iniciando predicción en tiempo real...")
    while True:
        # Leer y procesar datos en tiempo real
        nuevos_datos = leer_archivos_en_carpeta(carpeta_datos)
        
        # Supongamos que los datos nuevos tienen formato consistente para X_nueva
        for dato in nuevos_datos:
            if isinstance(dato, pd.DataFrame):
                for _, fila in dato.iterrows():
                    X_nueva = fila.values
                    prediccion = modelo.predict([X_nueva])
                    print(f"Predicción para {X_nueva}: {prediccion}")

                    # Guardar predicción en CSV
                    fila_con_prediccion = fila.to_dict()
                    fila_con_prediccion["prediccion"] = prediccion[0]
                    guardar_datos_csv([fila_con_prediccion], ruta_csv_predicciones)

        # Esperar antes de repetir el ciclo (simula tiempo real)
        time.sleep(10)  # Revisa cada 10 segundos por nuevos datos

if __name__ == "__main__":
    main()