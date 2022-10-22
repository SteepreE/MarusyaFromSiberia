from django.shortcuts import render
from .models import Master

from django.contrib.auth.views import login_required


@login_required(login_url='/login', redirect_field_name='')
def masters(request):
    context = {'masters': Master.objects.all()}

    return render(request, 'masters.html', context)


@login_required(login_url='/login', redirect_field_name='')
def add_master(request):
    if request.method != "POST":
        return {'success': False}

    master = Master(first_name="Яков", second_name="Горюнов", third_name="Павлович", phone_number="89991112233")

    master.save()

    return masters(request)
