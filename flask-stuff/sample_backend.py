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
    'current_user':""
}


def make_id():
    nums = str(random.randint(100, 999))
    letters = ''.join(random.choice(string.ascii_lowercase) for c in range(3))
    return letters + nums
@app.route('/',methods=['POST'])
def sign_in():
    truth = request.get_json()
    search_username = truth.get('username')
    search_password = truth.get('password')
    if search_username and search_password:
        found = User().find_by_login(search_username, search_password)
        if (len(found) ==0):
            return {}, 204
        else:
            #//found.append({'code', 200})
            return jsonify(found), 200
    elif search_username:
        return  {}, 204
    else:
        return {}, 204 

@app.route('/signup',methods=['POST'])
def sign_up():
    #For registering
    truth = request.get_json()
    print(truth, type(truth))
    search_username = truth['username']
    search_password = truth['password']
    first_name = truth['first_name']
    last_name =  truth['last_name']
    print(search_username, search_password, first_name, last_name)
    if search_username and search_password:
        found = User().find_by_name(search_username)
        if (len(found) ==0):
            userToAdd = truth
            #userToAdd['id'] = generate_id()
            #users['users_list'].append(userToAdd)
            newUser = User(userToAdd)
            newUser.save()
            resp = jsonify(newUser), 200
            return resp
        else:
            return jsonify(found), 204
    elif search_username:
        return  {}, 204
    else:
        return {}, 204 
@app.route('/list/<user>',methods=['GET', 'POST'])
def create_list(user):
    #get = get the lists for the user
    #post = add a new empty list to user 
    if request.method == 'POST':
        listos = User().find_all_lists(user)
        if len(listos) == 0:
            newList = User({"listId": 0})
            newList.saveList()
            return jsonify(newList), 200
        else:
            print(listos)

    return {}, 204
@app.route('/list/<user>/<listNum>',methods=['POST', 'GET', 'DELETE'])
    #adding , getting, and deleting lists
    #get = get the list for the user
    #post = update list
    #delete = delete this list
def get_list(user, listNum):
    if request.method == 'GET':
        listos = User().find_list(user, listNum)
        if len(listos) == 0:
            return {}, 204
        else:
            return jsonify(listos[0]), 200
    elif request.method == 'POST':
        listos = User().find_all_lists(user)
        if listNum in listos:
            return {}, 204
        else:
            newList = User().add_list(user, listNum)
            return jsonify(newList), 200
    elif request.method == 'DELETE':
        listos = User().find_all_lists(user)
        if listNum in listos:
            remainingLists = User().delete_list(user, listNum)
            return remainingLists, 200
        else:
            return listos, 204
@app.route('/list/<user>/<listNum>/<itemId>',methods=['GET', 'POST', 'DELETE'])
def get_item(user, listNum):
    if request.method == 'GET':
        listos = User().find_list(user, listNum)
        if len(listos) == 0:
            return {}, 204
        else:
            itemos = User().find_item(user, listNum, itemId)
            if len(itemos) == 0:
                return {}, 204
            else:
                return jsonify(itemos[0]), 200
    elif request.method == 'DELETE':
        listos = User().find_all_lists(user)
        if listNum in listos:
            itemos = User().find_item(user, listNum, itemId)
            if len(itemos) == 0:
                newList = delete_item(user, listNum, itemId)
                newList.saveList()
                return jsonify(newList), 200
            else:
                return {}, 204
        else:
            return {}, 204
    elif request.method == 'POST':
        listos = User().find_all_lists(user)
        if listNum in listos:
            itemos = User().find_item(user, listNum, itemId)
            if len(itemos) == 0:
                return {}, 204
            else:
                newList = User().add_item(user, listo, item)
                newList.saveList()
                return jsonify(newList), 200
        else:
            return {}, 204


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
def find_user_by_username(username):
    subdict = {'users_list' : []}
    for user in users['users_list']:
        if user['name'] == name:
            subdict['users_list'].append(user)
    return subdict  
