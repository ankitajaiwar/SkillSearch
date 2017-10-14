from common.database import Database


class CleanDatabase(object):
    # Clean
    @staticmethod
    def cleanDatabase():
        Database.initialize()
        print("Dropping test_collection. Errors = " + str(Database.dropCollection(collection_name="test_collection")))
        Database.removeEntry(collection_name="user_profiles", idName="uname", idValue="test_User1")
        print('cleaned..')


if __name__ == '__main__':
    CleanDatabase.cleanDatabase()