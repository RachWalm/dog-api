from rest_framework import generics, permissions
# from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsSuperUser
from .models import DogVaccine
from .serializers import DogVaccineSerializer

class DogVaccineList(generics.ListAPIView):
    permission_classes = [IsSuperUser]
    serializer_class =  DogVaccineSerializer
    queryset = DogVaccine.objects.all()
    # filter_backends = [
    #     DjangoFilterBackend
    # ]
    
    # filterset_fields = [
    #     # all comments associated with a post
    #     'post'
    # ]

class DogVaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class =  DogVaccineSerializer
    queryset = DogVaccine.objects.all()
    