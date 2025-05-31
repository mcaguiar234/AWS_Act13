import joblib

# Datos de prueba
elementos = [[ 149, 133,  133, 93, 68,  162, 140, 0]]
# Cargar el modelo
modelo = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl") 

# Hacer la predicción
prediccion = modelo. predict(elementos)
nombre_clase = label_encoder.inverse_transform(prediccion)
print("Prediccion:", nombre_clase[0])
