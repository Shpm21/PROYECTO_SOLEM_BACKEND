from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys
# THIS IS NEEDED TO IMPORT "processRequestImage" WHICH IS STORED IN ANOTHER DIRECTORY
sys.path.append('./cvf')
from imageProcessing import getTextFromSampleImage, getTextFromImageBytes

# getTextFromSampleImage()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET'])
@cross_origin()
def httpGetTextFromSampleImage():
    return getTextFromSampleImage()
    # import io
    # import requests
    # from PIL import Image
    # r = requests.get('https://www.bimbaylola.com/media/catalog/product/1/8/182BAC104_T2200_P_T_XX_1.jpg', stream=True)
    # print(r)
    # print(type(r))
    # return "chaoooooooooooooooo"


@app.route("/images", methods=['POST'])
@cross_origin()
def httpImagesRepo():
    
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return getTextFromImageBytes(imgBytes)
    else:
        return "Por favor, envía una imagen"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
