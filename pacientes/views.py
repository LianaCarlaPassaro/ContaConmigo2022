from django.db.models.sql import where
from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from pacientes.forms import DonanteReposicionForm, EditarPacienteForm
from pacientes.models import Pacientes
from reposicionesAsignadas.models import ReposicionesAsignadas


def listadoPaciente(request):
    donantes_requeridos = {'listado_don_req':Pacientes.objects.order_by('id'), 'cant_don':Pacientes.objects.count()}
    return render(request, 'paciente/listado.html',donantes_requeridos)

def nuevoPaciente(request):
    if request.method == 'POST':
        formaDonanteReposicion = DonanteReposicionForm(request.POST)
        if formaDonanteReposicion.is_valid():
            formaDonanteReposicion.save()
            return redirect('listadoPaciente')
    else:
        formaDonanteReposicion = DonanteReposicionForm()

    formaDonanteReposicion = {'formaDonanteReposicion': DonanteReposicionForm()}
    return render(request, 'paciente/nuevo.html', formaDonanteReposicion)

def detalleDonanteReposicion(request, id):
    donanteReposicion = {'detalle_don_rep': get_object_or_404(Pacientes, pk=id)}
    return render(request, 'paciente/detalle.html', donanteReposicion)

#DonanteReposicionForm = modelform_factory(DonanteReposicion, exclude=[])

def editarDonanteReposicion(request, id):
    donanteReposicion = get_object_or_404(Pacientes, pk=id)
    if request.method == 'POST':
        formaDonanteReposicion = EditarPacienteForm(request.POST, instance=donanteReposicion)
        if formaDonanteReposicion.is_valid():
            formaDonanteReposicion.save()
            return redirect('listadoPaciente')
    else:

        formaDonanteReposicion = EditarPacienteForm(instance=donanteReposicion)

    return render(request, 'paciente/editar.html', {'formaDonanteReposicion': formaDonanteReposicion})

def eliminarDonanteReposicion(request, id):
    donanteReposicion = get_object_or_404(Pacientes, pk=id)
    if donanteReposicion:
        donanteReposicion.delete()
    return redirect('listadoPaciente')





