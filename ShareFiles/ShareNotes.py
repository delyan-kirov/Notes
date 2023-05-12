from flask_cors import CORS
from flask import Flask, jsonify, request, render_template
import os
import json

app = Flask(__name__)
app.debug = True
CORS(app)

#%% Root route
@app.route("/")

def shareData():
    dataPath = "./data"
    output = []
    showData = ""
    for files in os.listdir(dataPath):
        files = os.path.join(dataPath, files)
        with open(files, 'r') as f:
            output.append(f.read(60))
            f.close()
    
    for data in output:
        showData += data + "\n"
    
    filename = request.args.get("filename")
    print(filename)
    
    print(output)
    return jsonify(showData)

#%% Share data route
@app.route("/init")

def giveFileData():
    dataPath = "./data"
    output = []
    names = []
    
    for files in os.listdir(dataPath):
        files = os.path.join(dataPath, files)
        with open(files, 'r') as f:
            output.append(f.read(60))
            names.append(str(os.path.basename(f.name)))
            f.close()
    print("\n")
    print(output,names)
    print("inside /init")
    return(jsonify(output,names))

#%%
@app.route("/notes", methods=["GET", "POST"])

def showNote():
    print(request.data)
    return (render_template("new.html"))

#%%
@app.route("/text", methods=["GET", "POST"])

def getText():
    data = request.get_json()
    print("Received message")
    print(json.dumps(data))
    
    data = json.dumps(data)
    dataPath = "./data"
    name = data[:20]
    path = os.path.join(dataPath, name + ".txt")
    
    with open(path,"w") as f:
        f.write(data)
        f.close()   

    return jsonify({'status': 'success'})

#%%
@app.route("/delete", methods=["DELETE", "GET"])

def deleteFile():
    print("received signal")
    
    filename = request.args.get("filename")
    print(filename)
    
    file_path = "./data/" + filename
    os.remove(file_path)
    return jsonify({'status': 'success'})
    