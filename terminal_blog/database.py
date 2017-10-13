import pymongo
class Database(object):

# This is a static class (static variables & methods). we are not planning to create objects for this class. Because,
# we want the database information to be same across the application. If we create objects, each obj can have different
# values.

#This is a static variable. This can be accessed elsewhere using the class name
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

#This is to say python we are not using the self object. its a static method.
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, data):
        return Database.DATABASE[collection].find(data)   #this find() fn return the cursor object

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)   #find_one() gives the 1st object

