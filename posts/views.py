from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, generics
from .models import Post
from .serializers import PostSerializer
from dog_api.permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly


class PostList(generics.ListAPIView):
    """
    View to provide a list of all posts stored in the database
    and the relevant details from the posts
    """
    serializer_class = PostSerializer
    permission_classes = [
        IsSuperUserOrReadOnly
    ]
    queryset = Post.objects.all().order_by('-created_at')
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
        'title',
        'content',
    ]
    filterset_fields = [
        'dog_id',
        'user_id',
    ]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class PostCreate(generics.ListCreateAPIView):
    """Create posts"""
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]
    queryset = Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to provide a single instance of a post from the
    database and the relevant details from that post.
    Checks that the specified post id is available in the
    database or if does not exist raising an error.
    get - views post and put - updates post and delete -
    deletes the post specified
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all(
    ).order_by('-created_at')
