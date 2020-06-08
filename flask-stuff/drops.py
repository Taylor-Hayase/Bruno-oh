import pymongo
db_client = pymongo.MongoClient('mongodb+srv://msblue:Brunos_hos@cluster0-sxjlm.mongodb.net/Project0?retryWrites=true&w=majority', 27017)
collection = db_client["users"]["users_list"]
lists = db_client["users"]["lists"]
items = db_client["users"]["items"]
collection.drop()
items.drop()
lists.drop()
