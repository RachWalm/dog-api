from django.db import models
from dog_profile.models import DogProfile

class DogVaccine(models.Model):
    """
    DogVaccine model is to store the details of the dogs that are in/have been
    in the rescue and their vaccination status.
    The model holds confidential information for the 
    rescue day to day running to care for the dog.
    """
    dog_id = models.ForeignKey(DogProfile, on_delete=models.CASCADE)
    overdue = models.BooleanField(default=True)
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
        
    class Meta:
        ordering = ['-dog_id']
        
        def __str__(self):
            return f"{self.dog_name} vaccine"