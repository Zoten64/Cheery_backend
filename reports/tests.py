from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post

# Create your tests here.


class TestUserReports(APITestCase):
    def setUp(self):
        '''Setups the test by creating two users and logging in as user1'''
        user1 = User.objects.create_user(username='testuser1',
                                         password='testpassword')
        User.objects.create_user(username='testuser2',
                                 password='testpassword')
        self.client.force_authenticate(user=user1)

    def test_user_report(self):
        '''Tests if the logged in user can make a report on user2'''
        user2 = User.objects.get(username='testuser2')
        response = self.client.post('/reports/users/',
                                    {"reported_user": user2.id,
                                     "category": "SPAM"})
        self.assertEqual(response.status_code, 201)


class TestPostReports(APITestCase):
    def setUp(self):
        '''
        Setups the test by creating two users and a post and
        logging in as user1
        '''
        user1 = User.objects.create_user(username='testuser1',
                                         password='testpassword')
        user2 = User.objects.create_user(username='testuser2',
                                         password='testpassword')
        self.client.force_authenticate(user=user1)
        Post.objects.create(title='Test Post', content='Test Content',
                            owner=user2)

    def test_post_report(self):
        '''Tests if the logged in user can make a report on a post'''
        post = Post.objects.get(title='Test Post')
        response = self.client.post('/reports/posts/',
                                    {"reported_post": post.id,
                                     "category": "SPAM"})
        self.assertEqual(response.status_code, 201)
