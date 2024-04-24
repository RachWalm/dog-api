from rest_framework import generics, permissions
# from django_filters.rest_framework import DjangoFilterBackend
# from dog_api.permissions import IsOwnerOrReadOnly
from .models import DogProfile
from .serializers import DogProfileSerializer

class DogProfileList(generics.ListCreateAPIView):
    serializer_class =  DogProfileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = DogProfile.objects.all()

class DogProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  DogProfileSerializer
    queryset = DogProfile.objects.all()
    