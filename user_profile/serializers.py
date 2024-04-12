from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.username')
    is_owner = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user_id
    
    class Meta:
        model = UserProfile
        fields= [
            'id', 'user_id', 'created_at', 'updated_at', 'first_name', 'last_name', 'email', 'is_owner'
        ]