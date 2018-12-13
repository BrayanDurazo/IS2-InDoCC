from django import forms
from Procesos.models import Proceso


class ProcesoForm(forms.ModelForm):

    class Meta:
        model = Proceso
        exclude = ['Proceso']
