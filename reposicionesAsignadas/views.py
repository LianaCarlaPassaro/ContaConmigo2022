from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from pacientes.models import Pacientes
from reposicionesAsignadas.forms import DonanteReposicionAsignadaForm
from reposicionesAsignadas.models import ReposicionesAsignadas

def listadoDonantesAplicados(request, id, nombre, apellido):
    #donante_asignado = {'listado_don_asignados':ReposicionesAsignadas.objects.filter(idPaciente_id=id), 'cant_don_asig':ReposicionesAsignadas.objects.count(), 'idDonante':id, 'nombre':nombre, 'apellido':apellido }
    donante_asignado = {'listado_don_asignados': ReposicionesAsignadas.objects.order_by('id'),
                        'cant_don_asig': ReposicionesAsignadas.objects.count(), 'idDonante': id, 'nombre': nombre,
                        'apellido': apellido}
    return render(request, 'reposicionesAsignadas/listadoPacienteAsignado.html',donante_asignado)

def listadoPacientesAplicados(request):
    donante_asignado = {'listado_don_asignados': ReposicionesAsignadas.objects.order_by('id'),
                        'cant_don_asig': ReposicionesAsignadas.objects.count()}
    return render(request, 'reposicionesAsignadas/listadoPacienteAsignado.html',donante_asignado)

def nuevoDonanteAsignar(request, id):
    if request.method == 'POST':
        formaReposicionAsignada = DonanteReposicionAsignadaForm(request.POST['idPaciente':id])
        #formaReposicionAsignada = DonanteReposicionAsignadaForm(request.POST, initial={'idPaciente': id, })
        if formaReposicionAsignada.is_valid():
            formaReposicionAsignada.save()
            return redirect('listadoDonantesAplicados')
    else:
        formaReposicionAsignada = DonanteReposicionAsignadaForm()

    formaReposicionAsignada = {'formaReposicionAsignada': DonanteReposicionAsignadaForm()}
    return render(request, 'reposicionesAsignadas/nuevo.html', formaReposicionAsignada)

def aplicarNuevaReposicion(request, id):

    if request.method == 'POST':
        formaReposicionAsignada = DonanteReposicionAsignadaForm(request.POST)
        if formaReposicionAsignada.is_valid():
            formaReposicionAsignada.save()
            return redirect('listadoPaciente')
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
            return redirect('listadoDonantesAplicados')
    else:

        formaDonanteReposicionAsignada = DonanteReposicionAsignadaForm(instance=donanteReposicionAsignada)

    return render(request, 'reposicionesAsignadas/editar.html', {'formaDonanteReposicionAsignada': formaDonanteReposicionAsignada})

def eliminarDonanteAsignado(request, id):
    donanteAsignado = get_object_or_404(ReposicionesAsignadas, pk=id)
    if donanteAsignado:
        donanteAsignado.delete()
    return redirect('listadoDonantesAplicados')