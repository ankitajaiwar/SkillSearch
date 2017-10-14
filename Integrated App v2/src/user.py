from common.database import Database
from passlib.hash import sha256_crypt

class User(object):
    def __init__(self, username, pwd):
        user_name = username
        password = pwd

    def validateUser(self, user_name,pwd):
        data = Database.find_one(collection="user_profiles",query={'uname':user_name})
        if data is not None:
            hash = data['password']
            print(hash)
        return sha256_crypt.verify(pwd, hash)

    @staticmethod
    def getName(username):
        data = Database.find_one(collection="user_profiles", query={'uname': username})
        if data is not None:
            firstName = data['fname']
        return firstName


