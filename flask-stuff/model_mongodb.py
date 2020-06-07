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

    def reload(self):
        if self._id:
            self.update(self.collection\
                    .find_one({"_id": ObjectId(self._id)}))
            self._id = str(self._id)

    def remove(self):
        if self._id:
            self.collection.remove({"_id": ObjectId(self._id)})
            self.clear()

class User(Model):
    db_client = pymongo.MongoClient('localhost', 27017)
    collection = db_client["users"]["users_list"]
    lists = db_client["users"]["lists"]
    items = db_client["users"]["items"]

    def add_user(self, user):
        return None
    def add_list(self, user, listo):
        return None
    def add_item(self, user, listo, item):
        return None
    

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
        print(users)
        return users
    def find_all_items(self, name, listId):
        users = list(self.items.find({"userID": name, "listId":listId}))
        for user in users:
            user["_id"] = str(user["_id"])
        print(users)
        return users
    def find_list(self, name, listNum):
        listo = []
        print(list(self.lists.find({"userID":name})))
        for li in (list(self.lists.find({"userID":name}))):
            listo.append(li["listId"])
        return listo
    def find_Item(self, user_id, listNum, itemId):
        items = list(self.items.find({"userID":user_id, "listId": listNum, "key":itemId}))
        print(items)
        for item in items:
            item["_id"] = str(item["_id"])
        return items
    def delete_user(self, user):
        return None
    def delete_list(self, user, listo):
        return None
    def delete_item(self, user, listo, item):
        return None
