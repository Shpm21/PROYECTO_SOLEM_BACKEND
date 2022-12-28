from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys
# THIS IS NEEDED TO IMPORT "ImageProcessor" WHICH IS STORED IN ANOTHER DIRECTORY
sys.path.append('./cvf')
# from ImageProcessor import getTextFromSampleImage, getTextFromImageBytes
from ImageProcessor import ImageProcessor

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['GET'])
@cross_origin()
def httpGetTextFromSampleImage():    
    return ImageProcessor.getTextFromSampleImage()

@app.route("/images", methods=['POST'])
@cross_origin()
def httpGetTextFromUploadedImage():
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return ImageProcessor.getTextFromImageBytes(imgBytes)
    else:
        return "Por favor, envía una imagen"


@app.route("/enhanced_images_v1", methods=['POST'])
@cross_origin()
def httpGetTextFromUploadedImageEcualized_v1():
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return ImageProcessor.getTextFromImageBytesEcualized_v1(imgBytes)
    else:
        return "Por favor, envía una imagen"


@app.route("/enhanced_images_v2", methods=['POST'])
@cross_origin()
def httpGetTextFromUploadedImageEcualized_v2():
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return ImageProcessor.getTextFromImageBytesEcualized_v2(imgBytes)
    else:
        return "Por favor, envía una imagen"


@app.route("/testHist", methods=['POST'])
@cross_origin()
def httpTestHistogramEqualization():
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return ImageProcessor.showHistFromImgBytes(imgBytes)
    else:
        return "Por favor, envía una imagen"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
