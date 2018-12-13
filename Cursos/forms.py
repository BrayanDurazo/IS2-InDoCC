from django import forms
from Cursos.models import Programa, Curso, Desarrollo


class ProgramaForm(forms.ModelForm):

    class Meta:
        model = Programa
        exclude = ['programa_id']


class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        exclude = ['curso_id']


class DesarrolloForm(forms.ModelForm):

    class Meta:
        model = Desarrollo
        exclude = ['desarrollo_id']
