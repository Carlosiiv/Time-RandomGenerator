# from django.contrib import 
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    
]