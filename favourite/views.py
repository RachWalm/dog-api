from rest_framework import generics, permissions
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
    queryset = Favourite.objects.all()
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