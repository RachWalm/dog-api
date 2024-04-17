from rest_framework import serializers
from .models import RequestAdopt

class RequestAdoptSerializer(serializers.ModelSerializer):
    """
    Serializer for RequestAdopt has all the details from an adoption request form
    """
     
    class Meta:
        model = RequestAdopt
        fields= [
            'id', 'user_id', 'dog_id', 'created_at', 'updated_at', 'contact_permission',
            'home_cats', 'home_dogs', 'home_animals', 'home_children', 'experience', 'query',
        ]
        