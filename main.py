from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Cargar modelo y codificador
modelo = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "prediccion": None})

@app.post("/", response_class=HTMLResponse)
def predecir_desde_formulario(
    request: Request,
    cantidad_imagenes: int = Form(...),
    ancho_promedio: int = Form(...),
    alto_promedio: int = Form(...),
    ancho_minimo: int = Form(...),
    alto_minimo: int = Form(...),
    ancho_maximo: int = Form(...),
    alto_maximo: int = Form(...),
    archivos_corruptos: int = Form(...)
):
    # Crear DataFrame con nombres que espera el modelo
    df = pd.DataFrame([{
        "image_count": cantidad_imagenes,
        "avg_width": ancho_promedio,
        "avg_height": alto_promedio,
        "min_width": ancho_minimo,
        "min_height": alto_minimo,
        "max_width": ancho_maximo,
        "max_height": alto_maximo,
        "corrupt_files": archivos_corruptos
    }])
    pred = modelo.predict(df)
    clase = label_encoder.inverse_transform(pred)[0]
    return templates.TemplateResponse("form.html", {"request": request, "prediccion": clase})
