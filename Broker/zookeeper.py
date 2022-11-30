from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json

# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'


# Route for seeing a data
@app.route('/bro', methods=['GET'])
def broker():
    data = {
        "url" : "http://localhost:5001"
    }
    return jsonify (data)



















# Running app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)