from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """Serializer for post includes authentication on is_owner to check if logged in"""
    user_id = serializers.ReadOnlyField(source='user_id.username')
    is_owner = serializers.SerializerMethodField()
    users_first_name = serializers.ReadOnlyField(source='user_id.userprofile.first_name')
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user_id
    
    class Meta:
        model = Post
        fields= [
            'id', 'user_id', 'created_at', 'updated_at', 'title', 'content', 'image', 'is_owner', 'users_first_name'
        ]