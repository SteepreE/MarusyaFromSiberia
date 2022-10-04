from django.shortcuts import render

from . import models


def orders(request):
    context = {'orders': models.Order.objects.all()}

    return render(request, 'orders.html', context)


def login(request):
    return render(request, 'login.html')


def add_order(request):
    return render(request, 'add_order.html')


def order(request, order_id):
    context = {'order': models.Order.objects.get(pk=order_id)}

    return render(request, 'order.html', context)
