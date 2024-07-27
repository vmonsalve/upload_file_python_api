from flask import Blueprint, jsonify, request
from Helpers.uploads import moveFileUploads

uploadControllerBp = Blueprint('upload', __name__, url_prefix='/api/upload')

@uploadControllerBp.route("/", methods=["POST","GET"])
def upload():
    if request.method == "POST":
        files = request.files.getlist('files')
        name_files = moveFileUploads(files)
        return jsonify({'msg': name_files})
    return jsonify({'msg':'Upload file'})