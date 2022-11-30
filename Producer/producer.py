from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json
import requests




# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def getbroker():
    x = requests.get('http://localhost:5000/bro')
    y = json.loads(x.text)
    global url
    url = y["url"]
    url = url + "/post"
    data = {
        "topic" : "test",
        "data" : "This is test data"
    }
    pos = requests.post(url,json=data)
    return str(pos.status_code)



















# Running app
def run(portd):
    app.run(host="0.0.0.0",port=portd,debug=False)
    