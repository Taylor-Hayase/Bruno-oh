import pymongo
db_client = pymongo.MongoClient('localhost', 27017)
collection = db_client["users"]["users_list"]
lists = db_client["users"]["lists"]
items = db_client["users"]["items"]
items.drop()
lists.drop()
