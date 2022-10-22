from django.shortcuts import render
from .models import Material

from django.contrib.auth.views import login_required


@login_required(login_url='/login', redirect_field_name='')
def materials(request):
    context = {'materials': Material.objects.all()}

    return render(request, 'materials.html', context)


@login_required(login_url='/login', redirect_field_name='')
def add_material(request):
    if request.method != "POST":
        return {'success': False}

    material = Material(name="Вельвет", count=1, price=100.0)

    material.save()

    return materials(request)
