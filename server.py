from flask import Flask, request
from flask_cors import CORS
import sys
# THIS IS NEEDED TO IMPORT "processRequestImage" WHICH IS STORED IN ANOTHER DIRECTORY
sys.path.append('./cvf')
from imageProcessing import processRequestImage

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    return "<p>holaMundo</p>"


@app.route("/images", methods=['POST'])
def httpImagesRepo():
    if (request.files):
        imagefile = request.files.get('imagefile', '')
        return processRequestImage(imagefile)
    else:
        return "Por favor, envía una imagen"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
