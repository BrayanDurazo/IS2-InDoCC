from django import forms
from Estrategias.models import Estrategia


class EstrategiaForm(forms.ModelForm):

    class Meta:
        model = Estrategia
        exclude = ['Estrategia_id']
