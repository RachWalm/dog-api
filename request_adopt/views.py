from rest_framework import generics, permissions
# from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsOwnerOrReadOnly
from .models import RequestAdopt
from .serializers import RequestAdoptSerializer

class RequestAdoptList(generics.ListCreateAPIView):
    serializer_class =  RequestAdoptSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RequestAdopt.objects.all()
    # filter_backends = [
    #     DjangoFilterBackend
    # ]
    
    # filterset_fields = [
    #     # all comments associated with a post
    #     'post'
    # ]
    
    # def perform_create(self, serializer):
    #     serializer.save(user_id=self.request.user)
        

class RequestAdoptDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  RequestAdoptSerializer
    queryset = RequestAdopt.objects.all()
    