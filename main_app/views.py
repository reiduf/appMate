from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Connection, Job, Todo, Status, Interaction
# Create your views here.
def home(request):
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def jobs_index(request):
  jobs = Job.objects.filter(user = request.user)
  return render(request, 'jobs/index.html', {
    'jobs' : jobs
  })

@login_required
def jobs_detail(request, job_id):
  job = Job.objects.get(id = job_id)
  todos = Todo.objects.filter(job = job_id)
  statuss = Status.objects.filter(job = job_id)
  return render(request, 'jobs/detail.html', {
    'job' : job,
    'todos': todos,
    'statuss' : statuss
  })