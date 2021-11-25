from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    # generate all editable fields of Project Model from models.py
    class Meta:
        model = Project
        fields = '__all__'