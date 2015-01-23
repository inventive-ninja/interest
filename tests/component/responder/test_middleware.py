import unittest
from importlib import import_module
component = import_module('interest.responder.middleware')


class MiddlewareTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Middleware = self.make_mock_middleware_class()
        self.middleware = self.Middleware('service')

    # Helpers

    def make_mock_middleware_class(self):
        class MockMiddleware(component.Middleware):
            # Public
            pass
        return MockMiddleware

    # Tests

    def test_service(self):
        self.assertEqual(self.middleware.service, 'service')