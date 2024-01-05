from django import forms
from .models import TaskModel
class taskform(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'
        