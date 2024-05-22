from rest_framework import serializers
from .models import RequestAdopt


class RequestAdoptSerializer(serializers.ModelSerializer):
    """
    Serializer for RequestAdopt has all the details from an
    adoption request form
    """
    class Meta:
        model = RequestAdopt
        fields = [
            'id', 'user_id', 'dog_id', 'created_at',
            'updated_at', 'contact_permission',
            'home_cats', 'home_dogs', 'home_animals',
            'home_children', 'experience', 'query',
        ]
        read_only_fields = ['user_id']  # Ensure user field is read-only

    def create(self, validated_data):
        """Set the user_id field to the current authenticated user.
        otherwise users could send the form on other users behalf
        """
        validated_data['user_id'] = self.context['request'].user
        return super().create(validated_data)
