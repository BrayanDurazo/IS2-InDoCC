from django.shortcuts import render
from django.views.generic import TemplateView
from Cursos.forms import DesarrolloForm, ProgramaForm, CursoForm
from Cursos.models import Desarrollo, Programa, Curso

class CursosAdd(TemplateView):
    template_name = 'Cursos/CursosAgregar.html'

    def get(self, request, **kwargs):
        form = DesarrolloForm()
        formprograma = ProgramaForm()
        formcurso = CursoForm()
        return render(request, self.template_name, {'form': form,
                                                    'formprograma': formprograma,
                                                    'formcurso': formcurso})

    def post(self, request):
        form = DesarrolloForm(request.POST)
        formprograma = ProgramaForm(request.POST)
        formcurso = CursoForm(request.POST)
        if form.is_valid():
            obj = Desarrollo.objects.all().first()
            for i in range(0, int(request.POST['formprogramaTablaNumber'])):
                obj2 = Programa(nombre=request.POST["nombre-" + str(i)],
                                beneficios=request.POST["beneficios-" + str(i)])
                obj2.save()
            for i in range(0, int(request.POST['formcursoTablaNumber'])):
                obj3 = Curso(nombre=request.POST["nombre2-" + str(i)],
                             responsabilidad=request.POST["responsabilidad-" + str(i)],
                             ultimo_anio=request.POST["ultimo año-" + str(i)],
                             penultimo_anio=request.POST["penultimo año-" + str(i)],
                             antepenultimo_anio=request.POST["antepenultimo año-" + str(i)],
                             numero_participantes=request.POST["numero de participantes-" + str(i)])
                obj3.save()
            obj.hay_plan_permanente_superacion = form.cleaned_data['hay_plan_permanente_superacion']
            obj.hay_programas_superacion = form.cleaned_data['hay_programas_superacion']
            obj.hay_otra_modalidad = form.cleaned_data['hay_otra_modalidad']
            obj.descripcion_modalidad = form.cleaned_data['descripcion_modalidad']
            obj.hay_plan_formacion = form.cleaned_data['hay_plan_formacion']
            obj.nivel_responsabilidad = form.cleaned_data['nivel_responsabilidad']
            obj.descripcion_formacion = form.cleaned_data['descripcion_formacion']
            obj.save()
            return render(request, self.template_name, {'form': form,
                                                        'formPrograma': formprograma,
                                                        'formcurso': formcurso},)
        else:
            return render(request, 'Estrategias/EstrategiasAgregar.html', {'form': form,
                                                                           'formprograma': formprograma,
                                                                           'formcurso': formcurso})


class CursosClean(TemplateView):
    template_name = 'Cursos/CursosLimpiar.html'

    def get(self, request, **kwargs):
        form = DesarrolloForm(request.POST)
        formprograma = ProgramaForm(request.POST)
        formcurso = CursoForm(request.POST)
        desarrollo = Desarrollo.objects.all().first()

        objs1 = Programa.objects.all()
        objs2 = Curso.objects.all()

        return render(request, self.template_name, {'form': form, 'formPrograma': formprograma,
                                                    'formcurso': formcurso, 'desarrollo': desarrollo,
                                                    'objs1': objs1, 'objs2': objs2})

    def post(self, request):
        obj = Desarrollo.objects.all().first()
        Programa.objects.all().delete()
        Curso.objects.all().delete()
        obj.hay_plan_permanente_superacion = False
        obj.hay_programas_superacion = False
        obj.hay_otra_modalidad = False
        obj.descripcion_modalidad = ""
        obj.hay_plan_formacion = False
        obj.nivel_responsabilidad = 'Institucional'
        obj.descripcion_formacion = ""
        obj.save()
        return render(request, self.template_name, {'obj': obj})

class CursosUpdate(TemplateView):
    template_name = 'Cursos/CursosVerEditar.html'

    def get(self, request, **kwargs):
        form = DesarrolloForm(request.POST)
        formprograma = ProgramaForm(request.POST)
        formcurso = CursoForm(request.POST)
        desarrollo = Desarrollo.objects.all().first()

        objs1 = Programa.objects.all()
        objs2 = Curso.objects.all()

        return render(request, self.template_name, {'form': form, 'formPrograma': formprograma,
                                                    'formcurso': formcurso, 'desarrollo': desarrollo,
                                                    'objs1': objs1, 'objs2': objs2})

    def post(self, request):
        form = DesarrolloForm(request.POST)
        formprograma = ProgramaForm(request.POST)
        formcurso = CursoForm(request.POST)
        if form.is_valid():
            obj = Desarrollo.objects.all().first()
            #for i in range(0, int(request.POST['formprogramaTablaNumber'])):
            #    obj2 = Programa(nombre=request.POST["nombre-" + str(i)],
            #                    beneficios=request.POST["beneficios-" + str(i)])
            #    obj2.save()
            #for i in range(0, int(request.POST['formcursoTablaNumber'])):
            #    obj3 = Curso(nombre=request.POST["nombre2-" + str(i)],
            #                 responsabilidad=request.POST["responsabilidad-" + str(i)],
            #                 ultimo_anio=request.POST["ultimo año-" + str(i)],
            #                 penultimo_anio=request.POST["penultimo año-" + str(i)],
            #                 antepenultimo_anio=request.POST["antepenultimo año-" + str(i)],
            #                 numero_participantes=request.POST["numero de participantes-" + str(i)])
            #    obj3.save()
            obj.hay_plan_permanente_superacion = form.cleaned_data['hay_plan_permanente_superacion']
            obj.hay_programas_superacion = form.cleaned_data['hay_programas_superacion']
            obj.hay_otra_modalidad = form.cleaned_data['hay_otra_modalidad']
            obj.descripcion_modalidad = form.cleaned_data['descripcion_modalidad']
            obj.hay_plan_formacion = form.cleaned_data['hay_plan_formacion']
            obj.nivel_responsabilidad = form.cleaned_data['nivel_responsabilidad']
            obj.descripcion_formacion = form.cleaned_data['descripcion_formacion']
            obj.save()
            return render(request, self.template_name, {'form': form,
                                                        'formPrograma': formprograma,
                                                        'formcurso': formcurso},)
        else:
            return render(request, 'Estrategias/EstrategiasAgregar.html', {'form': form,
                                                                           'formprograma': formprograma,
                                                                           'formcurso': formcurso})
