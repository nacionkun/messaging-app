import unittest

from app import app
from json import dumps

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_helloWorld(self):
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_addDataSources_badData_400(self):
        # arrange
        headers = [('Content-Type', 'application/json')]
        toInsert = {'message': 'Message with no sender.'}
        response = self.app.put(
            '/message', data=dumps(toInsert), headers=headers)

        self.assertEqual(response.status_code, 400)
