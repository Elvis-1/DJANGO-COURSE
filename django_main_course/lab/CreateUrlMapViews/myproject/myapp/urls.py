from django.urls import path
from . import views


urlpatterns = [ 
        path('', views.home, name="home"),
        path('aboutus/', views.about, name="aboutus"),
        path('menu/', views.menu, name="name"),
        path('book/', views.book, name="book"),
]