from flask import Flask , request
from flask_restful import Resource, Api,reqparse
import json
from werkzeug.datastructures import FileStorage #image

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('image', type=FileStorage, location='files') #image

class Home(Resource):
	def get(self):
		return {"message":"'./born'to calculate age or'./image'to upload image"}

class Image(Resource):
	def get(self):
		return {"message":"Plese sent 'image'(POST method) to me."}
	def post(self):
		args = parser.parse_args()
		image = args['image']
		image_name = image.filename
		image.save(image_name)
		return {"coda":200,"desc":"Upload success"}
api.add_resource(Home,'/')
api.add_resource(Image,'/image')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)


