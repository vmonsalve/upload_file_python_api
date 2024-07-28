# Upload api python

Desarrollo de un upload de archivos, guardando los nombres de las imagenes en una base de datos, y enviandolas a un servicio s3 de amazon.

## Desarrollador

Vicente Antonio Monsalve Vargas.

## Stack

 * Python 3.11.7
 * Flask
 * SqlAlchemy
 * MySQL

## Archivos .env

```
API_MODE=True
API_HOST="0.0.0.0"
API_PORT=1337

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASS=xxx
MYSQL_PORT=3306
MYSQL_NAME=db_upload

UPLOAD_PATH=Uploads
```
## Instalar dependencias

```
pip install -r requirements.txt
```

## Endpoint

```
http://127.0.0.1:1337/api/upload
```