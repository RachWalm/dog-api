from rest_framework import generics, permissions
# from django_filters.rest_framework import DjangoFilterBackend
# from dog_api.permissions import IsOwnerOrReadOnly
from .models import DogVaccine
from .serializers import DogVaccineSerializer

class DogVaccineList(generics.ListCreateAPIView):
    serializer_class =  DogVaccineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = DogVaccine.objects.all()
    # filter_backends = [
    #     DjangoFilterBackend
    # ]
    
    # filterset_fields = [
    #     # all comments associated with a post
    #     'post'
    # ]
    
    # def perform_create(self, serializer):
    #     serializer.save(dog_id=self.request.user)
        

class DogVaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  DogVaccineSerializer
    queryset = DogVaccine.objects.all()
    