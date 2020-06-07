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
            #print(found)
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
    #print(truth, type(truth))
    search_username = truth['username']
    search_password = truth['password']
    first_name = truth['first_name']
    last_name =  truth['last_name']
    #print(search_username, search_password, first_name, last_name)
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
        print(listo)
        #listos = User().find_all_lists(user_id)
        #print(user_id)
        # could be elaborate here to deal with listcounter
        #global listCounter
        #print(listCounter)
        listo["userID"] = user_id
        newlist = User(listo)
        #listCounter += 1
        newlist.saveList()
        #print(newlist)
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
@app.route('/list/<listId>/',methods=['GET', 'DELETE'])
def del_list(listId):
    #get = get the lists for the user
    #post = add a new empty list to user 
    global user_id
    global user_obj
    if request.method == 'DELETE':
        return {}, 204
    elif request.method == "GET":
        itemos = (User().find_all_items(user_id, int(listId)))
        #print(itemos)
        return jsonify(itemos), 200
    return {}, 204
@app.route('/list/<listNum>/<itemId>/',methods=['GET', 'POST', 'DELETE', 'PATCH'])
def get_item(listNum, itemId):
    print(listNum)
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
            print("here")
            itemos = User().find_Item(user_id, listNum, int(itemId))
            #print(itemos)
            if len(itemos) == 1:
                print("here2")
                newList = User().delete_item(user_id, listNum, itemId)
                return {}, 200
            else:
                return {}, 204
        else:
            return {}, 204
    elif request.method == "PATCH":
        return {}, 204
    elif request.method == 'POST':
        item = request.get_json()
        listos = User().find_list(user_id, listNum)
        #print(listos)
        if int(listNum) in listos:
            itemos = User().find_Item(user_id, listNum, itemId)
            #print("item", itemos)
            if len(itemos) == 0:
                #print("here")
                item["userID"] = user_id
                item["idCount"] = listNum
                #print("item", item)
                newList = User(item)
                newList.saveItem()
                return jsonify(newList["key"]), 200
            else:
                return {}, 204
        else:
            return {}, 204
