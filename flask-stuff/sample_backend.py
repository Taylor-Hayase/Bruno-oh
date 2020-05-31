import random
import string
from model_mongodb import User

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
'''
python3 -m venv venv;
export FLASK_APP=sample_backend.py;
export FLASK_ENV=development;
flask run;
'''

@app.route('/')
def hello_world():
    return 'Hello, World!'


users = {
   'users_list':
   [], 
}


def make_id():
    nums = str(random.randint(100, 999))
    letters = ''.join(random.choice(string.ascii_lowercase) for c in range(3))
    return letters + nums
@app.route('/',methods=['post'])
def sign_in():
    search_username = request.args.get('name')
    search_password = request.args.get('pass')
    # will also get first and lastname
    #will need a has access variable

    if search_username and search_password:
        return 
    else if search_username:
        return 
    else:
        return 
@app.route('/list/<listId>', methods=['GET', 'POST', 'PATCH'])
def get_users(listId):
   if request.method == 'GET':
    return users;
   elif request.method == 'POST':
   	userToAdd = request.get_json()
   	users['users_list'].append(userToAdd)
   	resp = jsonify(userToAdd)
   	if userToAdd in users['users_list']:
   		resp.status_code = 201
   	else:
   		resp.status_code = 400
   	return resp
   elif request.method == 'PATCH':
    newListOrder = request.get_json()
    users['users_list'] = newListOrder
    resp = jsonify(newListOrder)
    if users['users_list'] == newListOrder:
      resp.status_code = 200
    else:
      resp.status_code = 400
    return resp

@app.route('/list/1/<key>', methods=['GET', 'DELETE'])
def get_user(key):
   if request.method == 'GET':
      for user in users['users_list']:
        if user['key'] == key:
           return user
      return ({})
   elif request.method == 'DELETE':
   	for user in users['users_list']:
   		if user['key'] == (int(key)):
   			users['users_list'].remove(user)
   			resp = jsonify(success=True)
   			resp.status_code = 200
   			return resp
   	resp = jsonify(success=False)
   	resp.status_code = 400
   	return resp	
   return users
