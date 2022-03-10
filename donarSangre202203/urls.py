"""donarSangre202203 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pacientes.views import detalleDonanteReposicion, nuevoDonanteReposicion, editarDonanteReposicion, \
    eliminarDonanteReposicion, listadoDonanteReposicion
from donantes.views import listadoDonantes, detalleDonanteInscripto, editarDonanteInscripto, nuevoDonanteAInscribir, \
    eliminarDonanteInscripto
from reposicionesAsignadas.views import listadoPacienteAsignado, nuevoDonanteAsignar, detalleDonanteAsignado, \
    editarDonanteAsignado
from webapp.views import bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='inicio'),
    path('detalleDonanteReposicion/<int:id>', detalleDonanteReposicion),
    path('nuevoDonanteReposicion', nuevoDonanteReposicion),
    path('editarDonanteReposicion/<int:id>', editarDonanteReposicion),
    path('eliminarDonanteReposicion/<int:id>', eliminarDonanteReposicion),
    path('listadoDonanteReposicion', listadoDonanteReposicion,  name='listadoDonantesReposicion'),
    path('listadoDonantes', listadoDonantes, name='listadoDonantes'),
    path('detalleDonanteInscripto/<int:id>', detalleDonanteInscripto),
    path('editarDonanteInscripto/<int:id>', editarDonanteInscripto),
    path('eliminarDonanteInscripto/<int:id>', eliminarDonanteInscripto),
    path('nuevoDonanteAInscribir', nuevoDonanteAInscribir),
    path('listadoPacienteAsignado',listadoPacienteAsignado, name='listadoPacientesAsignado'),
    path('nuevoDonanteAsignar', nuevoDonanteAsignar),
    path('detalleDonanteAsignado/<int:id>', detalleDonanteAsignado),
    path('editarDonanteAsignado/<int:id>', editarDonanteAsignado),

]
