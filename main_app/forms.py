from django.forms import ModelForm
from .models import Todo, Status

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['description']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['description', 'date']