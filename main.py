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

@app.post("/", response_class=HTMLResponse)
def predecir_desde_formulario(
    request: Request,
    ancho_promedio: int = Form(...),
    alto_promedio: int = Form(...),
    ancho_minimo: int = Form(...),
    alto_minimo: int = Form(...),
    ancho_maximo: int = Form(...),
    alto_maximo: int = Form(...)
):
    df = pd.DataFrame([{
        "avg_width": ancho_promedio,
        "avg_height": alto_promedio,
        "min_width": ancho_minimo,
        "min_height": alto_minimo,
        "max_width": ancho_maximo,
        "max_height": alto_maximo
    }])

    pred = modelo.predict(df)
    clase_raw = label_encoder.inverse_transform(pred)[0]

    # Limpiar o unificar formato para HTML
    clase = clase_raw.strip().lower().replace(" ", "_")

    return templates.TemplateResponse("form.html", {
        "request": request,
        "prediccion": clase
    })
