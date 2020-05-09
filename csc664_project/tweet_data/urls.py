from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('data', views.data),
]