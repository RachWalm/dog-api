from rest_framework import generics, permissions
# from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsOwnerOrReadOnly
from .models import DogProfile
from .serializers import DogProfileSerializer, DogProfileDetailSerializer

class DogProfileList(generics.ListCreateAPIView):
    serializer_class =  DogProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = DogProfile.objects.all()
    # filter_backends = [
    #     DjangoFilterBackend
    # ]
    
    # filterset_fields = [
    #     # all comments associated with a post
    #     'post'
    # ]
    
    # def perform_create(self, serializer):
    #     serializer.save(dog_id=self.request.user)
        

class DogProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  DogProfileDetailSerializer
    queryset = DogProfile.objects.all()
    