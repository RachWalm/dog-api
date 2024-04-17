from django.db import models

class GenderChoices(models.Model):
    '''List of the gender choices model'''
    GENDER_CHOICES = (
        (0, 'TBC'),
        (1, 'Male'),
        (2, 'Female'),
    )
    
class SizeChoices(models.Model):
    '''List of the size choices model'''
    SIZE_CHOICES = (
        (0, 'TBC'),
        (1, 'Small'),
        (2, 'Large'),
    )
    
class StatusChoices(models.Model):
    '''List of the size choices model'''
    STATUS_CHOICES = (
        (0, 'To arrive'),
        (1, 'Not available'),
        (2, 'Available'),
        (3, 'Rehomed')
    )

class DogProfile(models.Model):
    """
    DogProfile model is to store the details of the dogs that are in/have been
    in the rescue.
    The model holds both the public available information on the dogs and the
    rescue day to day running information to care for the dog.
    """
    dog_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    received_date = models.DateTimeField(blank=True, null=True)
    rehomed_date = models.DateTimeField(blank=True, null=True)
    returned_date = models.DateTimeField(blank=True, null=True)
    dog_age = models.IntegerField(blank=True)
    dog_breed = models.CharField(max_length=255)
    dog_gender = models.IntegerField(choices=GenderChoices.GENDER_CHOICES, default=0)
    dog_size = models.IntegerField(choices=SizeChoices.SIZE_CHOICES, default=0)
    dog_image = models.ImageField(
        upload_to='images/',
        default='../dog-image-na_zmmfot'
    )
    at_rescue = models.BooleanField(default=True)
    status = models.IntegerField(choices=StatusChoices.STATUS_CHOICES, default=0)
    general = models.TextField()
    vaccine_canine_parvovirus = models.DateTimeField(blank=True, null=True)
    vaccine_canine_hepatitis = models.DateTimeField(blank=True, null=True)
    vaccine_distemper = models.DateTimeField(blank=True, null=True)
    vaccine_leptospirosis = models.DateTimeField(blank=True, null=True)
    vaccine_kennelcough = models.DateTimeField(blank=True, null=True)
    vaccine_rabies = models.DateTimeField(blank=True, null=True)
    vaccine_puppy_first = models.DateTimeField(blank=True, null=True)
    vaccine_puppy_second = models.DateTimeField(blank=True, null=True)
    vaccine_sixmonthboost = models.DateTimeField(blank=True, null=True)
    vaccine_twelvemonthboost = models.DateTimeField(blank=True, null=True)
    home_cats = models.BooleanField(default=False)
    home_dogs = models.BooleanField(default=False)
    home_animals = models.BooleanField(default=False)
    home_children = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        
        def __str__(self):
            return f"{self.dog_name} received {self.received_date} profile"