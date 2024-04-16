from django.urls import path
from dog_profile import views

urlpatterns = [
    path('dog_profile/', views.DogProfileList.as_view()),
    path('dog_profile/<int:pk>/', views.DogProfileDetail.as_view())
]
