from flask import Flask, jsonify
from Controller.uploadController import uploadControllerBp
from dotenv import load_dotenv
import os

load_dotenv()

api_mode = os.getenv('API_MODE')
api_host = os.getenv('API_HOST')
api_port = os.getenv('API_PORT')

app = Flask(__name__)

app.register_blueprint(uploadControllerBp)
    
if __name__ == '__main__':
    app.run(debug=api_mode,host=api_host,port=api_port)