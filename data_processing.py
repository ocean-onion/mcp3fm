import json
import os

def extract_features(plugin_path):
    # Function to extract features from a Minecraft plugin
    features = {}
    with open(plugin_path, 'r') as file:
        data = json.load(file)
        features['name'] = data.get('name', '')
        features['commands'] = data.get('commands', [])
        features['events'] = data.get('events', [])
    return features

def load_and_process_data(directory):
    # Load and process all plugins in the specified directory
    processed_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            plugin_path = os.path.join(directory, filename)
            features = extract_features(plugin_path)
            processed_data.append(features)
    return processed_data

if __name__ == "__main__":
    data_directory = 'plugins'  # Directory where plugins are stored
    processed_data = load_and_process_data(data_directory)
    print("Data loaded and processed:", processed_data)
