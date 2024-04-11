from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    
    class Meta:
        model = UserProfile
        fields= ['id', 'user_id', 'created_at', 'updated_at', 'first_name', 'last_name', 'email']