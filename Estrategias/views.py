from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from Estrategias.forms import EstrategiaForm
from Estrategias.models import Estrategia


class EstrategiasAdd(TemplateView):
    template_name = 'Estrategias/EstrategiasAgregar.html'

    def get(self, request, **kwargs):
        form = EstrategiaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EstrategiaForm(request.POST)
        if form.is_valid():
            obj = Estrategia.objects.all().first()
            obj.Hay_estrategia_posgrado = form.cleaned_data['Hay_estrategia_posgrado']
            obj.Hay_estrategia_asignaturas = form.cleaned_data['Hay_estrategia_asignaturas']
            obj.Descripcion = form.cleaned_data['Descripcion']
            obj.save()
            return render(request, 'Estrategias/EstrategiasAgregar.html', {'form': form},)
        else:
            form = EstrategiaForm()
        return render(request, 'EstrategiasAgregar.html', {'form': form})


class EstrategiasViewUpdate(TemplateView):
    template_name = 'Estrategias/EstrategiasVerEditar.html'

    def get(self, request, **kwargs):
        form = EstrategiaForm(request.POST)
        estrategia = Estrategia.objects.all().first()
        return render(request, self.template_name, {'form': form, 'estrategia':estrategia})

    def post(self, request):
        form = EstrategiaForm(request.POST)
        obj = Estrategia.objects.all().first()
        if form.is_valid():
            obj.Hay_estrategia_posgrado = form.cleaned_data['Hay_estrategia_posgrado']
            obj.Hay_estrategia_asignaturas = form.cleaned_data['Hay_estrategia_asignaturas']
            obj.Descripcion = form.cleaned_data['Descripcion']
            obj.save()
            return render(request, self.template_name)
        else:
            form = EstrategiaForm()
        return render(request, 'EstrategiasVerEditar.html', {'form': form})

class EstrategiasClean(TemplateView):
    template_name = 'Estrategias/EstrategiasLimpiar.html'

    def get(self, request, **kwargs):
        form = EstrategiaForm(request.POST)
        estrategia = Estrategia.objects.all().first()
        return render(request, self.template_name, {'form': form, 'estrategia':estrategia})

    def post(self, request):
        obj = Estrategia.objects.all().first()
        obj.Hay_estrategia_posgrado = False
        obj.Hay_estrategia_asignaturas = False
        obj.Descripcion = ' '
        obj.save()
        return render(request, self.template_name, {'obj': obj})