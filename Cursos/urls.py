from django.urls import path
from Cursos.views import CursosAdd, CursosClean, CursosUpdate

urlpatterns = [
    path('Agregar', CursosAdd.as_view(), name='Agregar'),
    path('VerEditar', CursosUpdate.as_view(), name='VerEditar'),
    path('Limpiar', CursosClean.as_view(), name='Limpiar'),
]