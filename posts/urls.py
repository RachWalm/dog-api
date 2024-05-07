from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts_create/', views.PostCreate.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view())
]
