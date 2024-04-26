from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase
from dog_profile.models import DogProfile

class PostListAndCreateViewTests(APITestCase):
    def setUp(self):
        User.objects.create_superuser(username='Super', password='password')
        User.objects.create_user(username='User', password='password')
        DogProfile.objects.create(dog_name='michelle', dog_age='1')
        
    def test_can_list_posts(self):
        super = User.objects.get(username='Super')
        dog = DogProfile.objects.get(dog_name='michelle')
        Post.objects.create(user_id=super, title='a title', dog_id=dog)
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))
        
    def test_logged_in_superuser_can_create_post(self):
        self.client.login(username='Super', password='password')
        response = self.client.post('/posts_create/', {'title': 'a title', 'dog_id': '1'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_logged_out_cannot_create_post(self):
        response = self.client.post('/posts_create/', {'title': 'a title', 'dog_id': '1'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
