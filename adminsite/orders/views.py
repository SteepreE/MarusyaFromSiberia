from django.shortcuts import render

from . import models
from django.contrib.auth.views import login_required


class Order:
    product = "Пиджак"
    current_stage = "Пошив"
    id = 1
    client = "Яков"


@login_required(login_url='/login', redirect_field_name='')
def orders(request):
    orders = [Order() for x in range(8)]
    print(dict(request.GET.items()))

    context = {
        'orders': orders,
        'filter_atrs': ['Название','Стадия производства','Дата','Клиент']
    }

    return render(request, 'orders.html', context)


@login_required(login_url='/login', redirect_field_name='')
def add_order(request):
    return render(request, 'add_order.html')


@login_required(login_url='/login', redirect_field_name='')
def order(request, order_id):
    context = {'order': models.Order.objects.get(pk=order_id)}

    return render(request, 'order.html', context)
