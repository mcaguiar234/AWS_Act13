# 👟 Predicción de Marca de Calzado con FastAPI

Este proyecto es una aplicación web construida con **FastAPI** que permite predecir la **marca de un zapato** a partir de características visuales como el ancho y alto promedio, mínimo y máximo extraídas de imágenes.

Incluye una interfaz web amigable con un formulario moderno y resultados ilustrados con imágenes representativas de cada marca.

---

## 🧠 Tecnologías usadas

- Python 3.9+
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- Joblib
- Jinja2 (para templates HTML)
- HTML/CSS personalizado

---

## 📦 Estructura del proyecto

AWS_Act13/
├── main.py # Backend principal en FastAPI
├── random_forest_model.pkl # Modelo entrenado
├── label_encoder.pkl # Codificador de clases
├── requirements.txt # Dependencias del proyecto
└── templates/
└── form.html # Formulario web interactivo

## Accede a la app
http://3.141.11.75:8000

## 🧪 ¿Cómo funciona?
El usuario ingresa características del calzado:

Ancho y alto promedio

Ancho y alto mínimo

Ancho y alto máximo

El sistema predice la marca del zapato usando un modelo Random Forest entrenado con datos reales.

Se muestra la marca predicha acompañada de una imagen ilustrativa.

## 📸 Marcas soportadas con imagen
Actualmente el sistema reconoce y muestra imágenes para marcas como:
- Adidas Ultraboost
- Nike Air Max
- New Balance 550
- Vans SK8-Hi
Si no se reconoce una marca específica, se muestra un icono de zapato genérico.



