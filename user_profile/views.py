from django.db.models import Count
from rest_framework import generics, filters
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from dog_api.permissions import IsOwnerOrReadOnly

class UserProfileList(generics.ListAPIView):
    """
    View to provide a list of all user profiles stored in the database
    and the relevant details from the user profile. No create as created
    when auth creates a User
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class UserProfileDetail(generics.RetreiveUpdateAPIView):
    """
    View to provide a single instance of a user profile from the
    database and the relevant details from that user profile.
    Only retreive and Update as other stuff comes from User
    Model in auth
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserProfile.objects.all()
    