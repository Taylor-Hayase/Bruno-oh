import unittest
import simplejson as json
import names

from sample_backend import app

class FlaskTests(unittest.TestCase):

        #just testing the root get
        def test_root(self):
            tester = app.test_client(self)
            response = tester.get('/', content_type='html/text')
            self.assertEqual(response.data, b'Hello, World!');

        #tests for signing in
        def test_sign_in_not_user(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/', data=json.dumps(dict(username='AlexT', password='1234')), content_type='application/json')
            self.assertEqual(response.status_code, 204)

        def test_sign_in_no_password(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/', data=json.dumps(dict(username='AlexT')), content_type='application/json')
            self.assertEqual(response.status_code, 204)

        def test_sign_in_blank(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/', data=json.dumps(dict()), content_type='application/json')
            self.assertEqual(response.status_code, 204)

        '''
        def test_sign_in_good(self):
            app.testing = True
            tester = app.test_client(self)
            name_to_save = names.get_first_name() 
            tester.post('/signup', data=json.dumps(dict(username=name_to_save, password='1234', first_name='Bruno', last_name='Da Silva')))
            response = tester.post('/', data=json.dumps(dict(username=name_to_save, password='1234')), content_type='application/json')
            self.assertEqual(response.status_code, 204)
        '''
        #tests for signing up
        def test_signup_no_username(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/signup', data=json.dumps(dict(username='', password='123', first_name='Bruno', last_name='Da Silva')), content_type='application/json')
            self.assertEqual(response.status_code, 204)

        def test_signup_no_password(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/signup', data=json.dumps(dict(username='Brand', password='', first_name='Bruno', last_name='Da Silva')), content_type='application/json')
            self.assertEqual(response.status_code, 204)

        def test_signup_blank(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/signup', data=json.dumps(dict(username='',
															password='',
															first_name='Bruno',
															last_name='Da Silva')),
							content_type='application/json')
            self.assertEqual(response.status_code, 204)

        def test_signup_good(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/signup', data=json.dumps(dict(username=names.get_first_name(),
															password='1234',
															first_name='Bruno',
															last_name='Da Silva')),
							content_type='application/json')
            self.assertEqual(response.status_code, 200)
        def test_signup_existing(self):
            app.testing = True
            tester = app.test_client(self)
            name_to_save = names.get_first_name()
            tester.post('/signup', data=json.dumps(dict(username=name_to_save,
															password='1234',
															first_name='Bruno',
															last_name='Da Silva')),
							content_type='application/json')
            response = tester.post('/signup', data=json.dumps(dict(username=name_to_save,
															password='1234',
															first_name='Bruno',
															last_name='Da Silva')),
							content_type='application/json')
            self.assertEqual(response.status_code, 204)

	#testing list/
        def test_list_get(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.get('/list/', content_type='html/text')
            self.assertEqual(response.status_code, 200)

        def test_list_post(self):
            app.testing = True
            tester = app.test_client(self)
            response = tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            self.assertEqual(response.status_code, 200)

	#testing list/<listID>
        def test_list_get(self):
            app.testing = True
            tester = app.test_client(self)
            tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            response = tester.get('/list/1/', content_type='html/text')
            self.assertEqual(response.status_code, 200)

        def test_list_del(self):
            app.testing = True
            tester = app.test_client(self)
            tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            response = tester.delete('/list/1/', content_type='application/json')
            self.assertEqual(response.status_code, 200)

        def test_list_patch(self):
            app.testing = True
            tester = app.test_client(self)
            tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            listo = tester.get('/list/1/', content_type='application/json')
            response = tester.patch('/list/1/', data=listo.data, content_type='application/json')
            self.assertEqual(response.status_code, 200)

        #testing /list/<listNum>/<itemId>/
        def test_item_post_new_item(self):
            app.testing = True
            tester = app.test_client(self)
            tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            response = tester.post('/list/1/1/', data=json.dumps(dict(idCount=1,text='finish this', key='',checked=False, due = '')), content_type='application/json')
            self.assertEqual(response.status_code, 200)
	
        def test_item_get_item_exists(self):
            app.testing = True
            tester = app.test_client(self)
            tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            tester.post('/list/1/1/', data=json.dumps(dict(idCount=1,text='finish this', key='1',checked=False, due = '')), content_type='application/json')
            response = tester.get('/list/1/1/', content_type='html/text')
            self.assertEqual(response.status_code, 204)
        
        def test_item_get_item_dne(self):
            app.testing = True
            tester = app.test_client(self)
            tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            response = tester.get('/list/1/1/', content_type='html/text')
            self.assertEqual(response.status_code, 204)
       
        def test_item_delete_item_exists(self):
            app.testing = True
            tester = app.test_client(self)
            tester.post('/list/', data=json.dumps(dict(idCount=1, lName='List 1')),
							 content_type='application/json')
            response = tester.delete('/list/1/1/', content_type='application/json')
            self.assertEqual(response.status_code, 200)
       
if __name__ == '__main__':
    unittest.main()
