import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] =True
        self.app=app.test_client()

    def tearDown(self):
        pass

    def test_api_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_api_delete(self):
    response = self.app.delete('/framework/5b7931870718704008885f86')
    self.assertEqual(response.status_code, 200)

    if __name__=="__main__":
    unittest.main()