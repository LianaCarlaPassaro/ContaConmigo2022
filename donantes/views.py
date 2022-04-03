from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from donantes.forms import DonanteInscriptoForm, EditarDonanteForm
from donantes.models import Donantes


def listadoDonantes(request):
    donante_inscripto = {'listado_don_inscr':Donantes.objects.order_by('id'), 'cant_don':Donantes.objects.count()}
    return render(request, 'donantes/listado.html',donante_inscripto)

def detalleDonanteInscripto(request, id):
    donante_inscripto = {'detalle_don_insc': get_object_or_404(Donantes, pk=id)}
    return render(request, 'donantes/detalle.html', donante_inscripto)

def editarDonanteInscripto(request, id):
    donanteInscripto = get_object_or_404(Donantes, pk=id)
    if request.method == 'POST':
        formaDonanteInscripto = EditarDonanteForm(request.POST, instance=donanteInscripto)
        if formaDonanteInscripto.is_valid():
            formaDonanteInscripto.save()
            return redirect('listadoDonantes')
    else:

        formaDonanteInscripto = EditarDonanteForm(instance=donanteInscripto)

    return render(request, 'donantes/editar.html', {'formaDonanteInscripto': formaDonanteInscripto})

def nuevoDonanteAInscribir(request):
    if request.method == 'POST':
        formaDonanteAInscribir = DonanteInscriptoForm(request.POST)
        if formaDonanteAInscribir.is_valid():
            formaDonanteAInscribir.save()
            return redirect('listadoDonantes')
    else:
        formaDonanteAInscribir = DonanteInscriptoForm()

    formaDonanteAInscribir = {'formaDonanteAInscribir': DonanteInscriptoForm()}
    return render(request, 'donantes/nuevo.html', formaDonanteAInscribir)


def eliminarDonanteInscripto(request, id):
    donanteInscripto = get_object_or_404(Donantes, pk=id)
    if donanteInscripto:
        donanteInscripto.delete()
    return redirect('listadoDonantes')