from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from dog_api.permissions import IsOwnerOrReadOnly

class UserProfileList(APIView):
    """
    View to provide a list of all user profiles stored in the database
    and the relevant details from the user profile
    """
    def get(self, request):
        user_profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(
            user_profiles, many=True, context={'request':request}
        )        
        return Response(serializer.data)
    
class UserProfileDetail(APIView):
    """
    View to provide a single instance of a user profile from the
    database and the relevant details from that user profile.
    Checks that the specified user profile is available in the
    database or if does not exist raising an error.
    get views user profile and put updates user profile
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            user_profile = UserProfile.objects.get(pk=pk)
            self.check_object_permissions(self.request, user_profile)
            return user_profile
        except UserProfile.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(
            user_profile, context={'request':request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        user_profile =  self.get_object(pk)
        serializer = UserProfileSerializer(
            user_profile, data=request.data, context={'request':request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)