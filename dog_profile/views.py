from django.db.models import Count
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from dog_api.permissions import IsOwnerOrReadOnly, IsSuperUser, IsSuperUserOrReadOnly, IsStaffOrReadOnly
from .models import DogProfile
from .serializers import DogProfileSerializer

class DogProfileList(generics.ListAPIView):
    serializer_class =  DogProfileSerializer
    permission_classes = [IsStaffOrReadOnly]
    queryset = DogProfile.objects.annotate(
        fav_count = Count('favourited', distinct=True)
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

    # def post(self, request):
    #     serializer = DogProfileSerializer(
    #         data=request.data, context={'request': request}
    #     )
    #     if serializer.is_valid():
    #         serializer.save(user_id=request.user)
    #         return Response(
    #             serializer.data, status=status.HTTP_201_CREATED
    #         )
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

class DogProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUserOrReadOnly]
    serializer_class =  DogProfileSerializer
    queryset = DogProfile.objects.all()
    