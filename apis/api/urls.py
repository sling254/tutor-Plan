from django.urls import path
from .views import getRouter


urlpatterns = [
    path('',getRouter, name="getrouters"),    # getRouter is a function in views.py
]