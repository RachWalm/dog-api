from django.db import IntegrityError
from rest_framework import serializers
from .models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the favourite model
    Create method handles the UNIQUE constraint on 'user_id' and 'dog_id'
    when a user wants to favourite a dog.
    """
    user_id = serializers.ReadOnlyField(source='user_id.username')
    dog_name = serializers.ReadOnlyField(source='dog_id.dog_name')

    class Meta:
        model = Favourite
        fields = [
            'id', 'user_id', 'created_at', 'dog_id', 'dog_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})