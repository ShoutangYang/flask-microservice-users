import json
from project.tests.base import BaseTestCase
from project import db 
from project.api.models import User

class TestUserService(BaseTestCase):
    def test_users(self):
        """确保ping的服务正常."""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])
    
    def test_add_user(self):

        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(username ='cynch',email='to_tsy@163.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,201)
            self.assertIn('to_tsy@163.com was added',data['message'])
            self.assertIn('success',data['status'])
    
    def test_add_user_invalid_json(self):
        """
        确保传入空值，能抛出错误。
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,400)
            self.assertIn('Invaild payload',data['message'])
            self.assertIn('fail',data['status'])
    
    def test_add_user_invalid_json_keys(self):
        """
        json 中只有一个值 username/email。
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(email='to_tsy@163.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,400)
            self.assertIn('Invaild payload',data['message'])
            self.assertIn('fail',data['status'])

        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(username='to_tsy')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,400)
            self.assertIn('Invaild payload',data['message'])
            self.assertIn('fail',data['status'])

    def test_add_user_duplicate_user(self):
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps(dict(username='to_yst',email='to_yst@163.com')),
                content_type='application/json',
            )
            response= self.client.post(
                '/users',
                data=json.dumps(dict(username='to_yst',email='to_yst@163.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,400)
            self.assertIn('Sorry, That email already exists.',data['message'])
            self.assertIn('fail',data['status'])
    
    def test_get_user(self):
        user = User(username='to_tsy',email='to_tsy@163.com')
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = self.client.get('/users/%d'%user.id)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,200)
            self.assertTrue('created_at' in data['data'])
            self.assertEqual('to_tsy',data['data']['username'])
            self.assertEqual('to_tsy@163.com',data['data']['email'])
            self.assertEqual('success',data['status'])

    def test_get_user_no_id(self):
        with self.client:
            response = self.client.get('/users/xxx')
            data = json.loads(response.data.decode())
            print('code  --->>>',response.status_code)
            self.assertEqual(response.status_code,400)
            self.assertIn('Param id error' ,data['message'])
            self.assertEqual('fail',data['status'])
    
    def test_get_user_incorrent_id(self):
        with self.client:
            response = self.client.get('/users/-1')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,404)
            self.assertIn('User does not exist' ,data['message'])
            self.assertEqual('fail',data['status'])
