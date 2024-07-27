from Models.upload import Upload
from Models.base import db
from dotenv import load_dotenv
import os

load_dotenv()

def add_upload(file_name, file_path):
    new_upload = Upload(file_name=file_name, file_path=file_path)
    db.session.add(new_upload)
    db.session.commit()
    return new_upload

def moveFileUploads(files):
    name_files = []
    for file in files:
        file_path = os.getenv('UPLOAD_PATH')
        file_name = file.filename
        name_files.append(file_name)
        file.save(os.path.join(os.getcwd(), file_path, file_name ))
        add_upload(file_name, file_path)
    return name_files 
