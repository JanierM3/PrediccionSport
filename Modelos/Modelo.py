from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

def entrenar_modelo(X, y, n_estimators=100, random_state=42):
    modelo = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    modelo.fit(X, y)
    return modelo

def guardar_modelo(modelo, ruta):
    joblib.dump(modelo, ruta)

def cargar_modelo(ruta):
    return joblib.load(ruta)

def actualizar_modelo(modelo, X, y, X_nueva, y_nueva):
    X_actualizado = np.vstack([X, X_nueva])
    y_actualizado = np.concatenate([y, y_nueva])
    modelo.fit(X_actualizado, y_actualizado)
    return modelo
