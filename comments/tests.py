from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment

# Create your tests here.


class CommentTests(APITestCase):
    def setUp(self):
        '''Creates 2 users for testing and one post as well as 2 comments'''
        user1 = User.objects.create_user(username='testuser',
                                         password='testpassword')
        self.client.force_authenticate(user=user1)
        user2 = User.objects.create_user(username='testuser2',
                                         password='testpassword')
        post = Post.objects.create(title='Test Post',
                                   content='Test content',
                                   owner=user2)
        Comment.objects.create(post=post,
                               owner=user1,
                               content='Test comment')
        Comment.objects.create(post=post,
                               owner=user2,
                               content='Test comment 2')

    def test_comment_list(self):
        '''Tests if the comment list view is accessible'''
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, 200)

    def test_can_retrieve_comment(self):
        '''Tests if a comment can be retrieved by id'''
        response = self.client.get('/comments/1')
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        '''Tests creating a comment'''
        post = Post.objects.get(title='Test Post')

        response = self.client.post('/comments/', {
            'post': post.id,
            'content': 'Test comment'
        })

        self.assertEqual(response.status_code, 201)

    def test_update_comment(self):
        '''Tests if a user can update their own comment'''
        response = self.client.put('/comments/1', {
            'post': 1,
            'content': 'Updated comment'
        })

        self.assertEqual(response.status_code, 200)

    def test_cant_update_others_comment(self):
        '''Tests if a user can't update another user's comment'''
        response = self.client.put('/comments/2', {
            'post': 2,
            'content': 'Updated comment'
        })

        self.assertEqual(response.status_code, 403)

    def test_delete_comment(self):
        '''Tests if a user can delete their own comment'''
        response = self.client.delete('/comments/1')
        self.assertEqual(response.status_code, 204)

    def test_cant_delete_others_comment(self):
        '''Tests if a user can't delete another user's comment'''
        response = self.client.delete('/comments/2')
        self.assertEqual(response.status_code, 403)
