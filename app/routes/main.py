import os
from flask import Flask
from config import Config
from app import create_app, db

app = create_app(Config)

@app.shell_context_processor
def make_shell_context():
    return {'db': db}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
