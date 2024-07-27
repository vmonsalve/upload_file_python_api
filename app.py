from flask import Flask
from flask_migrate import Migrate
from Models.base import database_uri, db
from Controller.uploadController import uploadControllerBp
from Models.upload import Upload
from dotenv import load_dotenv
import os

load_dotenv()

api_mode = os.getenv('API_MODE')
api_host = os.getenv('API_HOST')
api_port = os.getenv('API_PORT')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(uploadControllerBp)

if __name__ == '__main__':
    app.run(debug=api_mode,host=api_host,port=api_port)