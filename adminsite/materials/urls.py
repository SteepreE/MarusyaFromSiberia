from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.materials, name='materials'),
    path('add', views.add_material, name='add_material'),
]
