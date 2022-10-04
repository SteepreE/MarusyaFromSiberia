from django.urls import path

from . import views

urlpatterns = [
    path('', views.orders),
    path('order-<int:order_id>/', views.order),
    path('add-order/', views.add_order),
    path('login/', views.login)
]
