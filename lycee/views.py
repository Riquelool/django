from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus,Student,Presence
from .form import StudentForm,PresenceForm
from django.views.generic import CreateView,UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
  result_student = Student.objects.filter(cursus=cursus_id)
  # contexte
  context = { 'liste' : result_student}
  # utilisation du template intEgrE
  return render (request, 'lycee/detail.html', context)

def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'liste': result_list,}
    return render (request, 'lycee/student/detail_student.html' , context)

class StudentCreateView(CreateView):
  # ref au modele
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/create.html"

  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

def detailpresence(request,presence_id):
  result = get_object_or_404(Presence, pk=presence_id)
  template = "lycee/student/detailpresence.html"
    # context
  cont = {
    'list': result,
    'student' : Student.objects.get(id=result.students.id)
  }
  return render(request, template, cont)


class PresenceCreateView(CreateView):
  # ref au modele
  model = Presence
  # ref au formulaire
  form_class = PresenceForm
  # le nom du render
  template_name = "lycee/student/Presence.html"

  def get_success_url(self):
    return reverse ("detailpresence", args=(self.object.pk,))

class ModifyStudent(UpdateView):
  model = Student
  form_class = StudentForm
  template_name = "lycee/edit-piaf/edit.html"

  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

def callofroll(request):
  if request.method == 'POST':
    date = request.POST.get("date")
    for estudiante in Student:
      missing = request.POST.get('estudiante'+str(estudiante.id), "off")
    

