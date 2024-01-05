from django.forms import ModelForm, DateInput
from .models import Todo, Status, Job


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['description']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['description', 'date']
        widgets = {
            'date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
        }

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'date', 'salary', 'position', 'notes', 'location', 'progress']
        widgets = {
            'date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
        }