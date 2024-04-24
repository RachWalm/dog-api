from rest_framework import serializers
from .models import DogProfile
from favourite.models import Favourite

class DogProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for DogProfile has all the details of the dog
    """
    favourite_id = serializers.SerializerMethodField()
    
    def get_favourite_id(self, obj):
        """
        Checks if the current dog is a favourite of the logged in user
        and returns the id of the favourite record if it is a favourite.
        """
        logged_in = self.context['request'].user
        if logged_in.is_authenticated:
            favourite = Favourite.objects.filter(
                user_id=logged_in, dog_id=obj.id
            ).first()
            print(favourite)
            return favourite.id if favourite else None
        return None
    
    class Meta:
        model = DogProfile
        fields= [
            'id', 'dog_name', 'created_at', 'updated_at', 'received_date', 'rehomed_date', 'returned_date', 'dog_age',
            'dog_breed', 'dog_gender', 'dog_size', 'dog_image', 'at_rescue', 'status', 'general', 
            'home_cats', 'home_dogs', 'home_animals', 'home_children', 'favourite_id', #'favourite_count'
        ]
        
# class DogProfileDetailSerializer(DogProfileSerializer):
#     """
#     Serializer for the Dog profile model used in Detail view
#     """
#     dog = serializers.ReadOnlyField(source='dogprofile.id')