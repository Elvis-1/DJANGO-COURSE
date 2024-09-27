from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home),  # main/home 
     path('home2/', views.home2), 
]