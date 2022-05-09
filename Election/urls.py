from . import views
from django.urls import path


urlpatterns = [
    path('home', views.home, name="home"),
    path("", views.index, name='index'),
    path("LGA_result", views.LGA_result, name="LGA_result"),
    path("New_PU", views.New_PU, name="New_PU") 

]