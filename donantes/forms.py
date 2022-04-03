from django.forms import ModelForm, EmailInput, DateInput
import django.forms.widgets
from django import forms

from donantes.models import Donantes

class DonanteInscriptoForm(ModelForm):
    class Meta:
        model = Donantes
        fields = '__all__'
       # widgets = {
        #    'fechaNacimiento':DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
         #   'fechaUltimaExtraccion': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
          #  'mail': EmailInput(attrs={'type': 'email'}),
        #}
        widgets = {
            'fechaNacimiento': forms.DateInput(
                attrs={'type': 'date', 'data-date-format': 'dd-mm-yyyy', 'data-provide': 'datepicker'},
                format="%d/%m/%Y"),
            'mail': EmailInput(attrs={'type': 'email'}),
            'fechaUltimaExtraccion': forms.DateInput(
                attrs={'type': 'date', 'data-date-format': 'dd-mm-yyyy', 'data-provide': 'datepicker'},
                format="%d/%m/%Y"),
        }

class EditarDonanteForm(ModelForm):
    class Meta:
        model = Donantes
        fields = '__all__'
        widgets = {
            'fechaNacimiento': forms.DateInput(format=('%Y-%m-%d'),
                                               attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                      'type': 'date'}),
            'mail': EmailInput(attrs={'type': 'email'}),
            'fechaUltimaExtraccion': forms.DateInput(format=('%Y-%m-%d'),
                                           attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                  'type': 'date'}),
        }