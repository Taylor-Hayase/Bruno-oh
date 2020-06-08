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
user_obj = ""
listCounter = 1

users = {
   'users_list':
   [], 
    'current_user':""
}


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
            global user_id
            user_id = found[0]['_id']
            # will need to fix to account for number of already created lists
            global listCounter 
            listCounter = 1
            global user_obj 
            user_obj = found
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
    search_username = truth['username']
    search_password = truth['password']
    first_name = truth['first_name']
    last_name = truth['last_name']
    if search_username and search_password:
        found = User().find_by_name(search_username)
        if (len(found) ==0):
            userToAdd = truth
            #userToAdd['id'] = generate_id()
            #users['users_list'].append(userToAdd)
            global user_id
            newUser = User(userToAdd)
            newUser.save()
            user_id = newUser["_id"]
            # will need to fix to account for number of already created lists
            global listCounter 
            listCounter = 1
            global user_obj 
            user_obj = newUser
            return  jsonify(list(newUser)), 200
        else:
            return jsonify(found), 204
    elif search_username:
        return  {}, 204
    else:
        return {}, 204 
@app.route('/list/',methods=['GET', 'POST'])
def create_list():
    #get = get the lists for the user
    #post = add a new empty list to user 
    global user_id
    global user_obj
    if request.method == 'POST':
        listo = request.get_json()
        #listos = User().find_all_lists(user_id)
        # could be elaborate here to deal with listcounter
        #global listCounter
        listo["userID"] = user_id
        newlist = User(listo)
        #listCounter += 1
        newlist.saveList()
        newlist["_id"] = str(newlist["_id"])
        return jsonify(list(newlist)), 200
    elif request.method == "GET":
        listos = User().find_all_lists(user_id)
        maxo = 0
        names = []
        for li in listos:
            names.append(li["lName"])
            maxo = max(maxo, li["idCount"])
        return jsonify({"lists": names, "numLists": len(listos), "idCount": maxo+1}), 200
    return {}, 204
@app.route('/list/<listId>/',methods=['GET', 'DELETE', 'PATCH'])
def del_list(listId):
    global user_id
    global user_obj
    if request.method == 'DELETE':
        User().delete_list(user_id, listId)
        return {}, 200
    #get this
    elif request.method == "GET":
        itemos = (User().find_all_items(user_id, listId))
        return jsonify(itemos), 200
    elif request.method == 'PATCH':
        newItems = request.get_json()
        listos = User().find_list(user_id, listId)
        if int(listId) in listos:
            for i in range(len(newItems)):
                myquery = {"key" : newItems[i]["key"]}
                newVals = {"$set" : {"checked" : newItems[i]["checked"]}}
                User().items.update_one(myquery, newVals)
            return {}, 200
    return {}, 204

@app.route('/list/<listNum>/<itemId>/',methods=['GET', 'POST', 'DELETE'])
def get_item(listNum, itemId):
    global user_id
    if request.method == 'GET':
        listos = User().find_list(user_id, listNum)
        if listNum not in listos:
            return {}, 204
        else:
            itemos = User().find_item(user_id, listNum, itemId)
            if len(itemos) != 0:
                return {}, 204
            else:
                return jsonify(itemos[0]), 200
    elif request.method == 'DELETE':
        #not correct
        listos = User().find_list(user_id, listNum)
        if int(listNum) in listos:
            itemos = User().find_Item(user_id, listNum, int(itemId))
            if len(itemos) == 1:
                newList = User().delete_item(user_id, listNum, int(itemId))
                return {}, 200
        else:
            return {}, 204
    elif request.method == 'POST':
        item = request.get_json()
        listos = User().find_list(user_id, listNum)
        if int(listNum) in listos:
            itemos = User().find_Item(user_id, listNum, itemId)
            if len(itemos) == 0:
                item["userID"] = user_id
                item["idCount"] = listNum
                newList = User(item)
                newList.saveItem()
                return jsonify(newList["key"]), 200
            else:
                return {}, 204
        else:
            return {}, 204
