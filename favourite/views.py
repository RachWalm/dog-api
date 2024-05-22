from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsOwnerOrReadOnly
from .models import Favourite
from .serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    """
    List all occassions where a person has favourited a dog
    Create a favourite link so long as the user is logged in
    Perform_create: creates actual link between user to dog
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favourite.objects.annotate(
        favourited_count=Count('dog_id__favourited', distinct=True),
        person_count=Count('user_id__person', distinct=True),
    ).order_by('-created_at')
    serializer_class = FavouriteSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'dog_name',
        'user_id',
        'created_at',
        'person_count',
        'favourited_count',
    ]
    filterset_fields = [
        'dog_id',
        'user_id',
    ]
    serializer_class = FavouriteSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a specific user that is following a dog
    No Update view, as we either want the dog as a favourite or not
    Destroy a favourite link, i.e. no longer a favourite dog
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
