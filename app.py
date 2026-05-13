import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import gdown
import os

MODEL_PATH = "model.keras"

# Download model if not already present
if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/uc?id=1LMQYMI9hBLYfg627YDCJ9doAoZ8l-C1X"
    gdown.download(url, MODEL_PATH, quiet=False)

# Load model
model = tf.keras.models.load_model(MODEL_PATH)
