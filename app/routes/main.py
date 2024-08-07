from flask import Flask, request, jsonify
from predict import generate_fabric_mod
import os

app = Flask(__name__)

@app.route('/upload_plugin', methods=['POST'])
def upload_plugin():
    if 'plugin' not in request.files:
        return "No file part", 400
    file = request.files['plugin']
    if file.filename == '':
        return "No selected file", 400
    if file:
        file_path = os.path.join('uploaded_plugins', file.filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)
        mod_code = generate_fabric_mod(file_path)
        return jsonify({"mod_code": mod_code})

if __name__ == "__MAIN__":
    app.run(host='0.0.0.0', port=5000)
