import requests
import json

import requests

def test_hello_service():
    url = 'http://127.0.0.1:5000'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["Hello"] == "World"
    print(resp.text)

def test_financial_service():
    url = 'http://127.0.0.1:5000/api/AAPL'    
    resp = requests.get(url)           
    assert resp.status_code == 200
    assert resp.json()["symbol"] == "AAPL"
    print(resp.text)