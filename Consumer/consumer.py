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
    url = url + "/req"
    res = requests.get(url)
    return json.loads(res.text)

















# Running app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4500,debug=True)