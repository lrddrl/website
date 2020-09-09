from django.test import TestCase

from . import views

# Create your tests here.
class MyClassTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/index')
        self.assertEqual(response.status_code, 200)