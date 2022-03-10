from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from reposicionesAsignadas.forms import DonanteReposicionAsignadaForm
from reposicionesAsignadas.models import ReposicionesAsignadas

def listadoPacienteAsignado(request):
    donante_asignado = {'listado_don_asignados':ReposicionesAsignadas.objects.order_by('id'), 'cant_don_asig':ReposicionesAsignadas.objects.count()}
    return render(request, 'reposicionesAsignadas/listadoPacienteAsignado.html',donante_asignado)

def nuevoDonanteAsignar(request):
    if request.method == 'POST':
        formaReposicionAsignada = DonanteReposicionAsignadaForm(request.POST)
        if formaReposicionAsignada.is_valid():
            formaReposicionAsignada.save()
            return redirect('listadoPacientesAsignado')
    else:
        formaReposicionAsignada = DonanteReposicionAsignadaForm()

    formaReposicionAsignada = {'formaReposicionAsignada': DonanteReposicionAsignadaForm()}
    return render(request, 'reposicionesAsignadas/nuevo.html', formaReposicionAsignada)

def detalleDonanteAsignado(request, id):
    donante_asignado = {'detalle_don_asignados': get_object_or_404(ReposicionesAsignadas, pk=id)}
    return render(request, 'reposicionesAsignadas/detalle.html', donante_asignado)

def editarDonanteAsignado(request, id):
    donanteReposicionAsignada = get_object_or_404(ReposicionesAsignadas, pk=id)
    if request.method == 'POST':
        formaDonanteReposicionAsignada = DonanteReposicionAsignadaForm(request.POST, instance=donanteReposicionAsignada)
        if formaDonanteReposicionAsignada.is_valid():
            formaDonanteReposicionAsignada.save()
            return redirect('listadoPacientesAsignado')
    else:

        formaDonanteReposicionAsignada = DonanteReposicionAsignadaForm(instance=donanteReposicionAsignada)

    return render(request, 'reposicionesAsignadas/editar.html', {'formaDonanteReposicionAsignada': formaDonanteReposicionAsignada})

def eliminarDonanteAsignado(request, id):
    donanteAsignado = get_object_or_404(ReposicionesAsignadas, pk=id)
    if donanteAsignado:
        donanteAsignado.delete()
    return redirect('listadoDonantes')