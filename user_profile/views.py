
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserProfile
from .serializers import UserProfileSerializer
from dog_api.permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly


class UserProfileList(generics.ListAPIView):
    """
    View to provide a list of all user profiles stored in the database
    and the relevant details from the user profile. No create as created
    when auth creates a User
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = UserProfile.objects.annotate(
        post_count=Count('user_id__post', distinct=True),
        comment_count=Count('user_id__comment', distinct=True),
        fav_count=Count('user_id__person', distinct=True),
    ).order_by('-created_at')
    serializer_class = UserProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'fav_count',
        'updated_at',
        'created_at'
    ]
    filterset_fields = [
        'user_id__person__dog_id',
    ]


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    """
    View to provide a single instance of a user profile from the
    database and the relevant details from that user profile.
    Only retreive and Update as other stuff comes from User
    Model in auth
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
