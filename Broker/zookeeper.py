from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json
import requests
import threading

# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

# import the time module
import time

url = "j"
b1 = 0
b2 = 0
b3 = 0

# define the countdown func.
def countdown():
    global url,b1,b2,b3
   

    try:
        x = requests.get('http://localhost:5001/pool')
        if x.status_code == 200:
            
            b1 = 1
    except:
        #x = requests.get('http://localhost:5001/pool')
        b1 = 0
    try:    
        y = requests.get('http://localhost:5002/pool')
        if y.status_code == 200:
        
            b2 = 1
    except:
        #y = requests.get('http://localhost:5002/pool')
        b2 = 0
    try:
        z = requests.get('http://localhost:5003/pool')
        if z.status_code == 200:
            
            b3 = 1
    except:
        #z = requests.get('http://localhost:5003/pool')
        b3=0;

    if b1 == 1:
        url = "http://localhost:5001"
            
    elif b2 == 1:
        url = "http://localhost:5002"

    elif b3 == 1:
        url = "http://localhost:5003"

        




# Route for seeing a data
@app.route('/bro', methods=['GET'])
def broker():
    global url
    countdown()
    data = {
        "url" : url
    }
    return jsonify (data)



















# Running app
if __name__ == '__main__':
    #key = threading.Thread(target=countdown, args=(30,))
	# starting thread 1
    #key.start()
    app.run(host="0.0.0.0",port=5000,debug=True)