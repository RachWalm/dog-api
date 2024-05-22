from django.db import models
from django.contrib.auth.models import User
from dog_profile.models import DogProfile


class RequestAdopt(models.Model):
    """
    RequestAdopt model is to store the details of the users of the site request
    when they fill out a form to adopt a dog.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dog_id = models.ForeignKey(DogProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact_permission = models.BooleanField(default=False)
    home_children = models.BooleanField(default=False)
    home_cats = models.BooleanField(default=False)
    home_animals = models.BooleanField(default=False)
    home_dogs = models.BooleanField(default=False)
    experience = models.TextField(max_length=1000, blank=True, null=True)
    query = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user_id} interest in {self.dog_id}"
