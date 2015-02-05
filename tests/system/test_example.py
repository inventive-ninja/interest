import unittest
from pathlib import Path
from interest import Tester


class ExampleTest(unittest.TestCase):

    # Actions

    @classmethod
    def setUpClass(cls):
        current = Path(__file__).parent
        basedir = current / '..' / '..'
        factory = basedir / 'demo' / 'example.py'
        cls.tester = Tester(str(factory),
            environ={'PYTHONPATH': str(basedir)})
        cls.tester.start()

    @classmethod
    def tearDownClass(cls):
        cls.tester.stop()

    # Tests

    def test_read(self):
        response = self.tester.request('GET', '/api/v1/comment/7')
        self.assertEqual(response.status, 200)
        self.assertEqual(
            response.headers['CONTENT-TYPE'],
            'application/json; charset=utf-8')
        self.assertEqual(response.json, {'key': 7})

    def test_upsert(self):
        response = self.tester.request('PUT', '/api/v1/comment')
        self.assertEqual(response.status, 201)
        self.assertEqual(response.json, {'message': 'Created'})

    def test_not_found(self):
        response = self.tester.request('PUT', '/api/v1/not-found')
        self.assertEqual(response.status, 404)
