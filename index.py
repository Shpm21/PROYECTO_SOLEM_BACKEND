from flask import Flask
from flask_restful import Api, Resource
from app.common.Image import Image
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Image, '/image/')


if __name__ == '__main__':
    app.run(debug=True)