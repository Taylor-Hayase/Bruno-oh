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

user_id = ""
listCounter = 0

users = {
   'users_list':
   [], 
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
            print(found)
            global user_id
            user_id = found[0]['_id']
            global listCounter 
            listCounter = 0
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
            global user_id
            user_id = userToAdd['id']
            newUser = User(userToAdd)
            newUser.save()
            global listCounter 
            listCounter = 0
            resp = jsonify(newUser), 200
            return resp
        else:
            return jsonify(found), 204
    elif search_username:
        return  {}, 204
    else:
        return {}, 204 
@app.route('/list/',methods=['GET', 'POST'])
def create_list():
    user_i = request.get_json()
    print(user_i)
    #get = get the lists for the user
    #post = add a new empty list to user 
    global user_id
    if request.method == 'POST':
        listos = User().find_all_lists(user_id)
        print(user_id)
        if len(listos) == 0:
            global listCounter
            newList = User({"listId": listCounter})
            listCounter += 1
            newList.saveList()
            return jsonify(newList), 200
        else:
            print(listos)
    elif request.method == "GET":
        listos = User().find_all_lists(user_id)
        # need to actually get all the items here
        return jsonify(listos), 200
    return {}, 204
@app.route('/list/<user>/<listNum>',methods=['POST', 'GET', 'DELETE'])
    #adding , getting, and deleting lists
    #get = get the list for the user
    #post = update list
    #delete = delete this list
def get_list(user, listNum):
    return None
@app.route('/list/<user>/<listNum>/<itemId>',methods=['GET', 'POST', 'DELETE'])
    #do we want an update?
    #get = get the item for the user
    #post = update item
    #delete = delete this item
def get_item(user, listNum):
    return None



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
