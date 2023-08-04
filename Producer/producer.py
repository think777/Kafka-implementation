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

    '''
    Value entry from query string  

    args = request.args
    k = args.get("topic")
    k1 = args.get("data")

    '''

    x = requests.get('http://localhost:5000/bro')
    y = json.loads(x.text)
    global url
    url = y["url"]
    url = url + "/post"
    data = {
        "topic" : "third",
        "data" : "This is test1"
    }
    pos = requests.post(url,json=data)
    
    if (pos.status_code != 200):
        pos = requests.post(url,json=data)

    return str(pos.status_code)



















# Running app
def run(portd):
    app.run(host="0.0.0.0",port=portd,debug=False)
    