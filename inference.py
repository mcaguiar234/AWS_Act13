import joblib

# Datos de prueba
elementos = [[ 0, -0.52977177,  0.52644436, -0.64073999, -0.19534317,  1]]
# Cargar el modelo
modelo = joblib.load("modelo.pkl")
# Hacer la predicción
prediccion = modelo. predict(elementos)
print("Prediccion:", prediccion[0])
