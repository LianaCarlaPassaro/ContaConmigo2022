from django.forms import ModelForm, EmailInput, DateInput
import django.forms.widgets
from reposicionesAsignadas.models import ReposicionesAsignadas


class DonanteReposicionAsignadaForm(ModelForm):
    class Meta:
        model = ReposicionesAsignadas
        fields = '__all__'
        widgets = {
            'fechaReposicionElegida': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }
