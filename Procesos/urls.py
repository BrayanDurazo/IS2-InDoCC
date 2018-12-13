from django.urls import path
from Procesos import views

urlpatterns = [
    path('AgregarContratacion', views.ProcesosAddContratacion.as_view(), name='AgregarContratacion'),
    path('VerEditarContratacion', views.ProcesosUpdateContratacion.as_view(), name='VerEditarContratacion'),
    path('LimpiarContratacion', views.ProcesosCleanContratacion.as_view(), name='LimpiarContratacion'),
    path('AgregarSeleccion', views.ProcesosAddSeleccion.as_view(), name='AgregarSeleccion'),
    path('VerEditarSeleccion', views.ProcesosUpdateSeleccion.as_view(), name='VerEditarSeleccion'),
    path('LimpiarSeleccion', views.ProcesosCleanSeleccion.as_view(), name='LimpiarSeleccion'),
    path('AgregarReclutamiento', views.ProcesosAddReclutamiento.as_view(), name='AgregarReclutamiento'),
    path('VerEditarReclutamiento', views.ProcesosUpdateReclutamiento.as_view(), name='VerEditarReclutamiento'),
    path('LimpiarReclutamiento', views.ProcesosCleanReclutamiento.as_view(), name='LimpiarReclutamiento'),
]
