from django import forms
from brake_classroom.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['created', 'co2_saved', 'money_saved']
