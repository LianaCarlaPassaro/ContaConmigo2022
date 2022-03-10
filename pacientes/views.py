from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from pacientes.forms import DonanteReposicionForm
from pacientes.models import Pacientes

def listadoDonanteReposicion(request):
    donantes_requeridos = {'listado_don_req':Pacientes.objects.order_by('id'), 'cant_don':Pacientes.objects.count()}
    return render(request, 'donantesReposicion/listado.html',donantes_requeridos)

def nuevoDonanteReposicion(request):
    if request.method == 'POST':
        formaDonanteReposicion = DonanteReposicionForm(request.POST)
        if formaDonanteReposicion.is_valid():
            formaDonanteReposicion.save()
            return redirect('listadoDonantesReposicion')
    else:
        formaDonanteReposicion = DonanteReposicionForm()

    formaDonanteReposicion = {'formaDonanteReposicion': DonanteReposicionForm()}
    return render(request, 'donantesReposicion/nuevo.html', formaDonanteReposicion)

def detalleDonanteReposicion(request, id):
    donanteReposicion = {'detalle_don_rep': get_object_or_404(Pacientes, pk=id)}
    return render(request, 'donantesReposicion/detalle.html', donanteReposicion)

#DonanteReposicionForm = modelform_factory(DonanteReposicion, exclude=[])

def editarDonanteReposicion(request, id):
    donanteReposicion = get_object_or_404(Pacientes, pk=id)
    if request.method == 'POST':
        formaDonanteReposicion = DonanteReposicionForm(request.POST, instance=donanteReposicion)
        if formaDonanteReposicion.is_valid():
            formaDonanteReposicion.save()
            return redirect('listadoDonantesReposicion')
    else:

        formaDonanteReposicion = DonanteReposicionForm(instance=donanteReposicion)

    return render(request, 'donantesReposicion/editar.html', {'formaDonanteReposicion': formaDonanteReposicion})

def eliminarDonanteReposicion(request, id):
    donanteReposicion = get_object_or_404(Pacientes, pk=id)
    if donanteReposicion:
        donanteReposicion.delete()
    return redirect('listadoDonantesReposicion')



