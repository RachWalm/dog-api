from django.db.models import Count
from rest_framework import generics, permissions, filters
# from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsOwnerOrReadOnly
from .models import DogProfile
from .serializers import DogProfileSerializer

class DogProfileList(generics.ListCreateAPIView):
    serializer_class =  DogProfileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = DogProfile.objects.annotate(
        fav_count = Count('favourited', distinct=True)
    ).order_by('-created_at')
    serializer_class = DogProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        # DjangoFilterBackend,
    ]
    ordering_fields = [
        'fav_count',
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'dog_name',
        'dog_breed',
    ]
    # filterset_fields = [
    #     'dog_id',
    # ]

class DogProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  DogProfileSerializer
    queryset = DogProfile.objects.all()
    