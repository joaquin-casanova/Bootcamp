# BASIC PYTHON API

This repository contains a basic Flask API with two endpoints. 

The project was tested with Python 3.6.9, however in order to run successfully only is needed Python 3


## Installation
In order to get the correct enviroment to run the project you need to run the following command:
```
python3 -m venv api
```
Then run the following command:

```
source api/bin/activate
```

finally to set up the correct libraries, run the following command:
```
pip3 install -r requirements.txt
```

## How to run 
```
FLASK_ENV=development FLASK_APP=app.py flask run
```

## How to usage

The first endpoint is the default route and return the typical hello world.

The second endpoint return the company profile from https://financialmodelingprep.com

```
/api/<string:stock>
```

If you want to know the APPLE stock price you need following endpoint.

```
/api/AAPL
```

# Testing
In order to test the correct behaviour our basic api the project use pytest.

Open the terminal and run the following command:

```
pytest
```
