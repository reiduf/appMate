from django.forms import ModelForm, DateInput, TextInput, Textarea, Select, CheckboxInput
from .models import Todo, Status, Job, Interaction




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
                    'class': 'rounded-full border-gray-300 border-2 my-2 w-full',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'description': Textarea(
                attrs={
                    'placeholder': 'Add notes about the status update',
                    'cols': 30,
                    'rows': 5,
                }
            )
        }

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['position', 'company', 'salary', 'location', 'date', 'progress', 'notes', 'bookmarked']
        widgets = {
            'date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'text-primary text-sm block text-center rounded-full min-w-96 w-full text-center bg-gray-100 border-0', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'notes': Textarea(
                attrs={
                    'class': 'text-primary w-full text-sm block text-center rounded-xl min-w-96 bg-gray-100 border-0',
                    'placeholder': 'Add notes about job here',
                    'cols': 30,
                    'rows': 5,
                }),
            'location': TextInput(
                attrs={
                    'class': 'text-primary text-sm block text-center rounded-full min-w-96 w-full bg-gray-100 border-0',
                    'placeholder': 'San Francisco',
                }),
            'salary': TextInput(
                attrs={
                    'class': 'text-primary text-sm block text-center rounded-full min-w-96 w-full bg-gray-100 border-0',
                    'placeholder': '$89,000',
                }),
            'company': TextInput(
                attrs={
                    'class': 'text-primary text-sm block text-center rounded-full min-w-96 w-full bg-gray-100 border-0',
                    'placeholder': 'Facebook',
                }),
            'position': TextInput(
                attrs={
                    'class': 'text-primary text-sm block text-center rounded-full min-w-96 w-full bg-gray-100 border-0',
                    'placeholder': 'Sr. Frontend Engineer',
                }),
            'progress': Select(
                attrs={
                    'class': 'text-primary text-sm block text-center rounded-full min-w-96 w-full bg-gray-100 border-0',
                 }),
            'bookmarked': CheckboxInput(
                attrs={
                    'class': 'block mx-auto border-2 border-primary',
                 }),
        }

class InteractionForm(ModelForm):
    class Meta:
        model = Interaction
        fields = ['description', 'date']
        widgets = {
            'date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Select a date',
                    'type': 'date'
                }),
            'description': Textarea(
                attrs={
                    'placeholder': 'Got coffee',
                    'cols': 30,
                    'rows': 5,
                }
            )
        }

