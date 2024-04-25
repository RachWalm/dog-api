from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsOwnerOrReadOnly
from .models import RequestAdopt
from .serializers import RequestAdoptSerializer

class RequestAdoptList(generics.ListCreateAPIView):
    serializer_class =  RequestAdoptSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RequestAdopt.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'updated_at',
        'created_at'
    ]
    
    filterset_fields = [
        'user_id',
        'dog_id',
    ]
    
class RequestAdoptDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  RequestAdoptSerializer
    queryset = RequestAdopt.objects.all()
    