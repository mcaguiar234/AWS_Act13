from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo entrenado y el codificador de clases
modelo = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        try:
            # Extraer datos del formulario (con nombres en español)
            datos = {
                "image_count": int(request.form["cantidad_imagenes"]),
                "avg_width": int(request.form["ancho_promedio"]),
                "avg_height": int(request.form["alto_promedio"]),
                "min_width": int(request.form["ancho_minimo"]),
                "min_height": int(request.form["alto_minimo"]),
                "max_width": int(request.form["ancho_maximo"]),
                "max_height": int(request.form["alto_maximo"]),
                "corrupt_files": int(request.form["archivos_corruptos"])
            }

            # Convertir a DataFrame
            df = pd.DataFrame([datos])

            # Realizar la predicción
            prediccion = modelo.predict(df)
            clase = label_encoder.inverse_transform(prediccion)[0]

            # Mostrar resultado en la misma página
            return render_template("form.html", prediccion=clase)

        except Exception as e:
            return f"❌ Error en la predicción: {str(e)}"
    
    # Mostrar formulario vacío si es GET
    return render_template("form.html", prediccion=None)

if __name__ == "__main__":
    app.run(debug=True)
