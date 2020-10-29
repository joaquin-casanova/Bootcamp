from flask import Flask
from flask_restful import Resource, Api

from resources.hello import HelloWorld
from resources.financial import stock

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(stock,'/api/<string:stock>')

@app.errorhandler(404)
def page_not_found(error):
    return "This endpoint doesn't exist", 400