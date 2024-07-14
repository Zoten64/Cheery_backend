from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post

# Create your tests here.


class LikeTests(APITestCase):
    def setUp(self):
        '''
        Creates a user and a post. The user can repost their own post
        so there is no need to add a second user.
        '''
        user1 = User.objects.create_user(username='testuser1',
                                         password='password')
        self.client.force_authenticate(user=user1)
        Post.objects.create(title='test post 1',
                            content='test content 1',
                            owner=user1)

    def test_create_repost(self):
        '''
        Test if a repost can be created.
        '''
        Post.objects.get(title='test post 1')
        response = self.client.post('/reposts/', {'post': 1})
        self.assertEqual(response.status_code, 201)

    def test_delete_repost(self):
        '''
        Test if a repost can be deleted.
        '''
        Post.objects.get(title='test post 1')
        self.client.post('/reposts/', {'post': 1})
        response = self.client.delete('/reposts/1/')
        self.assertEqual(response.status_code, 204)
