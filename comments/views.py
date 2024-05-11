from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    serializer_class =  CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'updated_at',
        'created_at'
    ]
    search_fields = [
        'comment_content',
    ]
    filterset_fields = [
        'user_id',
        'post_id',
    ]
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  CommentDetailSerializer
    queryset = Comment.objects.all()
    