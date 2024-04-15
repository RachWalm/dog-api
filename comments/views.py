from rest_framework import generics, permissions
# from django_filters.rest_framework import DjangoFilterBackend
from dog_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    serializer_class =  CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    # filter_backends = [
    #     DjangoFilterBackend
    # ]
    
    # filterset_fields = [
    #     # all comments associated with a post
    #     'post'
    # ]
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class =  CommentDetailSerializer
    queryset = Comment.objects.all()
    