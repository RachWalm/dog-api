from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile includes authentication on is_owner to check if logged in"""
    user_id = serializers.ReadOnlyField(source='user_id.username')
    is_owner = serializers.SerializerMethodField()
    is_staff = serializers.SerializerMethodField()
    is_superuser = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user_id
    
    def get_is_staff(self, obj):
        return obj.user_id.is_staff
    
    def get_is_superuser(self, obj):
        return obj.user_id.is_superuser
    
    class Meta:
        model = UserProfile
        fields= [
            'id', 'user_id', 'created_at', 'updated_at', 'first_name', 'last_name',
            'email', 'is_owner', 'is_staff', 'is_superuser',
        ]