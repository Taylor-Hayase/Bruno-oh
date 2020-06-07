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
            print(found)
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
            # will need to fix to account for number of already created lists
            global listCounter 
            listCounter = 1
            global user_obj 
            user_obj = newUser
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
    global user_obj
    if request.method == 'POST':
        listos = User().find_all_lists(user_id)
        print(user_id)
        # could be elaborate here to deal with listcounter
        global listCounter
        print(listCounter)
        newlist = User({"listId": listCounter, "userID": user_id})
        listCounter += 1
        newlist.saveList()
        print(newlist)
        return jsonify({"listId": listCounter, "userID": user_id}), 200
    elif request.method == "GET":
        listos = User().find_all_lists(user_id)
        print(listos)
        # need to actually get all the items here
        itemos = []
        for li in listos:
            itemos.extend(User().find_all_items(user_id, li["listId"]))
        return jsonify(itemos), 200
    return {}, 204
@app.route('/list/<listNum>/',methods=['PATCH'])
def update_list(listNum):
    if request.method == 'PATCH':
        newItems = request.get_json()
        listos = User().find_list(user_id, listNum)
        if int(listNum) in listos:
            newList = User({"listId": listNum, "userID": user_id})
            newList.saveList()
            User().delete_list(user_id, listNum)
            for i in range(len(newItems)):
                newItems[i]["user_id"] = user_id
                newItems[i]["listId"] = listNum
                newItem = User(newItems[i])
                newItem.saveItem()
            #newList = User(newItems)
            #newList._id = oldList._id
            #newList.saveList()
            return {}, 200
        else:
            return {}, 204
@app.route('/list/<listNum>/<itemId>/',methods=['GET', 'POST', 'DELETE'])
def get_item(listNum, itemId):
    print(listNum)
    if request.method == 'GET':
        listos = User().find_items(user_id, listNum, itemId)
        if len(listos) == 0:
            return {}, 204
        else:
            itemos = User().find_item(useri_id, listNum, itemId)
            if len(itemos) == 0:
                return {}, 204
            else:
                return jsonify(itemos[0]), 200
    elif request.method == 'DELETE':
        #not correct
        itemKey = request.get_json()
        print (itemKey)
        listos = User().find_all_lists(user_id)
        if int(listNum) in listos:
            itemos = User().find_item(user_id, listNum, itemId)
            if len(itemos) == 0:
                newList = delete_item(user_id, listNum, itemId)
                newList.saveList()
                return jsonify(newList), 200
            else:
                return {}, 204
        else:
            return {}, 204
    elif request.method == 'POST':
        item = request.get_json()
        listos = User().find_list(user_id, listNum)
        print(listos)
        if int(listNum) in listos:
            itemos = User().find_Item(user_id, listNum, itemId)
            print("item", itemos)
            if len(itemos) == 0:
                print("here")
                item["user_id"] = user_id
                item["listId"] = listNum
                print("item", item)
                newList = User(item)
                newList.saveItem()
                return {}, 200
            else:
                return {}, 204
        else:
            return {}, 204
