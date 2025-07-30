import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load your trained model (optional, if you already trained one)
model = tf.keras.models.load_model('models/your_model.h5')

st.title("Pneumonia Detection from X-ray")

uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded X-ray", use_container_width=True)


    # Resize and preprocess image (change according to your model)
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict (if model is loaded)
    prediction = model.predict(img_array)
    st.write(f"Prediction: {'Pneumonia' if prediction[0][0] > 0.5 else 'Normal'}")

    st.write("Model prediction code here (uncomment after loading model)")
