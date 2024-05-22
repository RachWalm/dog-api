from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for post includes authentication on is_owner to
    check if logged in and has postee's first name available
    """
    user_id = serializers.ReadOnlyField(source='user_id.username')
    is_owner = serializers.SerializerMethodField()
    users_first_name = serializers.ReadOnlyField(source='user_id.userprofile.first_name')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 *2 : 
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is larger than 4096 px'
            )
        if value.image.height > 4066:
            raise serializers.ValidationError(
                'Image height is larger than 4096 px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user_id

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Post
        fields = [
            'id', 'user_id', 'created_at', 'updated_at',
            'title', 'content', 'image', 'is_owner',
            'users_first_name', 'dog_id'
        ]
