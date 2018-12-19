from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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

@app.route("/framework/<id>",methods = ['PUT'])
def update(id):

    framework = mongo.db.users

    frameworks = framework.find_one({"_id": ObjectId(id)})  

    frameworks['language']=request.json['language']
    #if frameworks:
    framework.save(frameworks)
    return "updated"

    #frameworks=[identity for identity in framework if identity['name']==name]
    #frameworks[0]['name']=request.json['name']
    #return jsonify({'results':frameworks[0]})#

@app.route("/framework/<id>",methods = ['DELETE'])
def remove(id):
    framework = mongo.db.users

    frameworks = framework.find_one({"_id":ObjectId(id)})
    fworks=framework.remove(frameworks)
    if fworks:
        return "deleted"
    else :
        return "no id found"    


app.run(debug = True )
