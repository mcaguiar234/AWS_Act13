from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Inicializar app
app = FastAPI()

# Cargar modelo y codificador
modelo = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Definir entrada esperada usando Pydantic
class DatosEntrada(BaseModel):
    cantidad_imagenes: int
    ancho_promedio: int
    alto_promedio: int
    ancho_minimo: int
    alto_minimo: int
    ancho_maximo: int
    alto_maximo: int
    archivos_corruptos: int

@app.post("/predecir")
def predecir_clase(datos: DatosEntrada):
    # Convertir datos a DataFrame
    df = pd.DataFrame([{
        "image_count": datos.cantidad_imagenes,
        "avg_width": datos.ancho_promedio,
        "avg_height": datos.alto_promedio,
        "min_width": datos.ancho_minimo,
        "min_height": datos.alto_minimo,
        "max_width": datos.ancho_maximo,
        "max_height": datos.alto_maximo,
        "corrupt_files": datos.archivos_corruptos
    }])

    prediccion = modelo.predict(df)
    clase = label_encoder.inverse_transform(prediccion)[0]
    return {"clase_predicha": clase}
