import json
from django.test import TestCase

# Create your tests here.
class EchoViewTestCase(TestCase):
    def test_echo_basic_call(self):
        response = self.client.get('/api/v1/echo?msg=hello-world')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['msg'], 'hello-world')
    
    def test_echo_missing_msg(self):
        response = self.client.get('/api/v1/echo')
        self.assertEqual(response.status_code, 400)
        content = json.loads(response.content)
        self.assertTrue('error' in content)
