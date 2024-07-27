
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

mysql_host=os.getenv('MYSQL_HOST')
mysql_user=os.getenv('MYSQL_USER')
mysql_pass=os.getenv('MYSQL_PASS')
mysql_port=os.getenv('MYSQL_PORT')
mysql_name=os.getenv('MYSQL_NAME')

database_uri = f'mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_name}'

# Inicialización de Flask y SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Clase base para los modelos
class BaseModel(db.Model):
    __abstract__ = True