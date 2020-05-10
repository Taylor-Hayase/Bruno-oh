import random
import string

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def make_id():
	nums = str(random.randint(100, 999))
	letters = ''.join(random.choice(string.ascii_lowercase) for c in range(3))
	return letters + nums


@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
   	search_username = request.args.get('name')
   	search_job = request.args.get('job')
   	if (search_username != None) & (search_job != None):
   		subdict = {'users_list' : []}
   		for user in users['users_list']:
   			if (user['name'] == search_username) & (user['job'] == search_job):
   				subdict['users_list'].append(user)
   		return subdict
   	elif search_username :
   		subdict = {'users_list' : []}
   		for user in users['users_list']:
   			if user['name'] == search_username:
   				subdict['users_list'].append(user)
   		return subdict
   	return users
   elif request.method == 'POST':
   	userToAdd = request.get_json()
   	userToAdd["id"] = make_id()
   	users['users_list'].append(userToAdd)
   	resp = jsonify(userToAdd)
   	if userToAdd in users['users_list']:
   		resp.status_code = 201
   	else:
   		resp.status_code = 400
   	return resp



@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   elif request.method == 'DELETE':
   	for user in users['users_list']:
   		if user['id'] == id:
   			users['users_list'].remove(user)
   			resp = jsonify(success=True)
   			resp.status_code = 200
   			return resp
   	resp = jsonify(success=False)
   	resp.status_code = 400
   	return resp	
   return users
