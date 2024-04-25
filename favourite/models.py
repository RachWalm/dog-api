from django.db import models
from django.contrib.auth.models import User
from dog_profile.models import DogProfile
from user_profile.models import UserProfile

class Favourite(models.Model):
    """
    Favourite model is to store a link between a user and a dog that they
    want included in their favourite list so that they can go straight to dogs
    they like instead of searching for them
    """
    user_id = models.ForeignKey(User, related_name='person', on_delete=models.CASCADE)
    dog_id = models.ForeignKey(DogProfile, related_name='favourited', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user_id', 'dog_id']
        
    def __str__(self):
        return f"{self.dog_id} is one of {self.user_id}'s favourites"