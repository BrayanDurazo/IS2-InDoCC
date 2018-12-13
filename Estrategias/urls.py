from django.urls import path
from Estrategias.views import EstrategiasAdd, EstrategiasViewUpdate, EstrategiasClean

urlpatterns = [
    path('Agregar', EstrategiasAdd.as_view(), name='Agregar'),
    path('VerEditar', EstrategiasViewUpdate.as_view(), name='VerEditar'),
    path('Eliminar', EstrategiasClean.as_view(), name='Eliminar'),
]
