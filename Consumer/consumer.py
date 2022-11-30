from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json

# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'




















# Running app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6000,debug=True)