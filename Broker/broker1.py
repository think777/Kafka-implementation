from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json
import jsonpickle

# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

user = ""

@app.route('/post', methods=['POST'])
def recieve():
    if request.method == 'POST':
        #print (request.is_json)
        user = request.get_json()
        d = "data recieved"
        #print (user)
        #user = request.form['topic']
        #return jsonpickle.encode(user)
        return jsonify(d)

@app.route('/list')
def listing():
    return user













# Running app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)