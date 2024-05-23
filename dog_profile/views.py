from django.db.models import Count
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsSuperUser
from dog_api.permissions import IsSuperUserOrReadOnly, IsStaffOrReadOnly
from .models import DogProfile
from .serializers import DogProfileSerializer


class DogProfileList(generics.ListAPIView):
    serializer_class = DogProfileSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = DogProfile.objects.annotate(
        fav_count=Count('favourited', distinct=True)
    ).order_by('-created_at')
    serializer_class = DogProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
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
    filterset_fields = [
        'dog_gender',
        'dog_size',
        'home_cats',
        'home_dogs',
        'home_animals',
        'home_children',
        'status',
    ]


class DogProfileCreate(generics.CreateAPIView):
    """Create dog profiles"""
    serializer_class = DogProfileSerializer
    permission_classes = [
        IsSuperUser
    ]


class DogProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DogProfileSerializer
    queryset = DogProfile.objects.all()
