import requests
import pandas as pd

API_KEY = ""
URL = ""

headers = {
    "x-apisports-key": API_KEY
}

# Verificar que las variables de entorno fueron cargadas correctamente
if not API_KEY or not URL:
    raise ValueError("Por favor, revisa que las variables de entorno fueron cargadas correctamente")

# Hacer la solicitud GET a la API
def obtener_datos():
    response = requests.get(URL, headers = headers)

# Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos")
        return None