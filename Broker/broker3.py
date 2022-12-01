from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json
import jsonpickle
import jsonlines
import os
#open("sample.json", "a+") as outfile

# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

user = ""
topic = ""

@app.route('/post', methods=['POST'])
def recieve():
    global topic
    if request.method == 'POST':
        #print (request.is_json)
        user = request.get_json()
        directory = user["topic"]
        parent_dir = "/home/college/Documents/Sem-5/BD/Team/yak/Broker"
        path = os.path.join(parent_dir, directory)
        d = "data recieved"

        try:
            os.mkdir(path)
            os.chdir(path)
            with jsonlines.open("sampledata.jsonl", "a") as writer:   # for writing
                writer.write(user) 
        except:
            os.chdir(path)
            #with open('sampledata.json', 'a+') as outfile:
            #json.dumps(user, outfile)
            with jsonlines.open("sampledata.jsonl", "a") as writer:   # for writing
                writer.write(user)  
            #   print (user)
            #user = request.form['topic']
            #return jsonpickle.encode(user)
        
        return jsonify(d)


@app.route('/req',methods=['GET'])
def post():
    args = request.args
    k = args.get("topic")
    directory = k
    parent_dir = "/home/college/Documents/Sem-5/BD/Team/yak/Broker"
    path = os.path.join(parent_dir, directory)
    ex = []

    try:
        os.chdir(path)
        with jsonlines.open('sampledata.jsonl') as reader:      # for reading
            for obj in reader:
                ex.append(obj)
        return jsonify(ex)
    except:
        return jsonify(k)
    


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
    app.run(host="0.0.0.0",port=5003,debug=True)