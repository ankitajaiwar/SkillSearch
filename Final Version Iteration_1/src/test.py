import unittest
from time import sleep
from passlib.handlers.sha2_crypt import sha256_crypt
from common.database import Database
from find_people import Find_People
from user import User

class TestApp(unittest.TestCase):

    def test_databaseInsert(self):
        Database.initialize()
        pwd = sha256_crypt.encrypt("test")
        Database.insert(collection="user_profiles", data={"fname": "Test_User_Name1",
                                                          "uname": "test_User1",
                                                          "password": pwd})
        Database.insert(collection="test_collection", data={"name": "vignesh", "age": "26"})
        test_data=Database.find_one(collection="test_collection",query={"name":"vignesh"})
        self.assertEqual(test_data['age'],'26')

    def test_databasefind(self):
        Database.initialize()
        test_data = Database.find_one(collection="test_collection", query={"age": "26"})
        self.assertEqual(test_data['name'], 'vignesh')

    def test_validateUser(self):
        status = 'not ok'
        if User.validateUser(user_name='test_User1', pwd='test'):
            status='ok'
        self.assertEqual(status,'ok')

    def test_getName(self):
        fName = User.getName(username="test_User1")
        self.assertEqual(fName,"Test_User_Name1")


    def test_findPeople(self):
        testName = None
        Database.insert(collection="skillset", data={"Name": "testuser", "skill": "test_Java"})
        print('hi2')
        results = Find_People.search_from_mongo(skill="test_Java")
        for r in results:
            testName = r['Name']
        self.assertEqual(testName,'testuser')

    if '__name__' == '__main__':
        unittest.main()