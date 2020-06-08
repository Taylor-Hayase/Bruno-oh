import pymongo
from bson import ObjectId

class Model(dict):
    """
    A simple model that wraps mongodb document
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def save(self):
        if not self._id:
            self.collection.insert(self)
        else:
            self.collection.update(
                { "_id": ObjectId(self._id) }, self)
        self._id = str(self._id)
    def saveList(self):
        if not self._id:
            self.lists.insert(self)
        else:
            self.lists.update(
                { "_id": ObjectId(self._id) }, self)
        self._id = str(self._id)
    def saveItem(self):
        if not self._id:
            self.items.insert(self)
        else:
            self.items.update(
                { "_id": ObjectId(self._id) }, self)
        self._id = str(self._id)
    '''
    def reload(self):
        if self._id:
            self.update(self.collection\
                    .find_one({"_id": ObjectId(self._id)}))
            self._id = str(self._id)
    def reloadItem(self):
        if self._id:
            self.update(self.items\
                    .find_one({"_id": ObjectId(self._id)}))
            self._id = str(self._id)
    '''
    def remove(self):
        if self._id:
            self.collection.remove({"_id": ObjectId(self._id)})
            self.clear()

class User(Model):
    db_client = pymongo.MongoClient('mongodb+srv://tayhay:thayase@cluster0-sxjlm.mongodb.net/Project0?retryWrites=true&w=majority', 27017)
    collection = db_client["users"]["users_list"]
    lists = db_client["users"]["lists"]
    items = db_client["users"]["items"]

    def find_all(self):
        users = list(self.collection.find())
        for user in users:
            user["_id"] = str(user["_id"])
        return users

    def find_by_name(self, name):
        users = list(self.collection.find({"username": name}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
    def find_by_login(self, name, password):
        users = list(self.collection.find({"username": name, "password":password}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
    def find_all_lists(self, name):
        users = list(self.lists.find({"userID": name}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
    def find_all_items(self, name, listId):
        users = list(self.items.find({"userID": name, "idCount":listId}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
    def find_list(self, name, listNum):
        listo = []
        for li in (list(self.lists.find({"userID":name}))):
            listo.append(li["idCount"])
        return listo
    def find_Item(self, user_id, listNum, itemId):
        Items = list(self.items.find({"key":itemId}))
        for Item in Items:
            Item["_id"] = str(Item["_id"])
        return Items
    def delete_list(self, name, listId):
        items = list(self.items.find({"userID": name, "idCount":listId}))
        for li in items:
            self.items.delete_one({"userID":name,"idCount":listId, "key":li["_id"]})
        self.lists.delete_one({"userID": name, "idCount":int(listId)}) 
    def delete_item(self, userId, listId, itemId):
        return self.items.delete_one({"userID":userId, "idCount":listId, "key":itemId})
