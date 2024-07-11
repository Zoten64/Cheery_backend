from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Like

# Create your tests here.

class LikeTests(APITestCase):
    def setUp(self):
        '''
        Creates a user and a post. The user can like their own post
        so there is no need to add a second user.
        '''
        user1 = User.objects.create_user(username='testuser1',
                                         password='password')
        self.client.force_authenticate(user=user1) 
        Post.objects.create(title='test post 1',
                            content='test content 1',
                            owner=user1)
        
    def test_create_like(self):
        '''
        Test if a like can be created.
        '''
        Post.objects.get(title='test post 1')
        response = self.client.post('/likes/', {'post': 1})
        self.assertEqual(response.status_code, 201)

    def test_cant_like_twice(self):
        '''
        Test if a user can like the same post twice.
        '''
        Post.objects.get(title='test post 1')
        #First like
        self.client.post('/likes/', {'post': 1})
        #Second like
        response = self.client.post('/likes/', {'post': 1})
        self.assertEqual(response.status_code, 400)

    def test_delete_like(self):
        '''
        Test if a like can be deleted.
        '''
        Post.objects.get(title='test post 1')
        self.client.post('/likes/', {'post': 1})
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, 204)