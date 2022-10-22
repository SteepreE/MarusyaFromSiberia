from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.masters, name='masters'),
    path('add', views.add_master, name='add_master')
]