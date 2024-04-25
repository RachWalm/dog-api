from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsSuperUser
from .models import DogVaccine
from .serializers import DogVaccineSerializer

class DogVaccineList(generics.ListAPIView):
    permission_classes = [IsSuperUser]
    serializer_class =  DogVaccineSerializer
    queryset = DogVaccine.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'vaccine_canine_parvovirus',
        'vaccine_canine_hepatitis',
        'vaccine_distemper',
        'vaccine_leptospirosis',
        'vaccine_kennelcough',
        'vaccine_rabies',
        'vaccine_puppy_first',
        'vaccine_puppy_second',
        'vaccine_sixmonthboost',
        'vaccine_twelvemonthboost',
    ]
    filterset_fields = [
        'overdue',
    ]

class DogVaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class =  DogVaccineSerializer
    queryset = DogVaccine.objects.all()
    