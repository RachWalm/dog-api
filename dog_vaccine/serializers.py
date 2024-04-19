from rest_framework import serializers
from .models import DogVaccine

class DogVaccineSerializer(serializers.ModelSerializer):
    """
    Serializer for DogProfile has all the details of the dog
    """
    dog_name = serializers.ReadOnlyField(source='dog_id.dog_name')
    dog_id = serializers.ReadOnlyField(source='dog_id.dog_id')
    class Meta:
        model = DogVaccine
        fields= [
            'id', 'dog_id', 'overdue',
            'vaccine_canine_parvovirus', 'vaccine_canine_hepatitis', 'vaccine_distemper', 'vaccine_leptospirosis',
            'vaccine_kennelcough', 'vaccine_rabies', 'vaccine_puppy_first', 'vaccine_puppy_second', 'vaccine_sixmonthboost',
            'vaccine_twelvemonthboost', 'dog_name',
        ]
        