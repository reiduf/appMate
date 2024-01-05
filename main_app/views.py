from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Connection, Job, Todo, Status, Interaction
from .forms import TodoForm, StatusForm, JobForm


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
  todo_form = TodoForm()
  status_form = StatusForm()
  return render(request, 'jobs/detail.html', {
    'job' : job,
    'todos': todos,
    'statuss' : statuss,
    'todo_form': todo_form,
    'status_form': status_form
  })


class JobCreate(LoginRequiredMixin, CreateView):
  model = Job
  form_class = JobForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class JobUpdate(LoginRequiredMixin, UpdateView):
  model = Job
  form_class = JobForm
  

class JobDelete(LoginRequiredMixin, DeleteView):
  model = Job
  success_url = '/jobs'


@login_required
def add_todo(request, job_id):
  form = TodoForm(request.POST)
  if form.is_valid():
    new_todo = form.save(commit=False)
    # below could be an issue
    new_todo.job_id = job_id
    new_todo.save()
  return redirect('detail', job_id=job_id)


@login_required
def update_todo(request, job_id, todo_id):
  todo = Todo.objects.get(id = todo_id)
  if todo.done == False:
    todo.done = True
  else:
    todo.done = False
  todo.save()
  return redirect('detail', job_id=job_id)

@login_required
def delete_todo(request, job_id, todo_id):
  todo = Todo.objects.get(id = todo_id)
  todo.delete()
  return redirect('detail', job_id=job_id)


@login_required
def add_status(request, job_id):
  form = StatusForm(request.POST)
  if form.is_valid():
    new_status = form.save(commit=False)
    new_status.job_id = job_id
    new_status.save()
  return redirect('detail', job_id=job_id)


@login_required
def delete_status(request, job_id, status_id):
  status = Status.objects.get(id = status_id)
  status.delete()
  return redirect('detail', job_id=job_id)