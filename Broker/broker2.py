from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json
import jsonpickle

#open("sample.json", "a+") as outfile

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
        with open('sampledata.json', 'a+') as outfile:
            json.dumps(user, outfile)
        #print (user)
        #user = request.form['topic']
        #return jsonpickle.encode(user)
        return jsonify(d)


@app.route('/req',methods=['GET'])
def post():
    with open('sampledata.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)


@app.route('/list')
def listing():
    with open('sampledata.json') as json_file:
        data = json.load(json_file)
    return data

@app.route('/pool',methods=['GET'])
def pool():
    d = "im alive"
    return jsonify(d)











# Running app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002,debug=True)