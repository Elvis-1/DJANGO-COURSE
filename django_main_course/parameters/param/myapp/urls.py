from django.urls import path
from myapp import views

urlpatterns = [
    path('getuser/<name>/<id>', views.pathview, name='pathview'), 
    path('getuser/', views.qryview, name='qryview'),
    path('showform/', views.showform, name='showform'), 
    path("showform/getform/", views.getform, name='getform'),
 #   path('showtemplatedir/', views.show_template_dirs, name='show_template_dirs'), 
]