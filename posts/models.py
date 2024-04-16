from django.db import models
from django.contrib.auth.models import User
from dog_profile.models import DogProfile


class Post(models.Model):
    """
    Post model is linked to the User that created the post and has
    the dates so that it can be sorted by most recent. The title and content
    will be written by the user. Image and content can be left blank as some posts
    maybe story without an image or just an image. Title is required.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dog_id = models.ForeignKey(DogProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
    