import unittest
import simplejson as json

from sample_backend import app

class FlaskTests(unittest.TestCase):

	def test_root(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.data, b'Hello, World!');

	def test_sign_in(self):
		tester = app.test_client(self)
		response = tester.post('/', data=json.dumps(dict(username='AlexT',
														password='1234')),
							content_type='application/json')
		self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
	unittest.main()
