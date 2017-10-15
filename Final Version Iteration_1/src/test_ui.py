from app import app
import unittest

class FrontEndTest(unittest.TestCase):

    """---------------------------------------tests for login.html---------------------------------------"""
    # checking if page loaded correctly
    # check by using content in the page
    def test_index_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type = 'html/text')
        self.assertTrue(b'SkillSearch: Find skilled people around your campus' in response.data)

    # ensuring correct loading of login page
    def test_login_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Not registered?' in response.data)

    # ensuring correct loading of register page
    def test_register_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type = 'html/text')
        self.assertTrue(b'Register' in response.data)
    """---------------------------------------tests for login.html---------------------------------------"""

    # ensuring login behaves correctly on valid credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_auth',
            data = dict(username = 'test_User1', pwd = 'test'),
            follow_redirects = True
        )
        self.assertIn(b'Log in Successful', response.data)

    # ensuring login behaves correctly on invalid credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_auth',
            data = dict(username = 'test_User1', pwd = 'test2'),
            follow_redirects = True
        )
        self.assertIn(b'Please Try Again', response.data)

    # ensuring logout behaves correctly
    def test_logout_page(self):
        tester = app.test_client(self)
        tester.post(
            '/login_auth',
            data = dict(username = 'test_User1', pwd = 'test2'),
            follow_redirects = True
        )
        response = tester.get('/logout', content_type = 'html/text')
        self.assertTrue(b'Log Out Successful' in response.data)

    """---------------------------------------tests for register.html---------------------------------------"""
    # ensuring the successful registration works correctly

    def test_correct_register_load(self):
        tester = app.test_client(self)

        response = tester.post(
            '/register_page',
            data = dict(
                FirstName = "Itachi",
                LastName = "Uchiha",
                Username = "iUchiha",
                email = "uchiha@konoha.com",
                pwd = "sasuke",
                ConfirmPassword = "sasuke",
                University = "Anbu",
                Department = "Elite"
            ),
            follow_redirects = True
        )
        self.assertIn(b'Registered Successfully!', response.data)


    # ensuring user homepage button works correctly
    def test_user_homepage_load(self):
        tester = app.test_client(self)
        response = tester.get('/userhome', content_type='html/text')
        self.assertTrue(b"User's Account" in response.data)

    # test_login_page, renamed the function
    def test_login_page_load1(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Not registered?' in response.data)

    """---------------------------------------tests for userhome.html---------------------------------------"""

    # ensuring addskills work correctly
    def test_addSkill_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/addskill', content_type='html/text')
        self.assertTrue(b"Add skill" in response.data)

    # ensuring searchpeople work correctly
    def test_searchpeople_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/searchpeople', content_type='html/text')
        self.assertTrue(b"Search people" in response.data)

    # checking logout page, renamed the function
    def test_logout_page1(self):
        tester = app.test_client(self)
        response = tester.get('/logout', content_type = 'html/text')
        self.assertTrue(b'Log Out Successful' in response.data)

    """---------------------------------------tests for addskill.html---------------------------------------"""

    # ensuring adding skills works correctly
    def test_incorrect_addingskill(self):
        tester = app.test_client(self)
        tester.post(
            '/login_auth',
            data = dict(username = 'test_User1', pwd = 'test'),
            follow_redirects = True
        )
        response = tester.post(
            '/skilladded',
            data = dict(skills = '', newSkill = ''),
            follow_redirects = True
        )
        self.assertIn(b'Failed to add skills', response.data)


    # ensuring skills are being added
    def test_correct_addingskill(self):
        tester = app.test_client(self)
        tester.post(
            '/login_auth',
            data = dict(username = 'test_User1', pwd = 'test'),
            follow_redirects = True
        )
        tester.get('/addskill', content_type='html/text')
        response = tester.post(
            '/skilladded',
            data = dict(skills = 'Android', newSkill = ''),
            follow_redirects = True
        )
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Skills Added', response.data)

    """---------------------------------------tests for search.html---------------------------------------"""

    # ensuring search results are being displayed
    def test_search_load_correctly(self):
        tester = app.test_client(self)
        response = tester.post(
            '/skilledpeople',
            data = dict(Skill = 'Art'),
            follow_redirects = True
        )
        self.assertIn(b'List of people with requested skill:', response.data)



if __name__ == '__main__':
    unittest.main()