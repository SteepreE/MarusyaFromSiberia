from django.shortcuts import render

from . import models
from django.contrib.auth.views import login_required


@login_required(login_url='/login', redirect_field_name='')
def orders(request):
    context = {'orders': models.Order.objects.all()}

    return render(request, 'orders.html', context)


@login_required(login_url='/login', redirect_field_name='')
def add_order(request):
    return render(request, 'add_order.html')


@login_required(login_url='/login', redirect_field_name='')
def order(request, order_id):
    context = {'order': models.Order.objects.get(pk=order_id)}

    return render(request, 'order.html', context)
