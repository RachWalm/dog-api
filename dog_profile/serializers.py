from rest_framework import serializers
from .models import DogProfile

class DogProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for DogProfile has all the details of the dog
    """
     
    class Meta:
        model = DogProfile
        fields= [
            'id', 'dog_name', 'created_at', 'updated_at', 'received_date', 'rehomed_date', 'returned_date', 'dog_age',
            'dog_breed', 'dog_gender', 'dog_size', 'dog_image', 'at_rescue', 'status', 'general', 
            'home_cats', 'home_dogs', 'home_animals', 'home_children', 
        ]
        
# class DogProfileDetailSerializer(DogProfileSerializer):
#     """
#     Serializer for the Dog profile model used in Detail view
#     """
#     dog = serializers.ReadOnlyField(source='dogprofile.id')