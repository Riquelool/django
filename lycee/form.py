from django.forms.models import ModelForm
from .models import Student,Presence

class PresenceForm(ModelForm):
  class Meta:
    # la ref du ModEle
    model = Presence

    # liste des champs A Editer
    fields =(
      "date",
      "ismissing",
      "Reasson",
      "students", 
    )

class StudentForm(ModelForm):

  class Meta:
    # la ref du ModEle
    model = Student

    # liste des champs A Editer
    fields  = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus",
    )