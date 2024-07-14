from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTests(APITestCase):
    def setUp(self):
        '''Creates a user on setup. A profile is created automatically.'''
        user = User.objects.create_user(username='testuser', password='pass')
        self.client.force_authenticate(user=user)

    def test_profile_created(self):
        '''Tests if the profile is created automatically.'''
        user = User.objects.get(username='testuser')
        profile = Profile.objects.get(owner=user)
        self.assertEqual(profile.owner, user)

    def test_retrieve_profile(self):
        '''Tests if the profile detail view is accessible.'''
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        '''Tests if the profile can be updated.'''
        response = self.client.put(
            '/profiles/1/', {'username': 'testusername'})
        self.assertEqual(response.status_code, 200)

    def test_retrieve_user(self):
        '''Tests if the user detail view is accessible.'''
        response = self.client.get('/profiles/1/owner')
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        '''Tests if a user can be deleted.'''
        response = self.client.delete('/profiles/1/owner')
        self.assertEqual(response.status_code, 204)
