import numpy as np
from tensorflow.keras.models import load_model
from data_processing import extract_features

# Load the trained model
model = load_model('best_model.h5')

def generate_fabric_mod(plugin_path):
    features = extract_features(plugin_path)
    features_array = np.array([features['commands'] + features['events']])
    mod_code = model.predict(features_array)
    return mod_code

if __name__ == "__MAIN__":
    plugin_path = 'path/to/plugin.json'  # Path to the plugin file to be processed
    mod_code = generate_fabric_mod(plugin_path)
    print("Generated Fabric Mod Code:", mod_code)
