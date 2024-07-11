from rest_framework.test import APITestCase
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.
class PostTestCase(APITestCase):
    def setUp(self):
        '''creates 2 users with a post each'''
        user = User.objects.create_user(
            username='testuser', password='pass')
        self.client.force_authenticate(user=user)

        user2 = User.objects.create_user(
            username='testuser2', password='pass')
        
        Post.objects.create(
            title='Test Post',
            content='This is a test post',
            owner=user
        )

        Post.objects.create(
            title='Test Post 2',
            content='This is a test post',
            owner=user2
        )
    def test_post_list(self):
        '''Tests if the post list view is accessible'''
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_can_retrieve_post(self):
        '''Tests if a post can be retrieved by id'''
        response = self.client.get('/posts/1/')
        self.assertEqual(response.status_code, 200)

    def test_cant_retrieve_invalid_id(self):
        '''Tests if a post can't be retrieved with an invalid id'''
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, 404)

    def test_post_create(self):
        '''Tests if a post can be created'''
        response = self.client.post('/posts/', {
            'title': 'New Post',
            'content': 'This is a new post',
        })
        self.assertEqual(response.status_code, 201)

    def test_post_update(self):
        '''Tests if a post can be updated'''
        response = self.client.put('/posts/1/', {
            'title': 'Updated Post',
            'content': 'This is an updated post',
        })
        self.assertEqual(response.status_code, 200)

    def test_cant_update_other_users_post(self):
        '''Tests if a user is unable update another user's post'''
        response = self.client.put('/posts/2/', {
            'title': 'Updated Post',
            'content': 'This is an updated post',
        })
        self.assertEqual(response.status_code, 403)

    def test_post_delete(self):
        '''Tests if a post can be deleted'''
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, 204)