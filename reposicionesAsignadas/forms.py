from django.forms import ModelForm, EmailInput, DateInput
import django.forms
from reposicionesAsignadas.models import ReposicionesAsignadas


class DonanteReposicionAsignadaForm(ModelForm):
    class Meta:
        model = ReposicionesAsignadas
        fields = '__all__'
        widgets = {
            'fechaReposicionElegida': DateInput(attrs={'type':'date', 'data-date-format': 'dd-mm-yyyy', 'data-provide': 'datepicker'}, format="%d/%m/%Y"),
                #DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

