from django.urls import path
from . import views

urlpatterns = [
    path('plus', views.home),
    path('add', views.add)
]
