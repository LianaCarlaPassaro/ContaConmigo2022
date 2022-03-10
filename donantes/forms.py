from django.forms import ModelForm, EmailInput, DateInput
import django.forms.widgets

from donantes.models import Donantes

class DonanteInscriptoForm(ModelForm):
    class Meta:
        model = Donantes
        fields = '__all__'
        widgets = {
            'fechaNacimiento':DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'fechaUltimaExtraccion': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'mail': EmailInput(attrs={'type': 'email'}),
        }
