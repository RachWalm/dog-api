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
        # print(response.data)
        # print(len(response.data))
        
    def test_logged_in_superuser_can_create_post(self):
        self.client.login(username='Super', password='password')
        response = self.client.post('/posts_create/', {'title': 'a title', 'dog_id': '1'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_logged_out_cannot_create_post(self):
        response = self.client.post('/posts_create/', {'title': 'a title', 'dog_id': '1'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
class PostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password="pass")
        brian = User.objects.create_user(username='brian', password="pass")
        dog = DogProfile.objects.create(dog_name='michelle', dog_age='1')
        Post.objects.create(
            user_id=adam, title='a title', content='adams content', dog_id=dog
        )
        Post.objects.create(
            user_id=brian, title='another title', content='brians content', dog_id=dog
        )
        
    def test_can_retrieve_post_using_valid_id(self):
        response =  self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_can_retrieve_post_using_invalid_id(self):
        response =  self.client.get('/posts/9/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        
    # def test_user_can_update_own_posts(self):
    #     self.client.login(username='adam', password='pass')
    #     response = self.client.put('/posts/1/', {'title': 'a new title'})
    #     post = Post.objects.filter(pk=1).first()
    #     print(post)
    #     self.assertEqual(post.title, 'a new title')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    def test_user_cant_update_others_posts(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    