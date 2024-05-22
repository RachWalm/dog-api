from django.db import models
from django.db.models.signals import post_save
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
    vaccine_canine_parvovirus = models.DateField(blank=True, null=True)
    vaccine_canine_hepatitis = models.DateField(blank=True, null=True)
    vaccine_distemper = models.DateField(blank=True, null=True)
    vaccine_leptospirosis = models.DateField(blank=True, null=True)
    vaccine_kennelcough = models.DateField(blank=True, null=True)
    vaccine_rabies = models.DateField(blank=True, null=True)
    vaccine_puppy_first = models.DateField(blank=True, null=True)
    vaccine_puppy_second = models.DateField(blank=True, null=True)
    vaccine_sixmonthboost = models.DateField(blank=True, null=True)
    vaccine_twelvemonthboost = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-dog_id']

    def __str__(self):
        return f"{self.dog_id} vaccine"


def create_dog_vaccine(sender, instance, created, **kwargs):
    """
    Function to create a userprofile when the User model creates an
    instance.
    """
    if created:
        DogVaccine.objects.create(dog_id=instance)


post_save.connect(create_dog_vaccine, sender=DogProfile)
