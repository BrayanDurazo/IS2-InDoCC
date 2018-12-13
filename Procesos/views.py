from django.shortcuts import render
from django.views.generic import TemplateView
from Procesos.forms import ProcesoForm
from Procesos.models import Proceso


class ProcesosAddContratacion(TemplateView):
    template_name = 'Procesos/AgregarContratacion.html'

    def get(self, request, **kwargs):
        form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProcesoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Proceso.objects.all().filter(Proceso="Contratacion").get()
            obj.Existe_proceso_formal = form.cleaned_data['Existe_proceso_formal']
            obj.Descripcion_Proceso = form.cleaned_data['Descripcion_Proceso']
            obj.Hay_reglamento = form.cleaned_data['Hay_reglamento']
            obj.evidencia = request.FILES['evidencia']
            obj.save()
            return render(request, self.template_name, {'form': form})
        else:
            form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

class ProcesosUpdateContratacion(TemplateView):
    template_name = 'Procesos/VerEditarContratacion.html'

    def get(self, request, **kwargs):
        form = ProcesoForm(request.POST)
        proceso = Proceso.objects.all().filter(Proceso="Contratacion").get()
        return render(request, self.template_name, {'form': form, 'proceso': proceso})

    def post(self, request):
        form = ProcesoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Proceso.objects.all().filter(Proceso="Contratacion").get()
            obj.Existe_proceso_formal = form.cleaned_data['Existe_proceso_formal']
            obj.Descripcion_Proceso = form.cleaned_data['Descripcion_Proceso']
            obj.Hay_reglamento = form.cleaned_data['Hay_reglamento']
            obj.evidencia = request.FILES['evidencia']
            obj.save()
            return render(request, self.template_name, {'form': form})
        else:
            form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

class ProcesosCleanContratacion(TemplateView):
    template_name = 'Procesos/LimpiarContratacion.html'

    def get(self, request, **kwargs):
        form = ProcesoForm(request.POST)
        proceso = Proceso.objects.all().filter(Proceso="Contratacion").get()
        return render(request, self.template_name, {'form': form, 'proceso': proceso})

    def post(self, request):
        obj = Proceso.objects.all().filter(Proceso="Contratacion").get()
        obj.Existe_proceso_formal = False
        obj.Descripcion_Proceso = ""
        obj.Hay_reglamento = False
        obj.evidencia.delete()
        obj.save()
        return render(request, self.template_name, {'obj': obj})

# ----------------------------------------------------------------------------------------------------------------------

class ProcesosAddSeleccion(TemplateView):
    template_name = 'Procesos/AgregarSeleccion.html'

    def get(self, request, **kwargs):
        form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProcesoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Proceso.objects.all().filter(Proceso="Seleccion").get()
            obj.Existe_proceso_formal = form.cleaned_data['Existe_proceso_formal']
            obj.Descripcion_Proceso = form.cleaned_data['Descripcion_Proceso']
            obj.Hay_reglamento = form.cleaned_data['Hay_reglamento']
            obj.evidencia = request.FILES['evidencia']
            obj.save()
            return render(request, self.template_name, {'form': form})
        else:
            form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

class ProcesosUpdateSeleccion(TemplateView):
    template_name = 'Procesos/VerEditarSeleccion.html'

    def get(self, request, **kwargs):
        form = ProcesoForm(request.POST)
        proceso = Proceso.objects.all().filter(Proceso="Seleccion").get()
        return render(request, self.template_name, {'form': form, 'proceso': proceso})

    def post(self, request):
        form = ProcesoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Proceso.objects.all().filter(Proceso="Seleccion").get()
            obj.Existe_proceso_formal = form.cleaned_data['Existe_proceso_formal']
            obj.Descripcion_Proceso = form.cleaned_data['Descripcion_Proceso']
            obj.Hay_reglamento = form.cleaned_data['Hay_reglamento']
            obj.evidencia = request.FILES['evidencia']
            obj.save()
            return render(request, self.template_name, {'form': form})
        else:
            form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

class ProcesosCleanSeleccion(TemplateView):
    template_name = 'Procesos/LimpiarSeleccion.html'

    def get(self, request, **kwargs):
        form = ProcesoForm(request.POST)
        proceso = Proceso.objects.all().filter(Proceso="Seleccion").get()
        return render(request, self.template_name, {'form': form, 'proceso': proceso})

    def post(self, request):
        obj = Proceso.objects.all().filter(Proceso="Seleccion").get()
        obj.Existe_proceso_formal = False
        obj.Descripcion_Proceso = ""
        obj.Hay_reglamento = False
        obj.evidencia.delete()
        obj.save()
        return render(request, self.template_name, {'obj': obj})
# ----------------------------------------------------------------------------------------------------------------------

class ProcesosAddReclutamiento(TemplateView):
    template_name = 'Procesos/AgregarReclutamiento.html'

    def get(self, request, **kwargs):
        form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProcesoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Proceso.objects.all().filter(Proceso="Reclutamiento").get()
            obj.Existe_proceso_formal = form.cleaned_data['Existe_proceso_formal']
            obj.Descripcion_Proceso = form.cleaned_data['Descripcion_Proceso']
            obj.Hay_reglamento = form.cleaned_data['Hay_reglamento']
            obj.evidencia = request.FILES['evidencia']
            obj.save()
            return render(request, self.template_name, {'form': form})
        else:
            form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

class ProcesosUpdateReclutamiento(TemplateView):
    template_name = 'Procesos/VerEditarReclutamiento.html'

    def get(self, request, **kwargs):
        form = ProcesoForm(request.POST)
        proceso = Proceso.objects.all().filter(Proceso="Reclutamiento").get()
        return render(request, self.template_name, {'form': form, 'proceso': proceso})

    def post(self, request):
        form = ProcesoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Proceso.objects.all().filter(Proceso="Reclutamiento").get()
            obj.Existe_proceso_formal = form.cleaned_data['Existe_proceso_formal']
            obj.Descripcion_Proceso = form.cleaned_data['Descripcion_Proceso']
            obj.Hay_reglamento = form.cleaned_data['Hay_reglamento']
            obj.evidencia = request.FILES['evidencia']
            obj.save()
            return render(request, self.template_name, {'form': form})
        else:
            form = ProcesoForm()
        return render(request, self.template_name, {'form': form})

class ProcesosCleanReclutamiento(TemplateView):
    template_name = 'Procesos/LimpiarReclutamiento.html'

    def get(self, request, **kwargs):
        form = ProcesoForm(request.POST)
        proceso = Proceso.objects.all().filter(Proceso="Reclutamiento").get()
        return render(request, self.template_name, {'form': form, 'proceso': proceso})

    def post(self, request):
        obj = Proceso.objects.all().filter(Proceso="Reclutamiento").get()
        obj.Existe_proceso_formal = False
        obj.Descripcion_Proceso = ""
        obj.Hay_reglamento = False
        obj.evidencia.delete()
        obj.save()
        return render(request, self.template_name, {'obj': obj})
