
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:28:50 2019

@author: Kshitiz Regmi
"""
from flask import Flask ,jsonify , request 

from flask_restful import Api ,Resource

app = Flask(__name__)
api = Api(app)

##define function to check status code to cheeck parameter errors

def status_code(data,url):
    if url == 'add'or url == 'sub' or url== 'mul' or url == 'div':
        if 'x' not in data or 'y' not in data:
            return 301
        else :
            return 200
    
#define resources
class Add(Resource):
    def post(self):
        #get posted data 
        data = request.get_json()
        ########################
        #check status code 
        ################## 'add' is url location
        code = status_code(data , 'add')
        print("\ncode=",code)
        if code == 200:
        
            #get vallus of x and y 
            x = data['x']
            y= data['y']
            x = int(x)
            y = int(y)
            #add posted data 
            z = x+y
            ###json of result 
            out= {'message':z , 'status':'OK'}
            #return value computed 
        if code != 200:
            out = {'message':"input error"}
            
        return jsonify(out)

class Sub (Resource):
    def post(self):
        #get posted data 
        data = request.get_json()
        ########################
        #check status code 
        ################## 'sub' is url location
        code = status_code(data , 'sub')
        print("\ncode=",code)
        if code == 200:
        
            #get vallus of x and y 
            x = data['x']
            y= data['y']
            x = int(x)
            y = int(y)
            
            #sub posted data 
            z = x-y
            ###json of result 
            out= {'message':z , 'status':'OK'}
            #return value computed 
        else:
            out = {'message': "input error" }
            
        return jsonify(out)

class Mul (Resource):
    def post(self):
        #get posted data 
        data = request.get_json()
        
        ########################
        #check status code 
        ################## 'Mul' is url location
        code = status_code(data , 'mul')
        print("\ncode=",code)
        if code == 200:
        
            #get vallus of x and y 
            x = data['x']
            y= data['y']
            x = int(x)
            y = int(y)
            
            #multipkly posted data 
            z = x*y
            ###json of result 
            out= {'message':z , 'status':'OK'}
            #return value computed 
        else:
            out = {'message': "input error" }
            
        return jsonify(out)

class Div (Resource):
    def post(self):
        #get posted data 
        data = request.get_json()
        
        ########################
        #check status code 
        ################## 'div' is url location
        code = status_code(data , 'div')
        print("\ncode=",code)
        if code == 200:
        
            #get vallus of x and y 
            x = data['x']
            y= data['y']
            x = int(x)
            y = int(y)
            
            #divide posted data 
            z = float(x/y)
            ###json of result 
            out= {'message':z , 'status':'OK'}
            #return value computed 
        else:
            out = {'message': "input error" }
            
        return jsonify(out)

##add resources in api
    
####
    # add_resource(resource_class_name , url_location)

api.add_resource(Add , '/add')

api.add_resource(Sub , '/sub')

api.add_resource(Mul , '/mul')

api.add_resource(Div , '/div')

if __name__ == "__main__":
    app.run()
