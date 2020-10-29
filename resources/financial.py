from flask_restful import Resource
import requests

API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'

class stock(Resource):
    def get(self, stock):
        data = requests.get(API_URL.format(stock.upper()), params={'apikey':'demo'}).json()
        return data, 200


