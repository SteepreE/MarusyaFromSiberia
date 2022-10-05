from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.orders),
    path('order-<int:order_id>/', views.order),
    path('add-order/', views.add_order)
]
