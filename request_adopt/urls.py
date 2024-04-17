from django.urls import path
from request_adopt import views

urlpatterns = [
    path('request_adopt/', views.RequestAdoptList.as_view()),
    path('request_adopt/<int:pk>/', views.RequestAdoptDetail.as_view())
]
