import numpy as np
from tensorflow import keras
import os
import json

MAX_LENGTH = 1000  # Define a fixed length for plugin data

def preprocess_data(plugin_data):
    processed_data = [ord(c) for c in plugin_data]
    if len(processed_data) < MAX_LENGTH:
        processed_data += [0] * (MAX_LENGTH - len(processed_data))
    else:
        processed_data = processed_data[:MAX_LENGTH]
    return processed_data

def train_mod_model():
    with open('training_data.json') as f:
        data = json.load(f)
    X_train = np.array([preprocess_data(item['plugin']) for item in data])
    y_train = np.array([item['mod'] for item in data])

    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_shape=(MAX_LENGTH,)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(len(set(y_train)), activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10)
    model.save('mod_generator_model.h5')
    return model

def generate_fabric_mod(plugin_path):
    with open(plugin_path, 'r') as f:
        plugin_data = f.read()

    processed_data = preprocess_data(plugin_data)
    model = keras.models.load_model('mod_generator_model.h5')
    mod_data = model.predict(np.array([processed_data]))[0]

    mod_path = plugin_path.replace('.plugin', '.mod')
    with open(mod_path, 'w') as f:
        f.write(mod_data)
    return mod_path
