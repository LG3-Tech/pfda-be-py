from flask import Flask, jsonify, request

from utils.os_functions import saveFiles, removeFiles
from utils.facial_recognition import verifyImages
from utils.document_validation import verifyDocument

app = Flask(__name__)

@app.route("/verify-images", methods=['POST'])
def verify_images():
    try:
      if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({'error': 'Missing images in request'}), 400
      
      image1 = request.files['image1']
      image2 = request.files['image2']

      images = [
         {"name": "image1", "file": image1},
         {"name": "image2", "file": image2},
      ]

      saveFiles(images, "image")
      result = verifyImages()
      removeFiles("image")

      return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/document-validation", methods=['POST'])
def document_validation():
    try:
      if 'document' not in request.files:
        return jsonify({'error': 'Missing document in request'}), 400

      document = request.files['document']
      documents = [{"name": "document", "file": document}]

      saveFiles(documents, "documents")
      result = verifyDocument("cnh")
      removeFiles("documents")

      return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
