from app import app
import unittest

class TestCase(unittest.TestCase):
    def test_index(self):

        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()




