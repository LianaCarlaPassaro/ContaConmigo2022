from django.forms import ModelForm, EmailInput, DateInput
import django.forms.widgets
from pacientes.models import Pacientes


class DonanteReposicionForm(ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        widgets = {
            'mail': EmailInput(attrs={'type': 'email'}),
            'fechaLimite': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'fechaNacimiento': DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
            #'fechaNacimiento': DateInput(format='%d/%m/%Y'),


        }
