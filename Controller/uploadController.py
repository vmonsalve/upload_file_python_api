from flask import Blueprint, jsonify, request
import os
uploadControllerBp = Blueprint('upload', __name__, url_prefix='/api/upload')

@uploadControllerBp.route("/", methods=["POST","GET"])
def upload():
    if request.method == "POST":
        files = request.files.getlist('files')
        name_files = []
        for file in files:
            name_files.append(file.filename)
            print()
            file.save(os.path.join(os.getcwd(), 'Uploads', file.filename)) 
        return jsonify({'msg': name_files})
    return jsonify({'msg':'Upload file'})