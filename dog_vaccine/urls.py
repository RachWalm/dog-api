from django.urls import path
from dog_vaccine import views

urlpatterns = [
    path('dog_vaccine/', views.DogVaccineList.as_view()),
    path('dog_vaccine/<int:pk>/', views.DogVaccineDetail.as_view())
]
