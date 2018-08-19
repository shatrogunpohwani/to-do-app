from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo

app=Flask(__name__)

app.config['MONGO_DBNAME'] = 'axiom'
app.config['MONGO_URI'] = 'mongodb://testing:testing123@ds263161.mlab.com:63161/axiom'

mongo = PyMongo(app)

@app.route("/framework", methods = ['GET'])
def all_framework():
    framework = mongo.db.users

    output = []

    for i in framework.find():
        output.append({ 'name':i['name'],'language':i['language']})
    
    return jsonify({'results':output})

@app.route("/framework/<name>" , methods = ['GET'])
def one_framework(name):
    framework = mongo.db.users

    single = framework.find_one({'name':name})
    
    if single:
         output = {'name':single['name'],'language':single['language']} 
    else:
         output = 'no results found'         

    return jsonify({'results':output})

@app.route("/framework",methods = ['POST'])
def add():

    framework = mongo.db.users

    name = request.json['name']
    language=request.json['language']

    framework_id = framework.insert({'name':name,'language':language})
    new_framework=framework.find_one({'_id':framework_id})

    output = {'name':new_framework['name'],'language':new_framework['language']}

    return jsonify({'results':output})



app.run()