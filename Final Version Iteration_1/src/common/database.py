import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def dropCollection(collection_name):
        return Database.DATABASE[collection_name].drop()

    @staticmethod
    def removeEntry(collection_name,idName,idValue):
        Database.DATABASE[collection_name].remove({idName:idValue})

    @staticmethod
    def list_values(collection, key):
        return Database.DATABASE[collection].find().distinct(key)

