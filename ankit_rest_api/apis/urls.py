from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path("v1/", welcome_call), 
    path("v2/", hello)
    ]