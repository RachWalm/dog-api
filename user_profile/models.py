from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    UserProfile model is to store the details of the users of the site, name/email etc.
    It is related to the authentication User model through user_id and allows posts etc.
    to be sourced back to an user, e-mail is also included as a contact detail if required.
    Has date fields to allow sorting.
    """
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
        def __str__(self):
            return f"{self.first_name} {self.last_name}'s user profile"
        
def create_user_profile(sender, instance, created, **kwargs):
    """
    Function to create a userprofile when the User model creates an
    instance.
    """
    if created:
        UserProfile.objects.create(user_id=instance)
        
post_save.connect(create_user_profile, sender=User)