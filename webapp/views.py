from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pacientes.models import Pacientes
from provincia.models import Provincia

def bienvenido(request):

    donantes_requeridos = {'listado_don_req':Pacientes.objects.order_by('id'), 'cant_don':Pacientes.objects.count()}
    return render(request, 'bienvenido.html',donantes_requeridos)

