from django.urls import path
from user_profile import views

urlpatterns = [
    path('user_profile/', views.UserProfileList.as_view()),
    path('user_profile/<int:pk>/', views.UserProfileDetail.as_view())
]
