from common.database import Database
from passlib.hash import sha256_crypt

class User(object):

    @staticmethod
    def validateUser(user_name,pwd):
        data = Database.find_one(collection="user_profiles",query={'uname':user_name})
        if data is not None:
            hash = data['password']
            print(hash)
        return sha256_crypt.verify(pwd, hash)

    @staticmethod
    def getName(username):
        firstName = 'NO-ONE-FOUND'
        data = Database.find_one(collection="user_profiles", query={'uname': username})
        if data is not None:
            firstName = data['fname']
        return firstName


