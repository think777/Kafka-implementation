from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json
import requests

# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

topic = ""

@app.route('/req')
def getbroker():
    args = request.args
    k = args.get("topic")
    x = requests.get('http://localhost:5000/bro')
    y = json.loads(x.text)
    global url
    url = y["url"]
    url = url + "/req?topic=" + k
    res = requests.get(url)
    return json.loads(res.text)

















# Running app
def run(portd):
    app.run(host="0.0.0.0",port=portd,debug=False)
    