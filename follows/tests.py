from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Follow

# Create your tests here.


class LikeTests(APITestCase):
    def setUp(self):
        '''
        Creates 2 users for testing the follower function
        '''
        user1 = User.objects.create_user(username='testuser1',
                                         password='password')
        self.client.force_authenticate(user=user1)
        User.objects.create_user(username='testuser2',
                                 password='password')

    def test_follow(self):
        '''
        Tests if user 1 can follow user 2
        '''
        response = self.client.post('/follows/', {'followed_user': 2})
        self.assertEqual(response.status_code, 201)

    def test_cant_follow_twice(self):
        '''
        Test if a user can follow the same user twice
        '''
        # First follow
        self.client.post('/follows/', {'followed_user': 2})
        # Second follow
        response = self.client.post('/follows/', {'followed_user': 2})
        self.assertEqual(response.status_code, 400)

    def test_unfollow(self):
        '''
        Test if a user can unfollow a user
        '''
        self.client.post('/follows/', {'followed_user': 2})
        response = self.client.delete('/follows/1/')
        self.assertEqual(response.status_code, 204)

    def cant_follow_self(self):
        '''
        Test if a user can follow themselves
        '''
        response = self.client.post('/follows/', {'followed_user': 1})
        self.assertEqual(response.status_code, 400)
